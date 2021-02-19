import unittest
import app


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        self.assertEqual(app.fibonacci(1), 1)

    def test_fibonacci_10(self):
        self.assertEqual(app.fibonacci(10), 89)

    def test_fibonacci_30(self):
        self.assertEqual(app.fibonacci(30), 1346269)


class TestFactorial(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(app.factorial(0), 1)

    def test_factorial_5(self):
        self.assertEqual(app.factorial(5), 120)


# if __name__ == '__main__':
#     unittest.main()