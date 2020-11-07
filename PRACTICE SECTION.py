# TODO FIND A MAXIMUM VALUE
# x = int(input('enter first number:'))
# y = int(input('enter second number:'))

# z = int(input('enter third number:'))


# num = [x,y,z]

# print(max(num))

# TODO IDENTIFY IF THE VALUE IS POSITIVE OR NEGATIVE
# a = float(input("Enter a Number:"))

# if a > 0:
#     print("Positive")
# else:
#     print("Negative")

# TODO FORMATTED LARGE NUMBER
# num = 100000000000
# num1 = 100000000000

# sum = num1 + num

# print(f'{sum:,}')

# TODO ADD USER-BASED NUMBERS USING FOR LOOP
# for i in range(3):
#     num = eval(input('Enter a number: '))
#     num1 = num+num+num
# print ('The square of your number is', f'{num1:,}')
# print('The loop is now done.')

# TODO FINDING SQUARE ROOT BASED ON RANGE
# import math as s
# for i in range(1, 500):
#     a = s.sqrt(i)
#     if i % a == 0:
#         print(i, end=' ')

# TODO FIBONACCI SEQUENCE W/ USER INPUT
# list1 = [0, 1]
# user = int(input("Enter Number:"))
# for i in range(user):
#     list1.append(list1[-1]+list1[-2])
# print(list1)

# TODO FINDING PRIME NUMBER BASED ON USER INPUT
# num = eval(input("Input:"))
# for i in range(2, num):
#     if num % i == 0:
#         print("Not Prime")
#         break
#     else:
#         print("Prime")
#         break

# TODO PRINTING PATTERNS
# a = '*'
# print("Pattern 1")
# for i in range(10, 0, -1):
#     print(a*i)
# print("Pattern 2")
# for e in range(0, 10, 1):
#     print(a*e)
# n = 9
# print("Pattern 3")
# for a1 in range(1, (n+1)//2 + 1):
#     for a2 in range((n+1)//2 - a1):
#         print(" ", end="")
#     for a3 in range((a1*2)-1):
#         print("*", end="")
#     print()
# print("Pattern 4")
# h = 5
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))

# TODO COLLIDING SETS
# set1 = {'a': 0, 'b': 1}
# set2 = {'c': 2, 'd': 3}
# set3 = {'e':4, 'f':5}
# all_set = {**set1, **set2, **set3}
# print(all_set)

# TODO COLLAPSING A MULTIDIMENSIONAL ARRAY
# import numpy as np
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#     print(x, end=" ")

# TODO DATA VISUALIZATION EXAMPLE
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# x = random.normal(loc=1, scale=10, size=(2, 3))
# sns.distplot(x, hist=True)
# plt.show()

# TODO IP ADDRESS FETCHER
# import socket
# host = socket.gethostname()
# ip = socket.gethostbyname(host)
# print(host)
# print(ip)

# TODO IMPORTING A SELF-MADE MODULE W/ SPACES
# Numpy = __import__("Numpy (Random)")
# Numpy.random_int()
# Numpy.data_dist()

# TODO BASIC GUI USING DEARPUGUI
# from dearpygui.core import *
# def save_callback(sender, data):
#     print("Save Clicked")
# add_text("Hello world")
# add_button("Save", callback=save_callback)
# add_input_text("string")
# add_slider_float("float")
# start_dearpygui()

# TODO BASIC GUI USING PYAUTOGUI
# import pyautogui
# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt(pyautogui.countdown(seconds=5))
# pyautogui.password('Enter password (text will be hidden)')

# TODO BASIC SHUTDOWN PROGRAM
# try:
#     import os
#     import pyautogui
#     x = str(input("Do you want this PC to shutdown? (yes/no):"))
#     if x.lower() == 'yes':
#         pyautogui.alert('Shutting Down')
#         os.system("shutdown /r /t 1")
#     elif x.lower() == "no":
#         print("cancelled")
#     else:
#         print("Error")
# except ImportError:
#     pass

# TODO CREATE HTML FILE BASED W/ GEOGRAPHICAL POSITION
# import folium
# cdo_location = [8.4542, 124.6319]
# map = folium.Map(location=cdo_location, zoom_start=15)
# map.save("mapa.html")

# TODO DATA VISUALIZATION USING PRETTYTABLE
# from prettytable import *
# x = PrettyTable()
# x.field_names = ["Student Name", "Age", "Course", "Phone Number"]
# x.add_row(["Kristian Roger M. Agdeppa", 18, "B.S Data Science", "09983424158"])
# x.add_row(["Yobel Chloe Labadan", 19, "B.S Data Science", "N/A"])
# x.add_row(["Natasha Kaye T, Agapay", 19, "B.S Data Science", "N/A"])
# x.add_row(["Maikko Nikko Banaag", 19, "B.S Data Science", "N/A"])

# """ The del_row method takes an integer index of a single row to delete.
# The del_column method takes a field name of a single column to delete.
# The clear_rows method takes no arguments and deletes all the rows in the table -
# but keeps the field names as they were so you that you can repopulate it with the same kind of data.
# The clear method takes no arguments and deletes all rows and all field names. It's not quite the same as creating a
# fresh table instance, though - style related settings, discussed later, are maintained."""

# print(x)

# TODO GENERATING FAKE INFORMATION VIA MODULE
# from faker import Faker
# from faker.providers import internet
# fake = Faker()
# fake.add_provider(internet)
# print("Fake I.P Address:", fake.ipv4_public())
# print("Fake I.P Address:", fake.ipv4_private())
# print("Fake Name:", fake.name())
# print("Fake Address:", fake.address())
# print("Fake Sentence:", fake.sentence())

# TODO __NAME__ SPECIAL PYTHON VARIABLE
# ex = __import__("Name Variable")
# ex.example()


# TODO (RECURSIVE SUMMATION)
# try:
#     class summation():
#         def example(self):
#             try:
#                 num1 = eval(input("Enter the first number:"))
#                 num2 = eval(input("Enter the second number:"))
#                 print(f'The sum of {num1} and {num2} is {num1 + num2}')
#             except BaseException:
#                 print('Error Try Again')
#                 summation.example(self)
#                 summation.example2(self)
#
#         def example2(self):
#             user = str(input("Do you still want to continue (yes/no):"))
#             if user.lower() == 'yes':
#                 summation.example(self)
#                 summation.example2(self)
#
#             elif user.lower() == 'no':
#                 print("Thank you for using my calculator")
#                 exit()
#
#             else:
#                 print("Error Try Again")
#                 self.example2()
#
# except BaseException:
#     print("Error Try Again")
#
# sum = summation()
#
# sum.example()
# sum.example2()

# class me():
#
#     def __init__(self, name, age):
#         self.my_name = name
#         self.my_age = age
#
#
#     def compare(self, others):
#         if self.my_name == me2.my_name:
#             print("ha")
#             return True
#
#         else:
#             print("hiiiiii")
#             return False
#
#
#
# me1 = me("Kristian Roger M. Agdeppa", 18)
# me2 = me("Kristian Roger M. Agdeppa", 32)
#
#
# me1.compare(me2)

# TODO PASSING ARGUMENTS INTO VARIABLES USING NAMEDTUPLE
# try:
#     from collections import namedtuple
#     Point = namedtuple('_', 'cpu ram')
#     com1 = Point("Core i5 9th Gen", "16gb")
#     com2 = Point("Ryzen 7", "32gb")
#
#     print(f'The first computer has a {com1.cpu} CPU and {com1.ram} of RAM')
#     print(f'The second computer has a {com2.cpu} CPU and {com2.ram} of RAM')
# except ImportError:
#     pass

# TODO GETTING THE AREA AND RADIUS OF A CIRCLE USING CLASSES AND OBJECTS
# from math import pi
#
#
# class Circle():
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def cal_radius(self):
#         try:
#             print(f'The area of the circle with the given radius {self.radius}  is:  {pi * self.radius ** 2}')
#         except BaseException:
#             print("Error Try Again")
#             self.cal_radius()
#
#     def cal_perimeter(self):
#         try:
#             print(f'The perimeter of the circle with the given radius {self.radius} is: {2 * pi * self.radius}')
#         except BaseException:
#             print("Error Try Again")
#             self.cal_perimeter()
#
#     @staticmethod
#     def input1():
#         try:
#             input_radius = eval(input("Input the radius of the circle:"))
#             smrt_radius = Circle(input_radius)
#             smrt_radius.cal_radius()
#         except BaseException:
#             print("Error Try Again")
#             Circle.input1()
#
#     @staticmethod
#     def input2():
#         try:
#             input_perimeter = eval(input("Input the perimeter of the circle:"))
#             smrt_perimeter = Circle(input_perimeter)
#             smrt_perimeter.cal_perimeter()
#
#         except BaseException:
#             print("Error Try Again")
#             Circle.input2()
#
#
# Circle.input1()
# Circle.input2()

# TODO GETTING DISCOUNT USING CLASSES AND OBJECTS
# class Mobile():
#
#     def __init__(self, brand, model, color, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price
#
#     def new_price(self):
#         try:
#             self.price = eval(input("Enter the new price:"))
#         except BaseException:
#             print("Error Try Again")
#             self.new_price()
#
#     def discount_price(self):
#         try:
#             discount = eval(input("Enter the discount:"))
#             discount *= 100
#             discounted_price = self.price - (self.price * discount / 100)
#             print(f'The discounted price is ₱{discounted_price:,} for the {self.brand}, Model: {self.model}, '
#                   f'Color: {self.color}')
#             """ Sir ge apply lang nako ang brand, model tas color kay wala na gamit hehe """
#         except BaseException:
#             print("Error Try Again")
#             self.discount_price()
#
#
# mobile1 = Mobile("Realme", "RX9821", "Ocean Blue", "₱10,000")
#
#
# if __name__ == '__main__':
#     mobile1.new_price()
#     mobile1.discount_price()

# TODO class with decorators (classmethod & staticmethod)
# class Student():
#
#     _, *grades = 89, 78, 91, 87, 86
#
#     @staticmethod
#     def students_name(*Names):
#         return Names
#     """ @staticmethod is a type of decorator that turns a specific function
#         into static, which means that function is under the class and is still an
#         object however it can be used without passing an argument self"""
#
#
#     @classmethod
#     def student_grades(cls):
#         return cls.grades
#     """ @classmethod is a type of decorator that allows the function to use
#         the class variables (cls) means class and in order to access the
#         class variables you need to call cls followed by the name of the class
#         variable"""
#
#
# print(Student.students_name("Kristian", "Roger", "Agdeppa"))
# print(Student.student_grades())

# TODO EXTRACTING VOWELS IN A STRING
# my_name = "Kristian Roger Mariblanca Agdeppa"
# total = 0
# vowels = ('a', 'e', 'i', 'o', 'u')
# for i in my_name.lower():
#     try:
#         if i in vowels:
#             total += 1
#             print(i, end=" ")
#     except BaseException:
#         print("Error")
#
# print() # to separate the next print from the last one
# print("The number of vowels in my name is:", total)

# TODO CLASS INHERITANCE SINGLE-LEVEL & MULTI-LEVEL
# class class1(object):
#
#     def function1(self):
#         print("function 1 is working")
#
#
# class class2(class1):
#
#     def function2(self):
#         print("function 2 is working")
#
#
# class class3(class2):
#
#     def function3(self):
#         print("function 3 is working")
#
#
# """ Inheritance allows us to define a class that inherits all the methods and properties from another class.
#     Parent (main) class is the class being inherited from, also called base class.
#     Child (sub) class is the class that inherits from another class, also called derived class."""
#
# func1 = class3()
# func2 = class3()
# func3 = class3()

# func1.function1()
# func2.function2()
# func3.function3()

# TODO ABSTRACT CLASSES AND METHODS
# from abc import *
#
# """ In order to make an abstract class you need to import
#     a module called abc """
#
# class info(ABC):
#
#     @abstractmethod
#     def student1(self): pass
#
#     @abstractmethod
#     def student2(self): pass
#
#
# class students(info):
#
#     def student1(self): print("Student 1 is present")
#
#     def student2(self): print("Student 2 is present")
#
#
# x = students()
#
# x.student1()
# x.student2()
#
# """ Abstract classes can be inherited by any sub classes, including all the
#     abstract methods, all the values that the subclasses pass in the abstract methods
#     are not overridden """

# TODO GENERATORS
# def calculator(num1=0, num2=0, operator=""):
#
#     try:
#         if operator == "sum" or operator == "+":
#             yield num1 + num2
#         elif operator == "minus" or operator == "-":
#             yield num1 - num2
#         elif operator == "multiply" or operator == "*":
#             yield num1 * num2
#         elif operator == "divide" or operator == "/":
#             yield num1 / num2
#
#     except BaseException as e:
#         print(e)
#         calculator()
#
# try:
#     x = eval(input("Enter First Number:"))
#     opr = input("Enter Operator:").lower()
#     y = eval(input("Enter Second Number:"))
#
#     obj = calculator(x, y, opr)
#
#     for i in obj:
#         print(i)
#
#
# except BaseException as e:
#         print(e)







