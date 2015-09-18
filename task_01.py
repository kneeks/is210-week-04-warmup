#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function knows what you mean and provides a statement.

    Args:
        wink (str): The person's name you are winking to.
        numwink (int, optional): Number of winks and nudges returned. Default: 2

    Returns:
        str: All agruments restringed into a sentence.

    Examples:

        >>> know_what_i_mean('Niko')
        'Know what I mean? NikoNiko, nudge nudge'
    `
        >>> know_what_i_mean('CUNY', 4)
        'Know what I mean? CUNYCUNYCUNYCUNY, nudge nudge nudge nudge'
        
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
