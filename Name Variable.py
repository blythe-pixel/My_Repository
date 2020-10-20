def example():
    print("This came from", __name__)


if __name__ == '__main__':
    example()

""" The if __name__ == '__main__' is a type of statement that gives restrictions
    to the importer. The statements under it will run if the file is executed by itself.
    Else, it would not be executed """
