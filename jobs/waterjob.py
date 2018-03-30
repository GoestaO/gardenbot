import time, sys, os

dirname = os.path.dirname(__file__)
parent_dir = os.path.join(dirname, '..')
sys.path.insert(1, parent_dir)
from core.gardenbot import Gardenbot
from database.models import Protocol


class Waterjob(Gardenbot):
    def __init__(self):
        super().__init__()

    '''
    This function measures the moisture of the soil. If it is too dry, the ventile will be opened, otherwise nothing will happen
    '''

    def measure_moisture(self):
        # Call sensor
        sensor_data = self.sensor.get_miflora_data()

        # Create protocol based on sensor data
        p = Protocol()

        # wait a bit
        time.sleep(1)
        if not super().soil_is_wet(sensor_data):
            p.water = 1
            self.water_plants()
        else:
            self.close_water()
            p.water = 0
            self.close()

        # Persist protocol
        Gardenbot.persist(p)

    @staticmethod
    def exit():
        sys.exit()




if __name__ == '__main__':
    gj = Waterjob()
    gj.setup_pins()
    gj.close_water()
    gj.measure_moisture()
    gj.close()
    Waterjob.exit()
