import RPi.GPIO as GPIO
import time
import os
from gardenlogger import Gardenlogger
from core.sensor import MiFloraSensor

dirname = os.path.dirname(__file__)
from database.models import Protocol
from database.db import persist
from core.configuration import load_yaml
thresholds = load_yaml(os.path.join(dirname, "thresholds.yaml"))

class Gardenbot:
    def __init__(self, relay_channel_ventile=17, float_switch_in=25, float_switch_out=4, watering_time=90):
        GPIO.setmode(GPIO.BCM)
        self.relay_channel_pump = relay_channel_ventile
        self.float_switch_in = float_switch_in
        self.float_switch_out = float_switch_out
        self.watering_time = watering_time
        self.sensor = MiFloraSensor()


    def setup_pins(self):
        GPIO.setup(self.relay_channel_pump, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.float_switch_in, GPIO.IN)
        GPIO.setup(self.float_switch_out, GPIO.OUT, initial=GPIO.LOW)

    @staticmethod
    def relay_close_circuit(channel):
        GPIO.output(channel, False)

    @staticmethod
    def relay_open_circuit(channel):
        GPIO.output(channel, True)

    def water_plants(self, watering_time=30):
        p = Protocol(water=1)
        self.gl.logger.info("Watering: {}".format(watering_time))
        self.open_water()
        time.sleep(watering_time)
        self.close_water()

    def enough_water(self):
        GPIO.output(self.float_switch_out, True)
        time.sleep(1)
        signal = GPIO.input(self.float_switch_in)
        GPIO.output(self.float_switch_out, False)
        return not signal

    def open_water(self):
        Gardenbot.relay_close_circuit(self.relay_channel_pump)

    def close_water(self):
        Gardenbot.relay_open_circuit(self.relay_channel_pump)

    def close(self):
        GPIO.cleanup()

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



if __name__ == '__main__':
    gb = Gardenbot()
    gb.setup_pins()
    gb.close_water()
    gb.measure_moisture()
    gb.close()
    gb.exit()