# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# Fails nodes in multilayer graph due to neighbors 

# parameters:
# mg: multulayer graph :: MultilayerGraph from multinetx 
# node_color: matrix that sets the color of each node :: list of integer [0, 0, 0, 1, 1, 1, 2, 2, 2]
# phi: indicates the percentage of neighbors that should be failed for node to fail too :: float (0.0 - 1.0)

import networkx as nx
from plot import plotGraph, save
from failOne import failOne
from math import floor

def cascade(mg, node_color, phi):
    it = 1
    # if change is not noted in iteration, end loop
    change = 1
    while change:
        all_fails = []
        # going layer through layer
        for i in range(mg.get_number_of_layers()):
            n = mg.get_number_of_nodes_in_layers()[i]
            fails = []
            # get layer from multilayer graph
            layer = mg.get_layer(i)
            print("Layer ", i+1)
            adj = mg.get_inter_layer_edges()
            # [(13, 0), (14, 7), (14, 8), (18, 7), (19, 4), (20, 19), (22, 17), (23, 15), (24, 17), (26, 12)]
            # going through every node
            for node in layer.nodes:
                # not looking at vertices that have already failed
                if layer.nodes[node]["status"] == "failed":
                    continue
                    
                # get all neighbors to vertex
                neighbors = [n for n in layer.neighbors(node)]

                # quantity of neighbors failed
                y = 0
                for p in neighbors:
                    if layer.nodes[p]["status"] == "failed":
                        y = y + 1
                
                # for each inter layer connection 
                for item in adj: # ex: (13, 2)
                    # if current node is connected to a node in another layer NL
                    if item[0] == (node + i*n):
                        distant_neighbor = item[1]
                        # check if node NL from another layer is failed
                        div = floor(distant_neighbor / n)
                        mod = distant_neighbor % n
                        # getting layer of NL
                        aux_layer = mg.get_layer(div)
                        aux_node = aux_layer.nodes[mod]
                        # if NL has failed status 
                        if aux_layer.nodes[mod]["status"] == "failed":
                            # than number of failed neighbors increases by 1
                            y = y + 1
                        neighbors.append(distant_neighbor)

                    # if current node is connected to a node in another layer NL
                    elif item[1] == (node + i*n):
                        distant_neighbor = item[0]
                        # check if node NL from another layer is failed
                        div = floor(distant_neighbor / n)
                        mod = distant_neighbor % n
                        # getting layer of NL
                        aux_layer = mg.get_layer(div)
                        aux_node = aux_layer.nodes[mod]
                        # if NL has failed status 
                        if aux_layer.nodes[mod]["status"] == "failed":
                            # than number of failed neighbors increases by 1
                            y = y + 1
                        neighbors.append(distant_neighbor)

                # if percent of neighbors that have failed surpass phi, then vertex fails too
                if (len(neighbors) == 0):
                    percent = 0
                else:
                    percent = y / len(neighbors)
                if (percent > phi):
                    fails.append(node)

                # print([(fail+0) for fail in fails])

            all_fails.append(fails)
            
        # print("total fails this round:")
        for j in all_fails:
            print(j)

        # if no node failed this round, stop loop
        if(max([len(lis) for lis in all_fails]) == 0):
            change = 0
        else:
            # failing nodes in all layers 
            for j in range(len(all_fails)):
                for fail in all_fails[j]:
                    # print("layer:", j, "fail", fail, "fail + j*n", fail + j*n)
                    failOne(mg, node_color, fail)
                    # nx.set_node_attributes(mg.get_layer(j), {fail: "failed"}, name="status")
                    # nx.set_node_attributes(mg.get_layer(j), {fail: "red"}, name="color")
                    # node_color[j*mg.get_number_of_nodes_in_layers()[j] + fail] = "red"

        plotGraph(mg, node_color)
        filename = './output/it' + str(it) + '.png'
        save(mg, node_color, filename)
        it += 1

    return mg