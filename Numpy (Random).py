# TODO (Random Array Numbers)
from numpy import *

""" In numpy their is an import called random
    that allows you too manipulated large amount
    of numbers with specification"""


#  TODO (Random Integers)
def random_int():
    ran1 = random.randint(11, size=(5, 2))
    """ random.randint() allow you to have an array
        list of random integer numbers , and it is usually based
        on the size next to it, (Columns, Rows)"""

    print(ran1)


# TODO (Random Decimals)
def random_dec():
    ran2 = random.rand(10)
    """ "random.rand() allow you to have an array
        list of random decimals numbers """

    print(ran2)


# TODO (Data Distribution)
def data_dist():
    ran3 = random.choice(["Apple", "Banana", "Carrots", "Dragon_Fruit", "Elderberry", "Farkleberry"],
                         p=(0.1666666666666667, 0.1666666666666667, 0.1666666666666667,
                            0.1666666666666667, 0.1666666666666667, 0.1666666666666667), size=(2, 3))
    """ The random.choice() allows you to specify the desired
        integers ypu want to include, and this method allows us
        to specify the probability of each element using "p="
         but the probability point must equal to "1" """
    print(ran3)


# TODO (Odd or Even using random numbers)
def odd_or_even():
    rand = random.randint(0, 100, 10)

    for i in ndenumerate(rand):
        i = i[-1]
        if i % 2 == 0:
            print("Even:", i)

        else:
            print("Odd:", i)
            break


# TODO (Shuffling a Random Numbers)
def random_shuffle():
    arr = ([1, 2, 3, 4, 5])
    random.shuffle(arr)
    print(arr)

    """ random.shuffle() method makes changes to the original array """


# TODO (Permuting a Random Numbers (Permutation))
def permute():
    arr = array([1, 2, 3, 4, 5])
    print("Permuted Array:", random.permutation(arr))
    print("Original Array:", arr)

    """ random.permutation() method shuffles the elements in the 
        array without changing the original array"""


# TODO (Getting the Arithmetic value in each element inside an array list)
def simple_arithmetic():
    array1 = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    array2 = array([90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
    array3 = array([-1, 2, 3, -4, 5, 6, -7, -8, -9, 10])

    sum_ = add(array1, array2)
    print(f'This is the sum: {sum_}')
    difference_ = subtract(array1, array2)
    print(f'This is the difference: {difference_}')

    product_ = multiply(array1, array2)
    print(f'This is the product: {product_}')

    quotient_ = divide(array1, array2)
    print(f'This is the quotient: {quotient_}')

    remainder_ = remainder(array1, array2)
    print(f'This is the remainder: {remainder_}')

    power_ = pow(array1, array2)
    print(f'This is the power: {power_}')

    absolute_ = abs(array3)
    print(f'This is the absolute: {absolute_}')

    remainder_quotient = divmod(array1, array2)
    print(f'This is the remainder & qoutient: {remainder_quotient}')


# TODO (Cumulative Mathematical operations)
def cumulative_operations():
    import seaborn as sns
    import matplotlib.pyplot as plt

    def cumulative_sum():
        arr1 = array([1, 2, 3, 4, 5])
        print("This is the cumulative summation:", cumsum(arr1))
        print("Equation:[1, 1 + 2 = 3 + 3 = 6 + 4 = 10 + 5 = 15]")

    cumulative_sum()

    def cumulative_diff():
        arr2 = array([10, 15, 25, 5])
        print("This is the cumulative product:", diff(arr2))
        print("Equation:[15 - 10 = 5; 25 - 15 = 10; 5 - 25 = -20]")

    cumulative_diff()

    def cumulative_prod():
        arr3 = array([1, 2, 3, 4, 5])
        arr4 = arr3.copy()
        print("This is the cumulative product:", cumprod(arr4))

    cumulative_prod()

    x = random.randn(100)
    kwargs = {'cumulative': True}
    sns.distplot(x, hist_kws=kwargs, kde_kws=kwargs)
    plt.show()


# TODO (Set Operations)
def set_operations():
    array1 = ([1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 6])
    print(unique(array1))
