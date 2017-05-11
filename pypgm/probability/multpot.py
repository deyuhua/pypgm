#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def multpot(*pots):

    return reduce(lambda pot_a, pot_b: pot_a * pot_b, pots)
