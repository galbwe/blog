import os


def load_environment_variable(variable_name: str):
    try:
        return os.environ[variable_name]
    except KeyError:
        raise EnvironmentError(
            f'Could not load environment variable "{variable_name}", you may need to source your .env file.'
        )
