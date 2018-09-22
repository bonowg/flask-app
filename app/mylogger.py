import logging
import datetime
import sys


class Logger(object):
    def __init__(self, filename):
        self.logger = logging.getLogger()
        self.logFormatter = logging.Formatter("%(asctime)s [%(name)s] [%(module)s] [%(levelname)s]  %(message)s")

        # self.filehandler = logging.FileHandler("{1}-{0}".format(filename, datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")))
        # self.filehandler.setFormatter(self.logFormatter)

        self.consolejhandler = logging.StreamHandler()
        self.consolejhandler.setFormatter(self.logFormatter)

        # self.logger.addHandler(self.filehandler)
        self.logger.addHandler(self.consolejhandler)

        self.logger.setLevel(logging.DEBUG)

    def debug(self, message="---"):
        self.logger.debug(message)

    def info(self, message="---"):
        self.logger.info(message)

    def warning(self, message="---"):
        self.logger.warning(message)

    def error(self, message="---"):
        self.logger.error(message)

    def critical(self, message="---"):
        self.logger.critical(message)


if __name__ == '__main__':
    sys.exit()
