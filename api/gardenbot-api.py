#from moisture import Gardenbot
import time
import connexion


def water_plants(seconds):
    print("Waiting now...")
    watering_time = int(seconds)
    time.sleep(watering_time)
    #super(GardenbotAPI, self).water_plants(watering_time)
    print("Exit")

if __name__ == "__main__":
    app = connexion.App(__name__)
    app.add_api('swagger/gardenbot-api.yaml')
    app.run(port=8080)

