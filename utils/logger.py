import logging

def get_logger():
    logger = logging.getLogger('playwright_logger')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('playwright.log')
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)

    return logger