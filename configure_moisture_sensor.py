from garden import Gardenbot

if __name__ == "__main__":
    gb = Gardenbot()
    gb.setup_pins()
    gb.start_sensor()

    soil_is_dry = Gardenbot.soil_is_dry(14)
    gb.stop_sensor()
    print("Soil is dry: {}".format(soil_is_dry))
    gb.close()
