from .line_reader import read_file
import pytest
import os
import pathlib
from unittest.mock import MagicMock


base_dir = pathlib.Path(__file__).parent.absolute()  # current dir of running script
file_dir = os.path.join(base_dir, "info.txt")


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_return_correct_string(mock_open, monkeypatch):
    mock_exist = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exist)
    result = read_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_throws_exception_with_badfile(mock_open,
                                       monkeypatch):
    mock_exist = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exist)
    with pytest.raises(Exception):
        result = read_file("blah")