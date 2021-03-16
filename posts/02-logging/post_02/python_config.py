import logging
import logging.handlers


def get_logger(module_name) -> logging.Logger:
    # loggers
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    rotating_file_handler = logging.handlers.RotatingFileHandler(
        'loggymclogface.log',
        maxBytes=1024,
        backupCount=3,
    )
    rotating_file_handler.setLevel(logging.INFO)

    # formatters
    simple_formater = logging.Formatter('%(levelname)s: %(message)s')
    timestamped_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatters to handlers
    stream_handler.setFormatter(simple_formater)
    rotating_file_handler.setFormatter(timestamped_formatter)

    # add handlers to logger
    logger.addHandler(stream_handler)
    logger.addHandler(rotating_file_handler)

    return logger