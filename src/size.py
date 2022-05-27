import csv
from igraph import *
import alg as A

# open the file in the write mode
f = open('./metrics/g_failsize.csv', 'w')

# creating csv writer
writer = csv.writer(f)

# csv file row
row = []

# load graph
g = load("./input/powergrid.edgelist.txt")

# iterator
# i = 1496
i = 0
for v in g.vs:
    # starting graph with failed node
    A.startG(g, i)
    # cascading failure
    A.cascade(g, 0.4, 100, 0)
    # couting how many nodes have failed
    size = A.countFail(g)
    # adding to row
    row.append(i)
    row.append(size)
    # writing row in csv file
    writer.writerow(row)
    # clear row
    row.clear()
    i = i + 1

# closing file
f.close()