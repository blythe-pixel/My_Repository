# TODO (Defining a function)
from numpy import *
import array


# TODO (A simple Function)
def simple_func():
    print("This is an example of function without parameters")

    """ This is a simple functions without parameters and
        arguments """


# TODO (Function with Default Parameter)
def para_func(Name="Kristian Roger M. Agdeppa", Course="B.S Data Science"):
    print(Name)
    print(Course)

    """ This is a function with default parameters and arguments; the 
    arguments are defined inside the parameter thus, no declaration of positional
    argument is needed """


# TODO (Positioning an Argument into Parameters)
def position(street, city):
    print("Street:", street)
    print("City:", city)


# position(city="Cagayan de Oro", street="Kauswagan Blvd.")


# TODO (Function with Various Arguments)
def multi_args(num1, *num2):
    sum = num1
    for vals in num2:
        sum = sum + vals
    print("Sum:", sum)
    return sum


# TODO (Keyworded Argument)
def pax_info(name, **data):
    print(name)
    print(data.items())


# pax_info("Roger", surname="Agdeppa", age=18)

# TODO __init__ (EXAMPLE 1)
try:
    class specs():

        def __init__(self, cpu, ram, gpu):
            self.cpu = cpu
            self.ram = ram
            self.gpu = gpu

        def com1_cpu(self):
            print("The cpu of spec1 is: ", self.cpu)

        def com1_ram(self):
            print("The ram of spec2 is", self.ram)

        def com1_gpu(self):
            print("The gpu of spec3 is:", self.gpu)


    spec1 = specs('Core i5', 16, 'rtx 3080')
    spec2 = specs('Ryzen 5', 12, 'gtx 2020')
    spec3 = specs('Core i9', 16, 'rtx 3080')

    spec1.com1_cpu()
    spec2.com1_ram()
    spec3.com1_gpu()
except BaseException:
    pass


# TODO __init__ (EXAMPLE 2)
try:
    class cryptocurrency():

        def __init__(self, crypto, val):
            self.crypto = crypto
            self.val = val


    BTC = cryptocurrency("Bitcoin", "554K")
    XRP = cryptocurrency("XRP/PHP", 12.541)

    print(BTC.crypto, BTC.val)
    print(XRP.crypto, XRP.val)

except BaseException:
    pass

# TODO BASIC EXCEPTION HANDLING
try:
    import sys
    import inspect
    sys.setrecursionlimit(20)
    x = 1000/0
    print(x)
except ZeroDivisionError:
    print("Undefined")

""" Basic example of try and except but using a ZeroDivisionError """
print()
try:
    class odd_even():

        @staticmethod
        def anony_func():
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
                print(f'You Have up 10 tries')
                print(f'Number of tries:{len(inspect.stack())}')
                odd_even.invalid(self)


    number = odd_even()

    print(number.anony_func(), number.invalid())

except RecursionError:
    print("The maximum number of tries has been reached")

finally:
    print("Thank you using the program!")

""" This is an example of try & except using RecursionError """

""" In exception handling you can specify what type of Error that has to be prioritize
    and these are the exception handling you can use:
    1. IndexError is thrown when trying to access an item at an invalid index.
    2. ModuleNotFoundError is thrown when a module could not be found.
    3. KeyError is thrown when a key is not found.
    4. ImportError is thrown when a specified function can not be found.
    5. StopIteration is thrown when the next() function goes beyond the iterator items
    6. TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
    7. ValueError is thrown when a function's argument is of an inappropriate type.
    8. NameError is thrown when an object could not be found.
    9. ZeroDivisionError is thrown when the second operator in the division is zero.
    10. KeyboardInterrupt is thrown when the user hits the interrupt key (normally Control-C)
        during the execution of the program. """

