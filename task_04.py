#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defines a function and take three arguments."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This This statement ensures we have at least one litterbox for each
    kitten and that we have some catfood. It then uses inversion via not to
    answer whether or not we have too many kittens.

    Args:
        kittens (int): the number of kittens
        litterboxes (int): the number of available litterboxes
        catfood (boolean): representing whether or not any catfood existd

    Returns:
        boolean: True or False stating if there is too many kittens.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
