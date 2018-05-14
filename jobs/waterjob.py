import sys
import os
from gardenbot_client import check, water_plants

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

class Waterjob():
    def __init__(self):
        super().__init__()


    '''
    This function measures the moisture of the soil. If it is too dry, the pump will be started, otherwise nothing will happen
    '''
    def water_or_not(self):
        # Is soil wet enough?
        soil_is_wet = check()
        if soil_is_wet == 'False':
            water_plants(30)


    @staticmethod
    def exit():
        sys.exit()



if __name__ == '__main__':
    wj = Waterjob()
    wj.water_or_not()
    Waterjob.exit()

