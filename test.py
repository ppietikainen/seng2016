import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(3) != "3 is a prime")

    def test_known_primes(self):
        # Test program output with known prime numbers as arguments
        app = FizzBuzz()
        # A list of known prime numbers
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 27]
        for i in primes:
            self.failIf(app.calc(i) != str(i) + " is a prime")
        
    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)
        
        # Test if there are 100 lines in output
        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
