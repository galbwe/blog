import logging.config
import os
from typing import Dict, Iterable

import yaml


from .config import load_environment_variable


YAML_LOGGING_CONFIG = load_environment_variable("YAML_LOGGING_CONFIG")


def parse_yaml(stream: Iterable) -> Dict:
    try:
        loader = yaml.CLoader
    except ImportError:
        loader = yaml.Loader
    return yaml.load(stream, loader)


def set_logging_config(config_file=YAML_LOGGING_CONFIG):
    with open(config_file, "r") as f:
        config = parse_yaml(f.read())
    logging.config.dictConfig(config)


if __name__ == "__main__":
    set_logging_config()
    logger = logging.getLogger("dictionary-config")
    for _ in range(10000):
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
