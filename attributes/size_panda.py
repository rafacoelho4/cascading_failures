import pandas as pd
from igraph import *
import alg as A

print("Calculating cascade fail size:")
phi = input("phi: ")
it = input("iterations: ")
n = input("number of nodes (0 if you want to go through all nodes): ")

# load graph
g = load("./input/powergrid.edgelist.txt")

# panda actual data
data = []
# row of data
row = []

if (int(n) != 0):
    i = 0
    for v in g.vs:
        # starting graph with failed node
        A.startG(g, i)
        # cascading failure
        A.cascade(g, float(phi), int(it), 0)
        # couting how many nodes have failed
        size = A.countFail(g)
        # adding to row
        row.append(i)
        row.append(size)
        # data
        data.append(row)
        # reseting row
        row = []
        print(i, size)
        i = i + 1
        if (i > int(n)):
            break
else:
    # iterator
    i = 0
    for v in g.vs:
        # starting graph with failed node
        A.startG(g, i)
        # cascading failure
        A.cascade(g, 0.4, 10000, 0)
        # couting how many nodes have failed
        size = A.countFail(g)
        # adding to row
        row.append(i)
        row.append(size)
        # data
        data.append(row)
        # reseting row
        row = []
        print(i, size)
        i = i + 1

# creating data frame
data = pd.DataFrame(data, columns=['id', 'fail size'])
# converting to csv file
data.to_csv("./size_output/p_failsize_phi" + phi.replace('.', '') + "_it" +
            it + ".csv",
            index=False)
