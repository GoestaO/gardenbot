from miflora.backends.gatttool import GatttoolBackend
from miflora.miflora_poller import MiFloraPoller, MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import json


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

if __name__ == '__main__':
    sensor = MiFloraSensor()
    print(sensor.get_miflora_data())