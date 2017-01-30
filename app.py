import connexion
import os
from flask import Flask, Session
from configuration import Configuration

app = connexion.App(__name__)
app.add_api('api/endpoints/gardenbot-api.yaml')
app.app.config.from_object(Configuration)






if __name__ == "__main__":
    app = connexion.App(__name__)
    app.add_api('endpoints/gardenbot-api.yaml')
    app.run(port=8080)
