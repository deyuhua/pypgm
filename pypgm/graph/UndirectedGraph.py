#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import combinations
from networkx import Graph


class UndirectedGraph(Graph):


    def __init__(self, *args, **kwards):

        super(self.__class__, self).__init__(*args, **kwards)


    def add_node(self, node, weight=None):

        super(self.__class__, self).add_node(node, weight=weight)


    def add_nodes(self, nodes, weights=None):

        if weights:

            if len(nodes) != len(weights):

                raise Exception('nodes and weights must have smae length')

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


    def is_clique(self, nodes):

        return all([self.has_edge(u, v) for u, v in combinations(nodes, 2)])


    def is_triangulated(self):

        return nx.is_chordal(self)


    def get_markov_blanket(self, node):

        return self.neighbors(node)


