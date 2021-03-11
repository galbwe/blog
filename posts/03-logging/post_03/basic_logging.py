import logging
import itertools
import time
import random

from .another_module import do_something

def example_01():
    logging.warning('I am a warning!')
    logging.info('I am informative!')


def logging_to_a_file(filename='example-02.log', level=logging.DEBUG, filemode='w'):
    logging.basicConfig(filename=filename, level=level, filemode=filemode)
    logging.debug('I help squash bugs! MUUUUUUUURDER!')
    logging.info("I am so informative!")
    logging.warning("YOU HAVE BEEN WARNED!")
    logging.error('Something is seriously wrong.')


def logging_with_multiple_modules():
    logging.basicConfig(filename='example-03.log', level=logging.DEBUG, filemode='w')
    logging.info("Started")
    do_something()
    logging.info("Ended")


def set_up_logging(*args, **kwargs):
    def decorator(f):
        called = False
        def inner(*iargs, **ikwargs):
            nonlocal called
            if not called:
                called = True
                logging.basicConfig(*args, **kwargs)
            return f(*iargs, **ikwargs)
        return inner
    return decorator


@set_up_logging(filename='example-04.log', level=logging.DEBUG, filemode='w')
def log_some_data(x):
    logging.info('"log_some_data" was called with x=%s', x)


@set_up_logging(format='%(asctime)s %(levelname)s:%(message)s', filename='example=05.log', level=logging.DEBUG, filemode='w')
def log_date_and_time(x):
    logging.info('"log_date_and_time" was called with x=%s', x)


if __name__ == '__main__':
    # logging_to_a_file(level=logging.WARNING)
    # logging_with_multiple_modules()
    for x in itertools.chain('abcdefg', range(4)):
        time.sleep(5 * random.random())
        log_date_and_time(x)