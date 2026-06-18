import logging


LOGS_FILE = "logs/app.log"


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        filename=LOGS_FILE,
        format="%(asctime)s | %(levelname)s | %(message)s")
    return logging.getLogger()