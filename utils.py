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


def check_blood_type(blood_type):
    blood_types = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
    assert blood_type in blood_types, "Blood types should one of {}".format(
        ",".join(blood_types)
    )
