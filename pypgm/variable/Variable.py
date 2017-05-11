#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
from datetime import datetime


__all__ = ['Variable']


class Variable(object):

    def __init__(self, name, domain, card):

        self.name = name

        if isinstance(domain, (list, tuple, np.ndarray)):

            self.domain = np.array(domain)

        else:

            raise Exception('domain must be array-like data structure')

        self.card = card


    def __str__(self):

        return 'variable {0} has domain: [{1}]'.format(
            self.name,
            ','.join([str(v) for v in self.domain.tolist()])
        )


    def __hash__(self):

        return self.card


    def __eq__(self, that):

        return all([self.name == that.name,
                    self.card == that.card,
                    all([f == s for f, s in zip(self.domain.tolist(), that.domain.tolist())])])

