import time, sys, os
import json

dirname = os.path.dirname(__file__)
parent_dir = os.path.join(dirname, '..')
sys.path.insert(1, parent_dir)
from gardenbot import Gardenbot
from database.models import SensorData


class Polljob(Gardenbot):
    def __init__(self):
        super().__init__()

    def save(self):
        # Call sensor
        sensor_data = json.loads(self.sensor.get_miflora_data())
        entity = SensorData(temperature=sensor_data['temperature'], moisture=sensor_data['moisture'],
                       fertility=sensor_data['conductivity'])
        Gardenbot.persist(entity)


if __name__ == "__main__":
    poll = Polljob()
    poll.save()
