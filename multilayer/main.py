# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# CASCADING FAILURES IN NETWORKS WITH MULTIPLE LAYERS 

import multinetx as mx
import os, shutil

from create import createGraph
from plot import plotGraph, save
from failOne import failOne
from cascade import cascade

def main():
    # number of layers
    l = 3
    # number of nodes (the same every layer)
    n = 10
    # number of arcs 
    m = int(n/2)

    # create graph
    mg, node_color = createGraph(l, n, m)
    # show graph
    plotGraph(mg, node_color)
    clearFolder('./output')
    save(mg, node_color, filename = './output/it' + str(0) + '.png')
    # failing one node
    mg = failOne(mg, node_color, 1)
    plotGraph(mg, node_color)

    # mg = cascade(mg, node_color, phi=0.4)
    mg = cascade(mg, node_color, phi=0.36)
    print("final result")
    printAtt(mg)
    plotGraph(mg, node_color)

    return

def printAtt(mg):
    for i in range(mg.get_number_of_layers()):
        dict = mx.get_node_attributes(mg.get_layer(i), "status")
        for key in dict:
            print('layer', i+1, ':', (key + i*mg.get_number_of_nodes_in_layers()[i]), '->', dict[key])

def clearFolder(foldername):
    folder = foldername
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            
if __name__ == "__main__":
    main()

