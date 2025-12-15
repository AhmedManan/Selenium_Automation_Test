import logging

class LogMaker:

    @staticmethod
    def generate_log():
        logging.basicConfig(filename='.\\logs\\demoblaze.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger