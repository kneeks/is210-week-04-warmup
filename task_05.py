#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that has a default"""


def defaults(my_required, my_optional=True):
    """This function compares two arguments.

    Args:
        my_required (boolean): Arg to compare to my_optional
        my_optional (boolean, optional): Arg to compare to my_required
        Default: True

    Returns:
        boolean: True or False

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
