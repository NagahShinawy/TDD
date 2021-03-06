from pytest import approx, raises


def test_int():
    assert 1 == 1


def test_float():
    assert 1.4 == 1.4
    # approx(0.3)  = 0.3 ± 3.0e-07 = 0.30000000000000004
    assert 0.1 + 0.2 == approx(0.3)  # without approx 0.30000000000000004 != 0.3


def test_str():
    assert "1" == "1"


def test_list():
    assert [1, 2, 3] == [1, 2, 3]


def test_dict():
    assert {"1": 1} == {"1": 1}


def raises_key_exception():
    # return dict()['test']
    raise KeyError


def raises_value_exception():
    # return dict()['test']
    raise ValueError


def test_exception():
    # do test on KeyError. is key noy found , the test will be passed, because you add "KeyError"
    with raises(KeyError):
        raises_key_exception()

    with raises(ValueError):
        raises_value_exception()
