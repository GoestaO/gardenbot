import connexion
import sys
import os

dirname = os.path.dirname(os.path.realpath(__name__))
APPLICATION_ROOT = os.path.join(dirname, os.pardir)
sys.path.extend(dirname)
sys.path.extend('..')
app = connexion.App(__name__)
app.add_api('swagger/gardenbot-api.yaml')

if __name__ == "__main__":
    app.run()
