from igraph import plot, load


# CASCADING FAILURE (graph, phi value --ex. 0.4, 0.2--, number of iterations, print or no)
def cascade(g, phi, r=5, p=0):
    it = 0
    # LOOP
    layout = g.layout("fr")
    change = 1
    while change:
        # keeping all vertices that fail
        fails = []
        # position in graph.vertices[]
        j = 0
        # plotting graph
        if p:
            if (it % 10) == 0:
                plot(g,
                     './output/it' + str(it) + '.png',
                     layout=layout,
                     bbox=(300, 300),
                     margin=20)
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
            if (percent > phi):
                fails.append(j)
            j = j + 1
        # changing status and color of failed vertices
        for i in fails:
            g.vs[i]["status"] = "fail"
            g.vs[i]["color"] = "red"
        # if no vertex failed in this round, break free from loop
        if len(fails) == 0:
            change = 0
        # limiting iterations
        it = it + 1
        if (it > r):
            return


# START GRAPH (graph, node that should be the first to fail)
def startG(g, fail):
    g.vs["status"] = "running"
    g.vs[fail]["status"] = "fail"
    # Colors
    color_dict = {"fail": "red", "running": "green"}
    g.vs["color"] = [color_dict[status] for status in g.vs["status"]]


# SIZE OF CASCADE FAIL (graph)
def countFail(g):
    n = 0
    i = 0
    for v in g.vs:
        if g.vs[i]["status"] == "fail":
            n = n + 1
        i = i + 1
    return n


# LOAD GRAPH
g = load("./input/powergrid.edgelist.txt")

# STARTING GRAPH
startG(g, 0)

# CASCADING FAILURE
cascade(g, 0.2, 100, 0)
