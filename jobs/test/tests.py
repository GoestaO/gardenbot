import unittest
import time
import random


class GardenbotDouble:

    def __init__(self, watering_time):
        self.watering_time = watering_time


    # def setup_pins(self):
    #     return "Setting up the pins."


    def measure_moisture(self, soil_is_wet):
        self.start_sensor()

        # wait a bit
        time.sleep(1)
        if not soil_is_wet:
            self.water_plants()
            return "Plants watered."
        else:
            self.close_water()
            self.stop_sensor()
            self.close()
        return "Plants not watered."


    @staticmethod
    def relay_close_circuit(channel):
        return "Circuit closed."

    @staticmethod
    def relay_open_circuit(channel):
        return "Circuit open."

    def water_plants(self, watering_time=None):
        self.stop_sensor()

        if watering_time is None:
            watering_time = self.watering_time

        self.open_water()
        time.sleep(watering_time)
        self.close_water()

    def setup_pump(self):
        for i in range(2):
            self.open_water()
            time.sleep(2)
            self.close_water()
            time.sleep(1)

    def open_water(self):
        return "Open water."

    def close_water(self):
        return "Close water."

    def start_sensor(self):
        return "Start sensor"

    def stop_sensor(self):
        return "Stop sensor"

    def close(self):
        return "Cleaning up the GPIOs"

    def exit(self):
        return "Exit."

    '''Returns random value for soil status'''

    @staticmethod
    def soil_is_wet():
        soil_status_list = [True, False]
        return random.choice(soil_status_list)


class GardenbotTest(unittest.TestCase):

    def setUp(self):
        self.gardenbot_double = GardenbotDouble(watering_time=5)

    # def test_setup_pins(self):
    #     self.gardenbot_double.setup_pins

    def test_measure_moisture_with_wet_soil(self):
        soil_is_wet = True
        returnValue = self.gardenbot_double.measure_moisture(soil_is_wet=soil_is_wet)
        self.assertEqual(returnValue, "Plants not watered.")

    def test_measure_moisture_with_dry_soil(self):
        soil_is_wet = False
        returnValue = self.gardenbot_double.measure_moisture(soil_is_wet=soil_is_wet)
        self.assertEqual(returnValue, "Plants watered.")









