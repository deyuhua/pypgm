#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def drawnet(G):

    import matplotlib.pyplot as plt
    import networkx

    networkx.draw_graphviz(G)
    plt.show()
