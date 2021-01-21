class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# get the keys of the dictionary
    def getvertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

# find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# add vertex as a key
    def addvertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

# add the new edge
    def addedge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


graph_element = {
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['e'],
    'e':['d']
}

g = Graph(graph_element)
print(g.getvertices())
print(g.edges())
g.addvertex('f')
print(g.getvertices())
g.addedge({'a','e'})
g.addedge({'a','c'})
print(g.edges())