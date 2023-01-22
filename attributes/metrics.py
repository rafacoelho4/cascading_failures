import csv
from igraph import *

# open the file in the write mode
f = open('./metrics/g_metrics.csv', 'w')
# create the csv writer
writer = csv.writer(f)

# load graph
g = load("./input/powergrid.edgelist.txt")

# file row
row = []

# degree
dg = g.degree()
# betweenness
bt = g.betweenness()
# closeness
cl = g.closeness()

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
    # write a row to the csv file
    writer.writerow(row)
    i = i + 1
    row.clear()

# close the file
f.close()