from views import *
from app import app as application, db
import models
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__name__))
sys.path.extend(dir_path)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
