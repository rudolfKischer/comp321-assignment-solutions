class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootY] += 1

def kruskal(n, E):
    E.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    MST = []
    total_weight = 0

    for e in E:
        u, v, weight = e
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            MST.append((u, v))
            total_weight += weight

    if len(MST) != n - 1:
        return "Impossible", []

    return total_weight, MST

def find_mst(n, E):
    total_weight, mst = kruskal(n, E)
    if total_weight == "Impossible":
        return ["Impossible"]
    else:
        mst.sort()
        formatted_edges = [(min(u, v), max(u, v)) for u, v in mst]
        formatted_edges.sort()
        return [total_weight] + formatted_edges

def main():
    results = []
    n, m = list(map(int, input().split()))
    while [n, m] != [0, 0]:
        E = [tuple(map(int, input().split())) for _ in range(m)]
        results.append(find_mst(n,E))
        n, m = list(map(int, input().split()))

    for result in results:
        if result == "Impossible":
            print(result)
        else:
            print(result[0])
            for edge in result[1:]:
                print(edge[0], edge[1])

main()
