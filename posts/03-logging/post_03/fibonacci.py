import logging
import sys
from functools import lru_cache

from .dict_config import set_logging_config
from .python_config import get_logger


set_logging_config()


logger = logging.getLogger(__name__)
# logger = get_logger(__name__)


@lru_cache()
def fibonacci(n):
    """
    Computes the nth fibonacci number.

    Fibonnaci numbers are defined by the recursive formula
    fibonacci(0) = 1, fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2), n ≥ 2
    """
    logger.info("Computing fibonacci(%s).", n)
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))