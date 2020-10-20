# TODO (Creating an Anonymous Function)
from numpy import *
import sys

""" lambdas are basically anonymous function,
    you can create a one-time function, with
    one time use."""

f = lambda a, b: a + b
print(f(12, 0))


# TODO (Applying an Anonymous Function)

class odd_even():

    def anony_func(self):
        nums = eval(input('Enter the number:'))
        global Even, Odd
        print(nums)
        Even = list(filter(lambda nums: nums % 2 == 0, nums))
        Odd = list(filter(lambda nums: nums % 2 == 1, nums))

    def invalid(self):
        data = str(input("Odd or Even? "))

        if data.lower() == "even":
            print(f'Even in the list:{list(Even)}')

        elif data.lower() == "odd":
            print(f'Odds in the list:{list(Odd)}')

        else:
            print("Invalid Input, Try Again")
            sys.setrecursionlimit(100)

            odd_even.invalid(self)


number = odd_even()

print(number.anony_func(), number.invalid())
