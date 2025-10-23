import logging

logger = logging.getLogger(__name__)

def test_example():
    logger.info("Тестовое сообщение")
    logger.debug("Детальная информация")
    logger.warning("Oops!")