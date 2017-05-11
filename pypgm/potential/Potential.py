#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import copy
from functools import reduce


__all__ = ['Potential']


class Potential(object):

    def __init__(self, variables, table):

        self.variables = list(variables)
        self.table = np.asarray(table)

        if len(self.variables) != self.table.ndim:

            raise Exception('')


    def __mul__(self, that, inplace=False):

        ### calculate dim that need to extended
        calc_extended_dim = lambda pot, vars_set: tuple(
            [v in pot.variables and len(v.domain) or 1 for v in vars_set]
        )

        new_pot = self if inplace else copy.copy(self)

        table_self = self.table.copy()
        table_that = that.table.copy()

        union_varialbes = list(set(self.variables + that.variables))
        union_dims = tuple([len(v.domain) for v in union_varialbes])

        extend_dim_self = calc_extended_dim(self, union_varialbes)
        extend_dim_that = calc_extended_dim(that, union_varialbes)

        table_self = table_self.reshape(extend_dim_self)
        table_that = table_that.reshape(extend_dim_that)

        new_pot.variables = union_varialbes
        new_pot.table = reduce(lambda tab_a, tab_b: tab_a * tab_b,
                               [table_self, table_that],
                               np.ones(union_dims))

        return new_pot


    def __div__(self, that, inplace=False):

        new_pot = self if inplace else copy.copy(self)

        table_self = self.table.copy()
        talbe_that = that.table.copy()

        new_pot.table = table_self / table_that

        return new_pot


    def __str__(self):

        return """
varialbes:\n{variables}\n
table:\n{table}
        """.format(variables='\n'.join(['\t' + str(v) for v in self.variables]),
                   table=self.table)

    def __repl__(self):

        return self.__str__()
