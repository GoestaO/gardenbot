from views import *
import connexion
from app import app, db
import models



if __name__ == "__main__":
    # app = connexion.App(__name__)
    # app.add_api('api/endpoints/gardenbot-api.yaml')

    app.run(debug=True, host='0.0.0.0', port=8080)