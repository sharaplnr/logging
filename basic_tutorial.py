import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8', filemode='w', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
logger.debug("debug 1")
logger.info("info")
logger.warning("warning")
logger.error("error")

if __name__ == '__main__':
    pass