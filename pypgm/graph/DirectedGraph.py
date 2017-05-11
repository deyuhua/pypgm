#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from networkx import DiGraph
from itertools import combinations
from functools import reduce
from .UndirectedGraph import UndirectedGraph


class DirectedGraph(DiGraph):

    def __init__(self, *args, **kwards):

        super(self.__class__, self).__init__(*args, **kwards)


    def add_node(self, node, weight=None):

        super(self.__class__, self).add_node(node, weight=weight)


    def add_nodes(self, nodes, weights=None):

        if weights:

            if len(nodes) != len(weights):

                raise Exception('nodes and weights must have smae length')

            else:

                for n, w in zip(nodes, weights):

                    self.add_node(node=n, weight=w)

        else:

            for n in nodes:

                self.add_node(node=n)


    def add_edge(self, u, v, weight=None):

        super(self.__class__, self).add_edge(u, v, weight=weight)


    def add_edges(self, ebunch, weights=None):

        if weights:

            if len(ebunch) != len(weights):

                raise Exception('ebunch and weights must have smae length')

            else:

                for edge, w in zip(ebunch, weights):

                    u, v = edge
                    self.add_edge(u, v, weight=w)

        else:

            for edge in ebunch:

                u, v = edge
                self.add_edge(u, v)


    def get_parent(self, node):

        return self.predecessors(node)


    def get_children(self, node):

        return self.successors(node)


    def moralize(self):

        moral_graph = UndirectedGraph(self.to_undirected().edges())

        for node in self.nodes():

            moral_graph.add_edges(combinations(self.get_parent(node), 2))

        return moral_graph


    def get_leaves(self):

        return [node for node, out_degree in self.out_degree_iter() if out_degree == 0]


    def get_roots(self):

        return [node for node, in_degree in self.in_degree_iter() if in_degree == 0]


    def get_markov_blanket(self, node):

        parent = self.get_parent(node)
        children = self.get_children(node)

        parent_of_children = reduce(lambda res, n: self.get_parent(n) + res, children, [])

        result = parent + children + parent_of_children
        result.remove(node)

        return result
