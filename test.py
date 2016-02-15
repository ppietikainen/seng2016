import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)

    def test_fizz(self):
        app = FizzBuzz()
        test_fizz = [3, 6, 9, 12, 18, 21, 24]
        # Run test
        for value in test_fizz:
            self.failIf(app.calc(value) != "Fizz")

    def test_buzz(self):
        app = FizzBuzz()
        test_buzz = [5, 10, 20, 35, 40, 50, 55]
        for value in test_buzz:
            self.failIf(app.calc(value) != "Buzz")

    def test_fizzbuzz(self):
        app = FizzBuzz()
        test_fizzbuzz = [15, 30, 45, 60, 75, 90]
        for value in test_fizzbuzz:
            self.failIf(app.calc(value) != "FizzBuzz")

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)
        
        # Test if there are 100 lines in output
        self.failIf(len(output.getvalue().splitlines()) == 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
