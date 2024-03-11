# CHAPTER 8
# 1. Make a list of all the data structures that you have used in your work with Python.

# -Lists
# -Tuples
# -Dictionaries
# -Strings
# -Array


# CHAPTER 9
# 2. You have an array an_array consisting of non-negative integers.Return an array in which all odd elements of the
# array an_array follow all even elements of an_array.


def an_array(arr):
    even = [i for i in arr if i % 2 == 0]
    odd = [i for i in arr if i % 2 != 0]
    return odd + even
