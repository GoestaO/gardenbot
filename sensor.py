from miflora.backends.gatttool import GatttoolBackend
from miflora.miflora_poller import MiFloraPoller, MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import json
from database.models import SensorData, Protocol
from database.db import persist

test_data = {'battery': 99, 'firmware': '3.1.8', 'name': 'Flower care', 'conductivity': 476, 'temperature': 5.6,
             'moisture': 12, 'light': 0}


class MiFloraSensor:
    def __init__(self):
        self.poller = MiFloraPoller('C4:7C:8D:65:B5:CF', GatttoolBackend)

    def get_miflora_data(self):
        d = dict()
        d['firmware'] = self.poller.firmware_version()
        d['name'] = self.poller.name()
        d['temperature'] = self.poller.parameter_value(MI_TEMPERATURE)
        d['moisture'] = self.poller.parameter_value(MI_MOISTURE)
        d['light'] = self.poller.parameter_value(MI_LIGHT)
        d['conductivity'] = self.poller.parameter_value(MI_CONDUCTIVITY)
        d['battery'] = self.poller.parameter_value(MI_BATTERY)
        return json.dumps(d)

    @staticmethod
    def get_sensor_data(sensor_data):
        p = SensorData(temperature=sensor_data['temperature'], moisture=sensor_data['moisture'],
                       fertility=sensor_data['conductivity'])
        return p

    @staticmethod
    def persist(entity):
        persist(entity)


if __name__ == '__main__':
    # sensor = MiFloraSensor()
    # sensor_data = json.loads(sensor.get_miflora_data())
    print(test_data)
    data = MiFloraSensor.get_sensor_data(test_data)
    print(data)
    MiFloraSensor.persist(data)

    p = Protocol()
    p.water = 1
    MiFloraSensor.persist(p)
