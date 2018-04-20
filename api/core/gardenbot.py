#import RPi.GPIO as GPIO
import os,sys
import time
sys.path.extend('..')
dirname = os.path.dirname(os.path.realpath(__file__))
APPLICATION_ROOT = os.path.abspath(os.path.join(dirname, '..'))
import RPi.GPIO as GPIO
from core.sensor import MiFloraSensor
from database.models import Protocol
from database.db import persist
from util.helper import load_yaml
thresholds = load_yaml(os.path.join(APPLICATION_ROOT, 'configuration.yaml')).get('thresholds')




class Gardenbot:
    def __init__(self, relay_channel_pump=15, float_switch_in=25, float_switch_out=4, watering_time=90):
        self.watering_time = watering_time
        self.sensor = MiFloraSensor()
        self.relay_channel_pump = relay_channel_pump
        self.float_switch_in = float_switch_in
        self.float_switch_out = float_switch_out
        self.setup_pins()


    @staticmethod
    def relay_close_circuit(channel):
        GPIO.output(channel, False)

    def setup_pins(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_channel_pump, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.float_switch_in, GPIO.IN)
        GPIO.setup(self.float_switch_out, GPIO.OUT, initial=GPIO.LOW)

    @staticmethod
    def relay_open_circuit(channel):
        GPIO.output(channel, True)

    def water_plants(self, watering_time=30):
        p = Protocol(water=1)
        persist(p)
        self.open_water()
        time.sleep(watering_time)
        self.close_water()
        self.close()

    def enough_water(self):
        self.float_switch_out_pin = True

        # wait a bit
        time.sleep(1)

        signal = GPIO.input(self.float_switch_in)
        # True = circuit close, False = circuit open

        time.sleep(1)

        GPIO.output(self.float_switch_out, False)
        self.close()
        return not signal

    def open_water(self):
        Gardenbot.relay_close_circuit(self.relay_channel_pump)

    def close_water(self):
        Gardenbot.relay_open_circuit(self.relay_channel_pump)

    '''Returns True, if the soil is wet enough and False if it is too dry'''
    @staticmethod
    def soil_is_wet(sensor_data):
        moisture = sensor_data.get('moisture')
        moisture_threshold = thresholds.get('moisture')
        return moisture > moisture_threshold

    '''Returns a boolean if the soil is fertile or not'''
    @staticmethod
    def soil_is_fertile(sensor_data):
        fertility = sensor_data.get('conductivity')
        fertility_threshold = thresholds.get('conductivity')
        return fertility > fertility_threshold

    @staticmethod
    def persist(entity):
        persist(entity)

    def close(self):
        GPIO.cleanup()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    gb = Gardenbot()
    gb.water_plants(10)
    gb.close()
    gb.exit()
