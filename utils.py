def is_multiple(value, mod):
    return (value % mod) == 0


def fizzbuzz(value):
    if is_multiple(value, 3) and is_multiple(value, 5):
        return "FizzBuzz"
    if is_multiple(value, 3):
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def check_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected, f"{value} != {expected}"
