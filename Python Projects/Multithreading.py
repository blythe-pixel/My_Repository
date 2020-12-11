# TODO PYTHON MULTITHREADING
# from time import sleep
# from threading import *
#
# """ In creating a thread you need to import a module called threading,
#     also to calculate the time dilation you need to import a module
#     called time and use a function called sleep()"""
#
# """ to create a thread the classes must inherit the keyword
#     Thread """
#
#
# class computer1(Thread):
#     def run(self):
#         for i in range(5):
#             print("Program 1 Scanning for Virus..")
#             """ sleep takes one argument it could be an int or a float
#                 and that will serve as a entry delay of the thread itself """
#             sleep(1)
#
#
# class computer2(Thread):
#     """ To run the Thread you must name your function run,
#         the function run you created was inherited from Thread
#         it is vital for the program to run """
#
#     def run(self):
#         for i in range(5):
#             print("Program 2 Scanning for Virus..")
#             """ sleep takes one argument it could be an int or a float
#                 and that will serve as a entry delay of the thread itself """
#             sleep(1)
#
#
# obj1 = computer1()
# obj2 = computer2()
#
# """ After passing an object to the classes, you can start your threads
#     by using the object you passed and accessed by a Thread function called
#     start()"""
#
# obj1.start()
# sleep(0.5)
# obj2.start()
#
# obj1.join()
# obj2.join()
#
# """ In order to print the programs that is not a child thread
#     all functions in the child thread must be executed, therefore
#     you cna use the Thread function called as join() accessed by the object
#     you passed to the classes """
#
# print("All programs are secured")
