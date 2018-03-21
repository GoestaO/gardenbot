import logging

class Gardenlogger:
    def __init__(self, logfile, loglevel=logging.INFO):
        self.logger = logging.getLogger("Gardenlogger")
        self.logger.setLevel(loglevel)
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter("%(asctime)s;%(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)



