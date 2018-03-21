import RPi.GPIO as GPIO
import time
import os
import yaml
from gardenlogger import Gardenlogger
from sensor import MiFloraSensor
dirname = os.path.dirname(__file__)

class Gardenbot:
    def __init__(self, relay_channel_ventile=17, float_switch_in=25, float_switch_out=4, watering_time=90):
        GPIO.setmode(GPIO.BCM)
        self.relay_channel_pump = relay_channel_ventile
        self.float_switch_in = float_switch_in
        self.float_switch_out = float_switch_out
        self.watering_time = watering_time
        self.gl = Gardenlogger("/var/log/gardenbot.log")
        self.thresholds = Gardenbot.load_yaml(os.path.join("thresholds.yaml")
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

    @staticmethod
    def load_yaml(file):
        with open(file) as f:
            return yaml.load(f)

    '''Returns True, if the soil is wet enough and False if it is too dry'''
    def soil_is_wet(self):
        moisture = self.sensor.get_miflora_data()['moisture']
        moisture_threshold = self.thresholds.get('moisture')
        return moisture > moisture_threshold

    '''Returns a boolean if the soil is fertile or not'''
    def soil_is_fertile(self):
        fertility = self.sensor.get_miflora_data()['conductivity']
        fertility_threshold = self.thresholds.get('conductivity')
        return fertility > fertility_threshold

if __name__ == '__main__':
    gb = Gardenbot()
    gb.setup_pins()
    gb.close_water()
    gb.measure_moisture()
    gb.close()
    gb.exit()