#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import numpy as np


def normailize(pot, inplace=False):

    new_pot = pot if inplace else copy.copy(pot)
    new_pot.table /= np.sum(pot.table)

    return new_pot
