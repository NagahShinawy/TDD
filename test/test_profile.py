import pytest
from random import choice

HTTP_200_OK = 200
HTTP_201_CREATED = 201


@pytest.fixture
def users():
    return ["nagah", "john", "mohammed", "leon"]


@pytest.fixture
def user(users):
    return choice(users)


@pytest.fixture
def allowed_files_types():
    return ["png", "jpg", "jpeg"]


@pytest.fixture(scope="class")
def allowed_methods():
    return ["GET", "POST", "PUT", "PATCH"]


def test_valid_username(user, users):
    print("\nUser", user)
    print("\nUsers", users)
    assert user in users


def test_valid_file_extension(allowed_files_types):
    # run "allowed_files_types" before "test_valid_file_extension" because "allowed_files_types" is fixture
    assert "png" in allowed_files_types
    assert "jpg" in allowed_files_types
    assert "jpeg" in allowed_files_types


class TestProfile:
    def test_create_profile(self, allowed_methods):
        assert "POST" in allowed_methods
        assert 201 == HTTP_201_CREATED

    def test_get_profile(self, allowed_methods):
        assert "GET" in allowed_methods
        assert 200 == HTTP_200_OK

    def test_update_profile(self, allowed_methods):
        assert "PUT" in allowed_methods

    def test_partial_update(self, allowed_methods):
        assert "PATCH" in allowed_methods
