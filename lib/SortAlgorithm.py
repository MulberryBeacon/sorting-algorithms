# -*- coding: utf8 -*-
"""
Set of generic and common functions for sort algorithms.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

def swapElements(list: list, p1: int, p2: int):
    """
    Swaps a pair of elements.

    :param list: List of elements
    :param p1: First element of the pair
    :param p2: Second element of the pair
    """
    aux = list[p1]
    list[p1] = list[p2]
    list[p2] = aux
