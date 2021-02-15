from utils import fizzbuzz, check_fizzbuzz


def test_assert_true():
    assert True


def test_string_len():
    assert len("1") == 1


# Todo : remove it at refactor phase
# def test_can_call_fizzbuzz():
#     fizzbuzz(1)


def test_returns_1_with_1_passed():
    check_fizzbuzz(1, "1")


def test_returns_2_with_2_passed():
    check_fizzbuzz(2, "2")


def test_returns_fizz_with_3_passed():
    check_fizzbuzz(3, "Fizz")
    check_fizzbuzz(6, "Fizz")
    check_fizzbuzz(9, "Fizz")
    check_fizzbuzz(12, "Fizz")
    check_fizzbuzz(18, "Fizz")


def test_returns_buzz_with_5_passed():
    check_fizzbuzz(5, "Buzz")
    check_fizzbuzz(25, "Buzz")
    check_fizzbuzz(20, "Buzz")
    check_fizzbuzz(35, "Buzz")


def test_returns_fizzbuzz_with_multiple3_or_5_passed():
    check_fizzbuzz(30, "FizzBuzz")
    check_fizzbuzz(15, "FizzBuzz")
    check_fizzbuzz(45, "FizzBuzz")
    check_fizzbuzz(90, "FizzBuzz")


def test_assert():
    assert True