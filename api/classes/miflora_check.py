from miflora.miflora_poller import MiFloraPoller
from miflora.backends.gatttool import GatttoolBackend
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import json


def get_miflora_data(poller):
    d =  dict()
    d['firmware'] = poller.firmware_version()
    d['name'] = poller.name()
    d['temperature'] = poller.parameter_value(MI_TEMPERATURE)
    d['moisture'] = poller.parameter_value(MI_MOISTURE)
    d['light'] = poller.parameter_value(MI_LIGHT)
    d['conductivity'] = poller.parameter_value(MI_CONDUCTIVITY)
    d['battery'] = poller.parameter_value(MI_BATTERY)
    return json.dumps(d)

if __name__== '__main__':
    poller = MiFloraPoller('C4:7C:8D:65:B5:CF', GatttoolBackend)
    dump = get_miflora_data(poller=poller)
    print(dump)


# from gattlib import GATTRequester, GATTResponse
# from struct import *
#
# address = "DE:AD:BE:EF:CA:FE"
# requester = GATTRequester(address)
# #Read battery and firmware version attribute
# data=requester.read_by_handle(0x0038)[0]
# battery, version = unpack('<B6s',data)
# print "Battery level:",battery,"%"
# print "Firmware version:",version
# #Enable real-time data reading
# requester.write_by_handle(0x0033, str(bytearray([0xa0, 0x1f])))
# #Read plant data
# data=requester.read_by_handle(0x0035)[0]
# temperature, sunlight, moisture, fertility = unpack('<hxIBHxxxxxx',data)
# print "Light intensity:",sunlight,"lux"
# print "Temperature:",temperature/10.,"°C"
# print "Soil moisture:",moisture,"%"
# print "Soil fertility:",fertility,"uS/cm"
