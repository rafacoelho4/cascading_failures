from igraph import Graph, plot


def create_graph(fail):
    g = Graph()
    g.add_vertices(5)
    # A
    g.add_edges([(0, 1), (0, 2), (0, 4)])
    # B
    g.add_edges([(1, 2)])
    # C
    g.add_edges([(2, 3)])
    # D
    g.add_edges([(3, 4)])
    # Attributes
    g.vs["label"] = ["A", "B", "C", "D", "E", "F", "G"]
    g.vs["phi"] = 0.2
    g.vs["status"] = "running"
    g.vs[fail]["status"] = "fail"
    # Colors
    color_dict = {"fail": "red", "running": "green"}
    g.vs["color"] = [color_dict[status] for status in g.vs["status"]]
    return g


# GENERATING GRAPH
g = create_graph(0)
layout = g.layout("kk")

# LOOP
photo = 1
change = 1
while change:
    # keeping all vertices that fail
    fails = []
    # position in graph.vertices[]
    j = 0
    # plotting graph
    plot(g,
         './output/graph' + str(photo) + '.png',
         layout=layout,
         bbox=(300, 300),
         margin=20)
    photo += 1
    # going through all vertices
    for i in g.vs:
        # not looking at vertices that have already failed
        if g.vs[j]["status"] == "fail":
            j = j + 1
            continue
        # get all neighbors to vertex j
        neighbors = g.neighbors(g.vs[j])
        # y counts how many neighbours have failed
        y = 0
        # going through every neighbour
        for p in neighbors:
            if g.vs[p]["status"] == "fail":
                y = y + 1
        # if percent of neighbours that have failed surpass phi, then vertex fails too
        if (len(neighbors) == 0):
            percent = 0
        else:
            percent = y / len(neighbors)
        if (percent > g.vs[j]["phi"]):
            fails.append(j)
        j = j + 1
    # changing status and color of failed vertices
    for i in fails:
        g.vs[i]["status"] = "fail"
        g.vs[i]["color"] = "red"
    g.get_eid(1, 2)
    # if no vertex failed in this round, break free from loop
    if len(fails) == 0:
        change = 0

# load ou edge list