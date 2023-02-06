# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# Fails only one node in a multilayer graph

# parameters:
# mg: multulayer graph :: MultilayerGraph from multinetx 
# node_color: matrix that sets the color of each node :: list of integer [0, 0, 0, 1, 1, 1, 2, 2, 2]
# n: node that will fail :: integer

# returns:
# mg: multilayer graph 

import networkx as nx
import multinetx as mx

from create import createGraph
from plot import plotGraph

from style import COLORS

def failOne(mg, node_color, f):
    # going layer through layer
    for i in range(mg.get_number_of_layers()):
        n = mg.get_number_of_nodes_in_layers()[i]
        # get layer from multilayer graph
        layer = mg.get_layer(i)

        # failing one node
        # print("Falhando", f, "in layer", i)
        layer.nodes[f]["status"] = "failed"
        layer.nodes[f]["color"] = "red"

        node_color[i*n + f] = COLORS["fail"][0]

    return mg
