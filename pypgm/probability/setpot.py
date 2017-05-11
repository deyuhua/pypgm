#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import numpy as np


def setpot(pot, variables, domains, inplace=False):

    new_pot = pot if inplace else copy.copy(pot)

    for var, dom in zip(variables, domains):

        idx = new_pot.variables.index(var)
        new_pot.table = np.take(new_pot.table, dom, axis=idx)

    new_pot.variables = [v for v in new_pot.variables if v not in variables]

    shape = tuple(len(v.domain) for v in new_pot.variables)
    new_pot.table = np.reshape(new_pot.table, shape)

    return new_pot
