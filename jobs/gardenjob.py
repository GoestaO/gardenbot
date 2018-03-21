import time, sys, os

dirname = os.path.dirname(__file__)
parent_dir = os.path.join(dirname, '..')
sys.path.insert(1, parent_dir)
from gardenbot import Gardenbot


class Gardenjob(Gardenbot):
    def __init__(self):
        super().__init__()

    '''
    This function measures the moisture of the soil. If it is too dry, the ventile will be opened, otherwise nothing will happen
    '''

    def measure_moisture(self):
        # wait a bit
        time.sleep(1)
        if not super().soil_is_wet():
            self.water_plants()
        else:
            self.close_water()
            self.gl.logger.info("Wet enough".format())
            self.close()
    @staticmethod
    def exit():
        sys.exit()


if __name__ == '__main__':
    gj = Gardenjob()
    gj.setup_pins()
    gj.close_water()
    gj.measure_moisture()
    gj.close()
    Gardenjob.exit()
