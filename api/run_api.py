import connexion
import sys, os

dir_path = os.path.dirname(os.path.realpath(__name__))
sys.path.extend(dir_path)




if __name__ == "__main__":
    app = connexion.App(__name__)
    app.add_api('swagger/gardenbot-api.yaml')
    app.run()
