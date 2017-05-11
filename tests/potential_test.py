#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import copy


from pypgm.potential import Potential
from pypgm.variable import Variable
from pypgm.probability import multpot, sumpot, normailize, setpot, condpot


### vairables and potential

difficulty = Variable('difficulty', [0, 1], 0)
intelligence = Variable('intelligence', [0, 1], 1)
grade = Variable('grade', [0, 1, 2], 2)
sat = Variable('sat', [0, 1], 3)
latter = Variable('latter', [0, 1], 4)

difficulty_pot = Potential([difficulty], [0.6, 0.4])
intelligence_pot = Potential([intelligence], [0.7, 0.3])
grade_pot = Potential([grade, difficulty, intelligence], [[[0.3, 0.4, 0.3],
                                                           [0.9, 0.08, 0.02]],
                                                          [[0.05, 0.25, 0.7],
                                                           [0.5, 0.3, 0.2]]])
sat_pot = Potential([sat, intelligence], [[0.95, 0.05], [0.2, 0.8]])
latter_pot = Potential([latter, grade], [[0.1, 0.9], [0.4, 0.6], [0.99, 0.01]])


### potential test case
dlt = 10 ** (-10)


class PotentialTest(unittest.TestCase):

    def test_probability(self):

        di_pot = multpot(*[difficulty_pot, intelligence_pot])
        mult_pot = multpot(*[difficulty_pot, intelligence_pot, grade_pot])
        sum_pot = sumpot(mult_pot, [grade])

        self.assertTrue((di_pot.table - sum_pot.table).sum() < dlt)


    def test_normalize(self):

        copy_pot = multpot(*[difficulty_pot, intelligence_pot, grade_pot])

        scale_copy_pot = copy.copy(copy_pot)
        scale_copy_pot.table *= 18.1

        self.assertTrue((copy_pot.table - normailize(scale_copy_pot).table).sum() < dlt)


    def test_setpot(self):

        joint_pot = multpot(*[difficulty_pot, intelligence_pot, grade_pot, latter_pot])

        for i in range(len(grade_pot.variables)):

            pick_vars = [grade]
            pick_domains = [[i]]

            margin = setpot(joint_pot, pick_vars, pick_domains)
            uniont_vars = list(set(joint_pot.variables) - set(pick_vars))

            self.assertTrue(all([
                all([v in uniont_vars for v in margin.variables]),
                all([v in margin.variables for v in uniont_vars])
            ]))

            self.assertTrue((margin.table.sum() - joint_pot.table[:, :, i, :].sum()) < dlt)


    def test_condpot(self):

        pick_vars = [grade]
        pick_domains = [[1]]

        joint_pot = multpot(*[difficulty_pot, intelligence_pot, grade_pot])
        margin = setpot(joint_pot, pick_vars, pick_domains)

        res_pot = condpot(margin, [intelligence])
        ture_res = np.array([0.8252427184466019, 0.17475728155339806])

        self.assertTrue((res_pot.table - ture_res).sum() < dlt)


if __name__ == '__main__':

    unittest.main()
