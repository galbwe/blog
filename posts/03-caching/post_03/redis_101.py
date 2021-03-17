import redis

from .environment import read_environment_variables


REDIS_HOST, REDIS_PORT, REDIS_DB = read_environment_variables('REDIS_HOST', 'REDIS_PORT', 'REDIS_DB')
REDIS_PORT = int(REDIS_PORT)
REDIS_DB = int(REDIS_DB)


def redis_client(**params):
    return redis.Redis(**params)


def set_test_data(redis):
    redis.set('test:str', 'value')


def read_test_data(redis):
    b = redis.get('test:str')
    s = str(b)
    print('test:str ', s)


if __name__ == '__main__':
    r = redis_client(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    set_test_data(r)
    read_test_data(r)