import os
from typing import List, Tuple


def read_environment_variable(variable: str) -> str:
    """
    Reads the value of an environment variable.
    """
    try:
        return os.environ[variable]
    except KeyError:
        raise EnvironmentError(f"Could not read environment variable {variable}. Did you source your .env file?")


def read_environment_variables(*variables: List[str]) -> Tuple[str]:
    """
    Reads the values of a list of environment variables.
    """
    return tuple(read_environment_variable(v) for v in variables)
