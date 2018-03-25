import time, sys, os
import json

dirname = os.path.dirname(__file__)
parent_dir = os.path.join(dirname, '..')
sys.path.insert(1, parent_dir)
from database.db import persist
from database.models import SensorData
from sensor import MiFloraSensor


class Polljob(MiFloraSensor):
    def __init__(self):
        super().__init__()

    def save(self):
        # Call sensor
        sensor_data = json.loads(self.get_miflora_data())
        entity = MiFloraSensor.get_sensor_data(sensor_data)
        persist(entity)


if __name__ == "__main__":
    poll = Polljob()
    poll.save()
