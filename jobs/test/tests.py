import sys

sys.path.append("/home/pi/gardenbot")
from gardenjob import Gardenbot
import time
import random
import mock
from mock import MagicMock
import unittest


# @mock.patch("RPi.GPIO")
class GardenbotTest(unittest.TestCase):
    def setUp(self):
        self.gardenbot_test_object = Gardenbot(watering_time=5)

        '''Mock the hardware methods in order to prevent pumping and watering...'''
        self.gardenbot_test_object.close_water = MagicMock()
        self.gardenbot_test_object.water_plants = MagicMock()
        self.gardenbot_test_object.start_sensor = MagicMock()
        self.gardenbot_test_object.water_plants = MagicMock()
        self.gardenbot_test_object.stop_sensor = MagicMock()

    def test_measure_moisture_with_dry_soil(self):
        Gardenbot.soil_is_wet = MagicMock(return_value="False")
        self.gardenbot_test_object.measure_moisture(14)
        self.assertTrue(self.gardenbot_test_object.water_plants.assert_called(), False)

    def test_measure_moisture_with_wet_soil(self):
        Gardenbot.soil_is_wet = MagicMock(return_value="True")
        self.assertEquals(Gardenbot.soil_is_wet(14), "True")
        self.gardenbot_test_object.measure_moisture(14)
        self.assertTrue(self.gardenbot_test_object.water_plants.assert_not_called(), True)


    def test_sensor_stopped(self):
        Gardenbot.soil_is_wet = MagicMock(return_value="True")
        self.gardenbot_test_object.measure_moisture(14)
        self.assertTrue(self.gardenbot_test_object.stop_sensor.assert_called(), True)




