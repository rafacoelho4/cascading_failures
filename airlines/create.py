# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# Defines a function 'create' that generates a multilayer graph

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import multinetx as mx
import random 

from style import COLORS

def createAir(l, n, active, matrix):
    g = []
    for i in range(l):
        gx = nx.Graph(directed=False)
        gx.add_nodes_from(range(0, n))
        gx.add_edges_from(matrix[i])
        # all nodes start in disabled status
        nx.set_node_attributes(gx, "disabled", "status")
        nx.set_node_attributes(gx, "white", "color")
        # disabled airports whithin an airline 
        for j in active[i]:
            nx.set_node_attributes(gx, {j: "running"}, name="status")
            nx.set_node_attributes(gx, {j: "green"}, name="color")
        # adding to array of layers 
        g.append(gx)
    # adj block defines interlayer edges
    adj_block = mx.lil_matrix(np.zeros((n*l,n*l)))
    # mirrroring
    adj_block += adj_block.T
    mg = mx.MultilayerGraph(list_of_layers=g, inter_adjacency_matrix=adj_block)
    # weight of inter layer edges
    mg.set_edges_weights(inter_layer_edges_weight=4)
    # weights for edges within same layer
    for i in range(l):
        mg.set_intra_edges_weights(layer=i, weight=i+1)
    # each layer has nodes their own distinct color
    node_color = []
    for i in range(mg.get_number_of_layers()):
        for j in range(mg.get_number_of_nodes_in_layers()[i]):
            node_color.append("white")
        for b in active[i]:
            node_color[b+(n*i)] = (COLORS["nodes"][i % len(COLORS["nodes"])])

    return mg, node_color