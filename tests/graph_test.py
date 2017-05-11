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

student_graph = DirectedGraph()

for v in student_vars:

    student_graph.add_node(v.card)

edges = [(0, 2), (1, 2), (2, 4), (1, 3)]
student_graph.add_edges(edges)

class GraphTest(unittest.TestCase):

    def test_graph_create(self):

        student_graph = DirectedGraph()

        for v in student_vars:

            student_graph.add_node(v.card)

        edges = [(0, 2), (1, 2), (2, 4), (1, 3)]
        student_graph.add_edges(edges)


    def test_edges(self):

        student_graph = DirectedGraph()

        for v in student_vars:

            student_graph.add_node(v.card)

        edges = [(0, 2), (1, 2), (2, 4), (1, 3)]
        student_graph.add_edges(edges)

        edges_t = student_graph.edges()

        edges_set = set(edges)
        edges_t_set = set(edges_t)

        self.assertTrue(all([
            all([v in edges_set for v in edges_t_set]),
            all([v in edges_t_set for v in edges_set])
        ]))


    def test_nodes(self):

        nodes_t = student_graph.nodes()

        nodes_set = {v.card for v in student_vars}
        nodes_t_set = set(nodes_t)

        self.assertTrue(all([
            all([v in nodes_set for v in nodes_t_set]),
            all([v in nodes_t_set for v in nodes_set])
        ]))


    def test_get_parents(self):

        parents = (0, 1)
        parents_t = student_graph.get_parent(2)

        self.assertTrue(all([
            all([v in parents_t for v in parents]),
            all([v in parents for v in parents_t])
        ]))

        self.assertTrue(student_graph.get_parent(4)[0] == 2)
        self.assertTrue(student_graph.get_parent(3)[0] == 1)


    def test_get_children(self):

        children = (2, 3)
        children_t = student_graph.get_children(1)

        self.assertTrue(all([
            all([v in children_t for v in children]),
            all([v in children for v in children_t])
        ]))

        self.assertTrue(student_graph.get_children(0)[0] == 2)
        self.assertTrue(student_graph.get_children(2)[0] == 4)


    def test_moralize(self):

        moralize_graph = student_graph.moralize()

        self.assertTrue(moralize_graph.has_edge(0, 1))


    def test_get_leaves(self):

        result = (3, 4)
        resutl_t = student_graph.get_leaves()

        self.assertTrue(all([
            all([v in resutl_t for v  in result]),
            all([v in result for v in resutl_t])
        ]))


    def test_get_roots(self):

        result = (0, 1)
        result_t = student_graph.get_roots()

        self.assertTrue(all([
            all([v in result for v in result_t]),
            all([v in result_t for v in result])
        ]))


    def test_get_markov_blanket(self):

        result = (0, 1, 4)
        result_t = student_graph.get_markov_blanket(2)

        self.assertTrue(all([
            all([v in result for v in result_t]),
            all([v in result_t for v in result])
        ]))

        moralize_graph = student_graph.moralize()
        result_t = moralize_graph.get_markov_blanket(2)

        self.assertTrue(all([
            all([v in result for v in result_t]),
            all([v in result_t for v in result])
        ]))


    def test_is_clique(self):

        moralize_graph = student_graph.moralize()

        self.assertTrue(moralize_graph.is_clique([0, 1, 2]))
        self.assertTrue(moralize_graph.is_clique([2, 4]))
        self.assertTrue(moralize_graph.is_clique([1, 2]))


    def test_is_triangulated(self):

        moralize_graph = student_graph.moralize()

        self.assertTrue(moralize_graph)



if __name__ == '__main__':

    unittest.main()
