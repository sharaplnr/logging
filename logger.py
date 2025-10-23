import logging

date_format = "%H:%M:%S"

class CustomFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\033[34m",  # синий
        logging.INFO: "\033[37m",  # белый
        logging.WARNING: "\033[33m",  # жёлтый
        logging.ERROR: "\033[31m",  # красный
        logging.CRITICAL: "\033[31m",  # красный
    }

    RESET = "\033[0m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"

    def format(self, record):
        color = self.COLORS.get(record.levelno, self.RESET)

        log_fmt = (
            f"{self.GREEN}%(asctime)s{self.RESET} - "
            f"{self.CYAN}%(name)s{self.RESET} - "
            f"{color}%(levelname)s - %(message)s{self.RESET}"
        )

        formatter = logging.Formatter(log_fmt, datefmt=date_format)

        return formatter.format(record)


# Фабрика
def get_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Получение именованного логгера с консольным handler'ом
    Безопасно для многократного вызова - не дублирует handler'ы за счет проверки существования у логгера консольного обработчика

    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        handler = logging.StreamHandler()
        handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


if __name__ == "__main__":

    logger = logging.getLogger("example")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(CustomFormatter())
    logger.addHandler(handler)

    logger.debug("Debug сообщение")
    logger.info("Info сообщение")
    logger.warning("Warning сообщение")
    logger.error("Error сообщение")
    logger.critical("Critical сообщение")