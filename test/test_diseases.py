import pytest
#
#
# @pytest.fixture
# def setup():
#     print("\nSetup1")
#     yield
#     print("\nTeardown1")
#
#
# @pytest.fixture
# def setup2(request):
#     print("\nSetup2")
#
#     def teardown_a():
#         print("\nA")
#
#     def teardown_b():
#         print("\nB")
#     # request:  <SubRequest 'setup2' for <Function test2>>
#     request.addfinalizer(teardown_a)  # runs after test
#     request.addfinalizer(teardown_b)  # runs after test


@pytest.fixture(params=[1, 3, 6])
def setup(request):
    value = request.param
    print("\nCurrent", value)
    return value


def test1(setup):
    print("Set up", setup)
    assert True
