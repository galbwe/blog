import logging

import re


class FibonacciFilter(logging.Filter):
    """
    Contrived example of a filter that only returns logging messages for calls to fibonacci for even n.
    """
    def filter(self, record: logging.LogRecord) -> bool:
        n: int = self._get_fibonacci_input(record)
        return self._is_even(n)

    def _get_fibonacci_input(self, record: logging.LogRecord) -> int:
        """
        Parse message from a LogRecord with a regex to extract the integer fibonacci was called with.
        """
        message = record.getMessage()
        return _get_int_from_message(message)

    def _is_even(self, n: int) -> bool:
        return n % 2 == 0


def _get_int_from_message(message: str):
    n = re.search(r"fibonacci\((\d+)\)", message).group(1)
    return int(n)
