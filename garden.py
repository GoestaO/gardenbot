import RPi.GPIO as GPIO
import time
import sys


class Gardenbot:
    def __init__(self, moisture_sensor_channel=14, relay_channel_ventile=17, relay_channel_sensor=18, watering_time=10):
        GPIO.setmode(GPIO.BCM)
        self.moisture_sensor_channel = moisture_sensor_channel
        self.relay_channel_ventile = relay_channel_ventile
        self.relay_channel_sensor = relay_channel_sensor
        self.watering_time = watering_time

    def setup_pins(self):
        GPIO.setup(self.moisture_sensor_channel, GPIO.IN)
        GPIO.setup(self.relay_channel_ventile, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.relay_channel_sensor, GPIO.OUT, initial=GPIO.HIGH)

    '''
    This function measures the moisture of the soil. If it is too dry, the ventile will be opened, otherwise nothing will happen
    '''
    def measure_moisture(self, channel):
        self.start_sensor()

        # wait a bit
        time.sleep(1)
        if Gardenbot.soil_is_dry(channel):
            self.water_plants()
        else:
            Gardenbot.close_water()
            print 'No need to water, exit!'
            Gardenbot.stop_sensor()
            self.close()

    @staticmethod
    def relay_close_circuit(channel):
        GPIO.output(channel, False)

    @staticmethod
    def relay_open_circuit(channel):
        GPIO.output(channel, True)

    #This method waters the plants
    def water_plants(self, watering_time=None):
        Gardenbot.stop_sensor()
        print 'Let us water the plants!'
        if watering_time == None:
            watering_time = self.watering_time
        Gardenbot.open_water()
        time.sleep(watering_time)
        print 'Closing the ventile!'
        Gardenbot.close_water()



    def open_water(self):
        Gardenbot.relay_close_circuit(self.relay_channel_ventile)

    def close_water(self):
        Gardenbot.relay_open_circuit(self.relay_channel_ventile)

    def start_sensor(self):
        print "starting the sensor..."
        Gardenbot.relay_close_circuit(self.relay_channel_sensor)

    def stop_sensor(self):
        Gardenbot.relay_open_circuit(self.relay_channel_sensor)

    def close(self):
        GPIO.cleanup()
        sys.exit()

    '''If the soil is wet enough, the sensor returns True, in other words: if the soil is too dry, it is false'''

    @staticmethod
    def soil_is_dry(channel):
        return GPIO.input(channel)


if __name__ == '__main__':
    gb = Gardenbot()
    gb.setup_pins()
    gb.close_water()
    gb.measure_moisture(channel=moisture_sensor_channel)
    gb.close()






