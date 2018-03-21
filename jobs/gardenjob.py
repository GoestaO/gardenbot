import time, sys, os
dirname = os.path.dirname(__file__)
gardenbot_file = os.path.join(dirname, '..', 'gardenbot.py')
sys.path.insert(1, gardenbot_file)
from gardenbot import Gardenbot

class Gardenjob(Gardenbot):
    def __init__(self):
        super().__init__()

    '''
    This function measures the moisture of the soil. If it is too dry, the ventile will be opened, otherwise nothing will happen
    '''

    def measure_moisture(self, channel):
        self.start_sensor()

        # wait a bit
        time.sleep(1)
        if not Gardenbot.soil_is_wet():
            self.water_plants()
        else:
            self.close_water()
            self.gl.logger.info("Wet enough".format())
            self.stop_sensor()
            self.close()

    def exit(self):
        sys.exit()

if __name__ == '__main__':
    gj = Gardenjob()
    gj.setup_pins()
    gj.close_water()
    gj.measure_moisture(channel=gj.moisture_sensor_channel)
    gj.close()
    gj.exit()
