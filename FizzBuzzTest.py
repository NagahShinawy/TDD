from utils import fizzbuzz


def test_assert_true():
    assert True


def test_string_len():
    assert len("1") == 1


# Todo : remove it at refactor phase
# def test_can_call_fizzbuzz():
#     fizzbuzz(1)


def test_returns_1_with_1_passed():
    number = fizzbuzz(1)
    assert number == "1"


def test_returns_2_with_2_passed():
    number = fizzbuzz(2)
    assert number == "2"
