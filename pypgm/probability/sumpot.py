#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import numpy as np


def sumpot(pot, variables, inplace=False):

    new_pot = pot if inplace else copy.copy(pot)

    along_axis = tuple([i for i, v in enumerate(pot.variables) if v in variables])
    keep_variables = [v for v in pot.variables if v not in variables]

    new_pot.variables = keep_variables
    new_pot.table = np.sum(pot.table, axis=along_axis)

    return new_pot

