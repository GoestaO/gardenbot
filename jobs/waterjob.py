import os
import sys
import time

from .gardenbot_client import check, water_plants

class Waterjob():
    def __init__(self):
        super().__init__()

    '''
    This function measures the moisture of the soil. If it is too dry, the pump will be started, otherwise nothing will happen
    '''
    def measure_moisture(self):
        # Is soil wet enough?
        soil_is_wet = check()
        if not soil_is_wet:
            water_plants(30)

    @staticmethod
    def exit():
        sys.exit()


if __name__ == '__main__':
    wj = Waterjob()
    wj.measure_moisture()
    Waterjob.exit()
