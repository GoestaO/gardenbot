import os, sys
CURRENT_WORK_DIR = os.getcwd()
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_WORK_DIR, os.pardir))

sys.path.append(CURRENT_WORK_DIR)
sys.path.append(APPLICATION_DIR)
from main import db

if __name__ == '__main__':
    db.create_all()