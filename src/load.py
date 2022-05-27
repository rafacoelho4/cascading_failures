import igraph as ig

g = ig.Graph.Read_Edgelist('powergrid.edgelist.txt')
g.write_graphml('powergrid.GraphML')