class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        # root x and root y
        xr = self.find(parent, x)
        yr = self.find(parent, y)

        if rank[xr] < rank[yr]:
            parent[xr] = yr
        elif rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[yr] = xr
            rank[xr] += 1

    def MST(self, existing):

        e = 0
        i = 0
        result = []
        parent = []
        rank = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.V):
            print 'node={}'.format(node)
            parent.append(node)
            rank.append(0)

        for edge in existing:
            result.append([edge[0], edge[1], 0])
            e = e + 1
            self.union(parent, rank, edge[0], edge[1])

        while e < self.V - 1:
            u, v, w = self.graph[i]
            print 'u={}, v={}, w={}'.format(u, v, w)
            i = i + 1
            print 'find(parent={}, i={})'.format(parent, u)
            x = self.find(parent, u)
            print 'find(parent={}, i={})'.format(parent, v)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return sum(c[1] for c in result)


def minimumCostIncurred(numTotalEdgeNodes,
                        numTotalAvailableNetworkRoutes,
                        networkRoutesAvailable,
                        numNewNetworkRoutesConstruct,
                        costNewNetworkRoutesConstruct):
    g = Graph(numTotalEdgeNodes)

    for edge in networkRoutesAvailable:
        # cost 0 - existing edges
        g.addEdge(edge[0]-1, edge[1]-1, 0)

    for edge in costNewNetworkRoutesConstruct:
        g.addEdge(edge[0]-1, edge[1]-1, edge[2])

    return g.MST(networkRoutesAvailable)

if __name__ == '__main__':
    numTotalEdgeNodes = 6
    numTotalAvailableNetworkRoutes = 3
    networkRoutesAvailable = [[1, 4], [4, 5], [2, 3]]
    numNewNetworkRoutesConstruct = 4
    costNewNetworkRoutesConstruct = [[1,2,5], [1,3,10], [1,6,2], [5,6,5]]

    print minimumCostIncurred(numTotalEdgeNodes,
                        numTotalAvailableNetworkRoutes,
                        networkRoutesAvailable,
                        numNewNetworkRoutesConstruct,
                        costNewNetworkRoutesConstruct)