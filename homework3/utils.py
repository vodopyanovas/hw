# -*- coding: utf-8 -*-

"""
Utility functions, just doing simple tasks.
"""

__author__ = 'sobolevn'


def get_input_function():
    """
    This function returns right `input` function for python2 and python3.
    :return: function `input` in python3 or `raw_input` in python2.
    """

    try:
        input_function = raw_input
    except NameError:
        # `raw_input` was not defined, so `NameError` occured:
        input_function = input

    return input_function
