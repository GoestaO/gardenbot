from garden import Gardenbot

if __name__ == "__main__":
    gb = Gardenbot()
    gb.setup_pins()
    soil_is_dry = Gardenbot.soil_is_dry(14)
    print("Soil is dry: {}".format(soil_is_dry))
    gb.close()
