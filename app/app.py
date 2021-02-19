def fibonacci(number):
    if number <= 1:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


fibonacci(1)
fibonacci(10)
factorial(0)
factorial(2)
