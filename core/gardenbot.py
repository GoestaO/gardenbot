#import RPi.GPIO as GPIO
from gpiocrust import Header, OutputPin, InputPin
import time
import os
from core.sensor import MiFloraSensor

dirname = os.path.dirname(__file__)
from database.models import Protocol
from database.db import persist
from core.configuration import load_yaml
thresholds = load_yaml(os.path.join(dirname, "thresholds.yaml"))

class Gardenbot:
    def __init__(self, relay_channel_pump=17, float_switch_in=25, float_switch_out=4, watering_time=90):
        self.watering_time = watering_time
        self.sensor = MiFloraSensor()
        with Header() as header:
            self.pump_pin = OutputPin(relay_channel_pump, value=1)
            self.float_switch_in_pin = InputPin(float_switch_in)
            self.float_switch_out_pin = OutputPin(float_switch_out, value=0)


    @staticmethod
    def relay_close_circuit(pin: OutputPin):
        pin.value = 0

    @staticmethod
    def relay_open_circuit(pin: OutputPin):
        pin.value = 1

    def water_plants(self, watering_time=30):
        p = Protocol(water=1)
        persist(p)
        self.open_water()
        time.sleep(watering_time)
        self.close_water()

    def enough_water(self):
        self.float_switch_out_pin = True

        # wait a bit
        time.sleep(1)

        # signal = GPIO.input(self.float_switch_in)
        # True = circuit close, False = circuit open

        signal = self.float_switch_in_pin.value
        time.sleep(1)

        #GPIO.output(self.float_switch_out, False)
        self.float_switch_out_pin = False
        return not signal

    def open_water(self):
        Gardenbot.relay_close_circuit(self.pump_pin)

    def close_water(self):
        Gardenbot.relay_open_circuit(self.pump_pin)

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
    gb.close_water()
