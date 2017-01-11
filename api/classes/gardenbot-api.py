#from moisture import Gardenbot
import time
import connexion
from flask import Response
#from moisture import Gardenbot
from . import authservice

@authservice.requires_token
def water_plants(seconds):

    #print("Waiting now...")
    watering_time = int(seconds)
    time.sleep(watering_time)
    #super(GardenbotAPI, self).water_plants(watering_time)
    msg = "The plants have been watered for {0} seconds".format(seconds)
    return Response(msg)



