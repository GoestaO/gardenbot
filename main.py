from views import *
import connexion
from app import app



if __name__ == "__main__":
    # app = connexion.App(__name__)
    # app.add_api('api/endpoints/gardenbot-api.yaml')

    app.run(debug=True, port=8080)