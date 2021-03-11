from pytest_mock import mocker

import post_03.basic_logging as basic_logging


def test_example_01(mocker):
    mock_warning = mocker.patch.object(basic_logging.logging, "warning")
    mock_info = mocker.patch.object(basic_logging.logging, "info")

    basic_logging.example_01()

    mock_warning.assert_called()
    mock_info.assert_called()
    assert False