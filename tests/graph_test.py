#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from pypgm.variable import Variable
from pypgm.potential import Potential
from pypgm.graph import DirectedGraph, UndirectedGraph
from pypgm.utils import drawnet


### varibales define

difficulty = Variable('difficulty', [0, 1], 0)
intelligence = Variable('intelligence', [0, 1], 1)
grade = Variable('grade', [0, 1, 2], 2)
sat = Variable('sat', [0, 1], 3)
latter = Variable('latter', [0, 1], 4)

student_vars = [difficulty, intelligence, grade, sat, latter]


### unit test case

class GraphTest(unittest.TestCase):

    def test_graph_create(self):

        student_graph = DirectedGraph()

        for v in student_vars:

            student_graph.add_node(v.card)

        student_graph.add_edges([[0, 2], [1, 2], [2, 4], [1, 3]])

        drawnet(student_graph)


if __name__ == '__main__':

    unittest.main()
