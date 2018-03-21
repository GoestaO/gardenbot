import connexion
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__name__))
sys.path.extend(dir_path)

app = connexion.App(__name__)
app.add_api('swagger/gardenbot-api.yaml')


if __name__ == "__main__":
    app.run()
