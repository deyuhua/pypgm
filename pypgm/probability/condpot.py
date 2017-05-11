#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import numpy as np

from .sumpot import sumpot
from .normalize import normailize


def condpot(pot, query_vars):

    sum_vars = [v for v in pot.variables if v not in query_vars]

    res_pot = sumpot(pot, sum_vars)
    res_pot.table /= res_pot.table.sum()

    return normailize(res_pot)
