# author: Rafael Coelho Monte Alto
# advisor: Prof. Dr. Vander Luis 
# 2022/2023

# Shows image of multilayer graph plotted 

# parameters:
# mg: multilayer graph :: MultilayerGraph from multinetx 
# node_color: matrix that sets the color of each node :: list of integer [0, 0, 0, 1, 1, 1, 2, 2, 2]

import matplotlib.pyplot as plt
import multinetx as mx

from style import COLORS, FIGURE

def plotGraph(mg, node_color, node_size=0, node_position=0):
    fig = plt.figure(figsize=FIGURE["size"])
    # first image: matrix of connections
    ax1 = fig.add_subplot(121)
    ax1.imshow(mx.adjacency_matrix(mg,weight='weight').todense(), origin='upper',interpolation='nearest',cmap=plt.cm.jet_r)
    ax1.set_title(FIGURE["title1"])
    # second image: graph drawing
    ax2 = fig.add_subplot(122)
    ax2.axis('off')
    ax2.set_title(FIGURE["title2"])

    if(not node_size): 
        node_size = FIGURE["node_size"] 
        return 

    if(not node_position): 
        custom_pos = {} 
        x = y = 0.01 
        print(mg.get_number_of_nodes_in_layers()[0])
        for i in range(mg.get_number_of_nodes_in_layers()[0]): 
            if i % 2 == 0: 
                custom_pos[i] = [x + i/100, 0.4] 
                # custom_pos[i] = [x + i/100, y + i/10]
            else: 
                custom_pos[i] = [x + i/100, -0.4] 
                # custom_pos[i] = [x + i/100, y - i/10]
        node_position = custom_pos

    pos = mx.get_position(mg,node_position,
                        layer_vertical_shift=1.4,
                        layer_horizontal_shift=0.0,
                        proj_angle=7)

    custom_edge_color = [COLORS["nodes"][(mg[a][b]['weight'] - 1) % len(COLORS["nodes"])] for a,b in mg.edges()]
    mx.draw_networkx(mg,pos=pos, ax=ax2, node_size=node_size, with_labels=FIGURE["with_labels"], node_color=node_color, 
                    edge_color=custom_edge_color,
                    edge_cmap=plt.cm.jet_r)

    plt.show()
    return 

def save(mg, node_color, filename):
    fig = plt.figure(figsize=FIGURE["size"])
    # first image: matrix of connections
    ax1 = fig.add_subplot(121)
    ax1.imshow(mx.adjacency_matrix(mg,weight='weight').todense(), origin='upper',interpolation='nearest',cmap=plt.cm.jet_r)
    ax1.set_title(FIGURE["title1"])
    # second image: graph drawing
    ax2 = fig.add_subplot(122)
    ax2.axis('off')
    ax2.set_title(FIGURE["title2"])
    custom_pos = {}
    x = y = 0.01
    for i in range(mg.get_number_of_nodes_in_layers()[0]):
        if i % 2 == 0:
            custom_pos[i] = [x + i/100, 0.4] 
            # custom_pos[i] = [x + i/100, y + i/10]
        else:
            custom_pos[i] = [x + i/100, -0.4] 
            # custom_pos[i] = [x + i/100, y - i/10]

    pos = mx.get_position(mg,custom_pos,
                        layer_vertical_shift=1.4,
                        layer_horizontal_shift=0.0,
                        proj_angle=7)

    custom_edge_color = [COLORS["nodes"][(mg[a][b]['weight'] - 1) % len(COLORS["nodes"])] for a,b in mg.edges()]
    mx.draw_networkx(mg,pos=pos, ax=ax2, node_size=FIGURE["node_size"], with_labels=FIGURE["with_labels"], node_color=node_color, 
                    edge_color=custom_edge_color,
                    edge_cmap=plt.cm.jet_r)
    plt.savefig(filename)
    plt.close(fig)
    return 