#import RPi.GPIO as GPIO
from gpiocrust import Header, OutputPin, InputPin
import time
import os
from core.sensor import MiFloraSensor

dirname = os.path.dirname(__file__)
parentdir = os.path.join(dirname, os.pardir)
from database.models import Protocol
from database.db import persist
from util.helper import load_yaml
configuration = load_yaml(os.path.join(parentdir, "configuration.yaml"))
thresholds = configuration.get('thresholds')

class Gardenbot:
    def __init__(self, relay_channel_pump=10, float_switch_in=16, float_switch_out=7, watering_time=90):
        self.watering_time = watering_time
        self.sensor = MiFloraSensor()
        with Header() as header:
            self.pump_pin = OutputPin(relay_channel_pump, value=1)


    @staticmethod
    def relay_close_circuit(pin: OutputPin):
        pin.value = 0

    @staticmethod
    def relay_open_circuit(pin: OutputPin):
        pin.value = 1

    def water_plants(self, watering_time=30):
        p = Protocol(water=1)
        persist(p)
        self.start_pump()
        time.sleep(watering_time)
        self.stop_pump()


    def start_pump(self):
        Gardenbot.relay_close_circuit(self.pump_pin)

    def stop_pump(self):
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
    gb.stop_pump()
