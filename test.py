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
        self.failIf(app.calc(6) != "Fizz")

    def test_buzz(self):
        app = FizzBuzz()
        self.failIf(app.calc(10) != "Buzz")

    def test_fizzbuzz(self):
        app = FizzBuzz()
        self.failIf(app.calc(15) != "FizzBuzz")
    
    def test_prime(self):
        app = FizzBuzz()
        primes = [2, 7, 13, 17, 19, 23, 29, 31, 37]
        for p in primes:
            self.failIf('prime' not in app.calc(p) )

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
