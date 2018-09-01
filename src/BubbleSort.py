# -*- coding: utf8 -*-
"""
Several possible implementations of the Bubble Sort algorithm.
These will normally consist of a base version and a set of possible optimizations.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

def bubbleSort(array: list):
    """
    Straightforward version of Bubble Sort.

    :param array: List of numbers
    """
    size = len(array)

    for i in range(size):
        for j in range(size - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                #array[j], array[j + 1] = array[j + 1], array[j]


def bubbleSortSmart(array: list):
    """
    Smart version of Bubble Sort.
    It assumes that the nth largest element is placed in its final position in the nth iteration.
    The inner 'for' loop avoids looking at the last n-1 elements in its nth iteration.

    :param array: List of numbers
    """
    size = len(array)

    for i in range(size):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                #array[j], array[j + 1] = array[j + 1], array[j]


def bubbleSortSmarter(array: list):
    """
    Smarter version of Bubble Sort.
    It memorizes the index of the last element to be switched and assumes that all the elements
    onwards are in their final positions. The next iteration will proceed until the the memorized
    index.

    :param array: List of numbers
    """
    size = len(array)

    while size > 0:
        idx = 0
        for j in range(size):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                #array[j], array[j + 1] = array[j + 1], array[j]
                idx = j + 1

        size = idx
