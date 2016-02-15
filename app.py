#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    def fizzBuzzTester(self, number):
        if (number % 3 == 0) and (number % 5 == 0):
            toPrint = 'FizzBuzz'
        elif (number % 3 == 0):
            toPrint = 'Fizz'
        elif (number % 5 == 0):
            toPrint = 'Buzz'
        else:
            toPrint = number
        return toPrint
		
    def run(self, end, out=sys.stdout):
        for i in range(1, end):
			
            print >> out, self.calc(i)

    def calc(self, i):
        return self.fizzBuzzTester(i)

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
