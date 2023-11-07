class Node:
    def __init__(self, v):
        self.v = v
        self.neighbors = []
        
inputl = [int(x) for x in input().split()]
nodes = {}
for i in range(inputl[0]):
    o = int(input())
    nodes[i] = Node(o)
for _ in range(inputl[1]):
    f = [int(x) for x in input().split()]
    nodes[f[0]].neighbors.append(nodes[f[1]])
    nodes[f[1]].neighbors.append(nodes[f[0]])
    
notvisited = set()
for v in nodes:
    notvisited.add(nodes[v])
flag = True
while notvisited:
    stack = [notvisited.pop()]
    currsum = 0
    visited = set()
    while stack:
        n = stack.pop()
        currsum += n.v
        visited.add(n)
        if n in notvisited:
            notvisited.remove(n)
        for ne in n.neighbors:
            if ne not in visited:
                stack.append(ne)
    if currsum != 0:
        print("IMPOSSIBLE")
        flag = False
        break

if flag:
    print("POSSIBLE")