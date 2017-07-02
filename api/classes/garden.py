import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
# from models import User, Protocol
# from app import db
from gardenlogger import Gardenlogger


class Gardenbot:
    def __init__(self, moisture_sensor_channel=14, relay_channel_ventile=17, relay_channel_sensor=18,
                 float_switch_in=25, float_switch_out=4, watering_time=90):
        GPIO.setmode(GPIO.BCM)
        self.moisture_sensor_channel = moisture_sensor_channel
        self.relay_channel_ventile = relay_channel_ventile
        self.relay_channel_sensor = relay_channel_sensor
        self.float_switch_in = float_switch_in
        self.float_switch_out = float_switch_out
        self.watering_time = watering_time
        self.gl = Gardenlogger("/var/log/gardenbot.log")

    def setup_pins(self):
        GPIO.setup(self.moisture_sensor_channel, GPIO.IN)
        GPIO.setup(self.relay_channel_ventile, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.relay_channel_sensor, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.float_switch_in, GPIO.IN)
        GPIO.setup(self.float_switch_out, GPIO.OUT, initial=GPIO.LOW)

    '''
    This function measures the moisture of the soil. If it is too dry, the ventile will be opened, otherwise nothing will happen
    '''

    def measure_moisture(self, channel):
        self.start_sensor()

        # wait a bit
        time.sleep(1)
        if not Gardenbot.soil_is_wet(channel):
            self.water_plants()
        else:
            self.close_water()
            self.gl.logger.info("Wet enough".format())
            self.stop_sensor()
            self.close()

    def start_sensor(self):
        # print "starting the sensor..."
        Gardenbot.relay_close_circuit(self.relay_channel_sensor)

    def stop_sensor(self):
        Gardenbot.relay_open_circuit(self.relay_channel_sensor)

    @staticmethod
    def relay_close_circuit(channel):
        GPIO.output(channel, False)

    @staticmethod
    def relay_open_circuit(channel):
        GPIO.output(channel, True)

    def water_plants(self, watering_time=None):
        self.stop_sensor()

        if watering_time == None:
            watering_time = self.watering_time
        self.gl.logger.info("Watering: {}".format(watering_time))
        # self.setup_pump()
        self.open_water()
        time.sleep(watering_time)
        self.close_water()

    def enough_water(self):
        GPIO.output(self.float_switch_out, True)
        time.sleep(1)
        signal = GPIO.input(self.float_switch_in)
        GPIO.output(self.float_switch_out, False)
        return not signal

    def setup_pump(self):
        for i in range(2):
            self.open_water()
            time.sleep(2)
            self.close_water()
            time.sleep(1)

    def open_water(self):
        Gardenbot.relay_close_circuit(self.relay_channel_ventile)

    def close_water(self):
        Gardenbot.relay_open_circuit(self.relay_channel_ventile)

    def close(self):
        GPIO.cleanup()

    def exit(self):
        sys.exit()

    '''Returns True, if the soil is wet enough and False if it is too dry'''

    @staticmethod
    def soil_is_wet(channel):
        return not GPIO.input(channel)


if __name__ == '__main__':
    gb = Gardenbot()
    gb.setup_pins()
    gb.close_water()
    gb.measure_moisture(channel=gb.moisture_sensor_channel)
    gb.close()
    gb.exit()
