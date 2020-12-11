# TODO (list of numpy array)
from numpy import *

""" * represents the whole functions of numpy
   importing * means that you are importing
   all the functions of numpy """


# TODO (creating a 1d array)
def array1d():
    arr = array(['B', 'A', 'C', 'E', 'D'], dtype=str)
    _ = sorted(arr, reverse=False)
    "['A', 'B', 'C', 'D', 'E']"
    """ This kind of array is a 'str', we can use strings in
    numpy. """
    arr1 = array([90, 87, 1, 3, 54, 43], dtype='i')
    arr1 = sorted(arr1, reverse=False)
    "[1, 3, 43, 54, 87, 90]"
    print(arr1)
    """ This kind of array is an 'int', we can use integers in
        numpy as well as float """

    """ In dealing with int array there are specific mathematical
        commands you can use which are:
        sort()
        max()
        min()
        log()
        sin()
        cos()
        sum() """

    """ variable = sorted(variable, reverse=boolean) this variable
        can be use to manipulate the array list, whether you want
        to print it in reversed format or not using the boolean signs """


# TODO (creating a 2D array)
def array2d():
    arr2 = array([[10, 19, 90, 123], [124, 155, 166, 187], [90, 21, 21, 32]])
    print(f'{arr2.reshape(-1)}')


# TODO (creating a 3D array)
def array3d():
    arr3 = arange(start=0, stop=100, step=1, dtype=int)
    """ arange can be used to present a list of numerical ranges
        with index value, unlike range, numbers in arange
        are represented as an array List """

    arr4 = arr3.reshape(10, 2, 5)
    """ This represents the formatted version of the arange above
        the first number presents as number of arrays, the second
        number presents as number of columns per mentioned array
        and the last is the number of rows per column """

    # Unknown Dimension
    arr4 = arr3.reshape(10, 2, -1)
    """ the usage of negative number in columns or rows represents
        the unknown dimension which means that if a negative value is
        assigned, python will automatically find the best shape for you
        NOTE: you can only have one(1) unknown dimension per shape """

    print(arr4)
    """ [[[ 0  1  2  3  4]
        [ 5  6  7  8  9]]

     [[10 11 12 13 14]
      [15 16 17 18 19]]

     [[20 21 22 23 24]
      [25 26 27 28 29]]

     [[30 31 32 33 34]
      [35 36 37 38 39]]

     [[40 41 42 43 44]
      [45 46 47 48 49]]] """

    """ NOTE: In adding a multidimensional array you can use
        vstack(array names) for by column stacking and 
        hstack(array names) for one row stacking """


# TODO (Copying an array List)
def array_copying():
    arr5 = array([90, 87, 32, 21, 54, 76, 32], dtype=int)
    arr6 = arr5
    """ giving a value to an empty array is the same as calling
        .view(). i.e, arr6 = arr5.view()"""
    arr5[0] += 10
    """ The given code above is another way of copying an array
        list called as shallow copy, which means that the two arrays
        have same address, if one of the arrays have been manipulated, 
        the same manipulation will happen on the another array.
         Except for: sin(), cos() and, log()."""

    print(arr5, arr6)
    print(id(arr5))
    print(id(arr6))

    print()

    arr7 = ([90, 87, 32, 21, 54, 76, 32])
    arr8 = arr7.copy()
    arr7[0] += 10
    """ The given code above is another way of copying an array
    list called as deep copy, which means that the two arrays
    have different address, if one of the arrays is manipulated,
    the other array wont be affected since they are only copying
    the list inside before the manipulation."""

    print(arr7, arr8)
    print(id(arr7))
    print(id(arr8))


#  TODO (Array searching)
def array_searching():
    arr9 = array([2, 1, 5, 3, 4], dtype=int)
    search1 = sorted(arr9, reverse=False)
    search = searchsorted(search1, 2, side='left')
    """ In terms of array searching you can use
        searchsorted() to find the index value 
        of the numbers in the array, but the array must
        be SORTED"""
    print(search)


#  TODO (Multiplying Array Matrices)
def matrix_ex():
    m = matrix('1, 2, 3;, 4, 5, 6; 7, 8, 9')
    m1 = m.copy()

    print(m)
    print()
    print(m1)
    print()
    print((m * m1))


# TODO (Rounding Decimals inside an Array)
def array_rounding():
    array1 = array([-1, -2.333, -91.00001, -8.93, 71.88], dtype='f')

    print("This is the truncated array:", trunc(array1))
    """ trunc() is a type of function that iterates the following
        elements inside an array and removes the numbers under 
        the decimals same as fix() """

    print("This is the rounded array:", around(array1, 2))
    """ around() is a type of function that iterates the elements
        inside an array and rounds it, around() takes two arguments
        the first is the array_name and second is the number of decimals
        to be placed """

    print("This is the floored array:", floor(array1))
    """ floor() is a type of function that iterates the
        elements inside an array and converts is into its flat
        value regardless of the decimal values """

    print("This is the ceiled array:", ceil(array1))
    """ The ceil() function rounds off decimal to nearest upper integer."""


# TODO (Finding LCM & GCD)
def find_LCM():
    num1 = int(eval(input("Enter  the first number:")))
    num2 = int(eval(input("Enter  the second number:")))
    print(f'The least common multiple of {num1} and {num2} is: {lcm(num1, num2)}')
    """ In arithmetic and number theory, the least common multiple, lowest common multiple, 
    or smallest common multiple of two integers a and b, usually denoted by lcm, 
    is the smallest positive integer that is divisible by both a and b. """


def find_GCD():
    num1 = int(eval(input("Enter  the first number:")))
    num2 = int(eval(input("Enter  the second number:")))
    print(f'The greatest common denominator of {num1} and {num2} is: {gcd(num1, num2)}')
    """ The greatest common divisor of two integers, 
    also known as GCD, is the greatest positive 
    integer that divides the two integers."""



