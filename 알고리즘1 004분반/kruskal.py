#Initializing the Graph Class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self,s,d,w):
        print("Edge : Weight\n")
        for s, d, w in self.MST:
            print("%s-%s:%s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)

#Implementing Disjoint Set data structure and its functions
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    #Function to implement Kruskal's Algorithm


g = Graph(10)
for i in range(1,11) :
    g.addNode("v"+str(i))
g.addEdge("v1", "v2", 32)
g.addEdge("v1", "v4", 17)
g.addEdge("v2", "v5", 45)
g.addEdge("v3", "v4", 18)
g.addEdge("v3", "v7", 5)
g.addEdge("v4", "v5", 10)
g.addEdge("v4", "v8", 3)
g.addEdge("v5", "v6", 28)
g.addEdge("v5", "v9", 25)
g.addEdge("v6", "v10", 6)
g.addEdge("v7", "v8", 59)
g.addEdge("v8", "v9", 4)
g.addEdge("v9", "v10", 12)

g.kruskalAlgo()
