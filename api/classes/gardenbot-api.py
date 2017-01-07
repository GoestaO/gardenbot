#from moisture import Gardenbot
import time
import connexion
#from moisture import Gardenbot
from . import authservice

@authservice.requires_token
def water_plants(seconds):

    print("Waiting now...")
    watering_time = int(seconds)
    time.sleep(watering_time)
    #super(GardenbotAPI, self).water_plants(watering_time)
    print("Exit")



