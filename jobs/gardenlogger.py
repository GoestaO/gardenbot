import logging

class Gardenlogger:
    def __init__(self, logfile):
        self.logger = logging.getLogger("Gardenlogger")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter("%(asctime)s;%(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)



