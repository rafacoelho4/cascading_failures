from igraph import *
import pandas as pd

# load graph
g = load("./input/powergrid.edgelist.txt")

# degree
dg = g.degree()
# betweenness
bt = g.betweenness()
# closeness
cl = g.closeness()

# panda header
header = ['id', 'degree', 'betweenness', 'closeness']
# panda actual data
data = []
# row of data
row = []

# iterator
i = 0
for v in g.vs:
    # id
    row.append(i)
    # degree
    row.append(dg[i])
    # betweenness
    row.append(bt[i])
    #closeness
    row.append(round(cl[i], 3))
    i = i + 1
    data.append(row)
    row = []

# creating data frame
data = pd.DataFrame(data, columns=header)
# converting to csv file
data.to_csv('./metrics/p_data.csv', index=False)
