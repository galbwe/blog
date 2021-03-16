import logging.config

import pytest
from pytest_mock import mocker

import post_03.dict_config as dict_config
from post_03.dict_config import parse_yaml, set_logging_config


@pytest.fixture
def yaml_file_contents():
    return """
        key_1: value_1
        key_2:
            nested_key_1: nested_value_1
            nested_key_2: nested_value_2
        int_key: 42
        list_key:
            - 1
            - 2
            - 3
            - hello
        filter:
            (): module_name
    """


@pytest.fixture
def config_dict():
    return {
        "key_1": "value_1",
        "key_2": {
            "nested_key_1": "nested_value_1",
            "nested_key_2": "nested_value_2",
        },
        "int_key": 42,
        "list_key": [1, 2, 3, "hello"],
        "filter": {
            "()": "module_name",
        },
    }


def test_parse_yaml(yaml_file_contents, config_dict):
    assert parse_yaml(yaml_file_contents) == config_dict


def test_set_logging_config(config_dict, mocker):
    mock_parse_yaml = mocker.patch.object(dict_config, "parse_yaml")
    mock_parse_yaml.return_value = config_dict

    mock_dict_config = mocker.patch.object(logging.config, "dictConfig")

    set_logging_config()

    mock_parse_yaml.assert_called_once()
    mock_dict_config.assert_called_once_with(config_dict)