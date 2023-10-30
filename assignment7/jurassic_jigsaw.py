import numpy as np
from queue import PriorityQueue

# gene  strings
# constructing a tree
# need to find the tree that is most unlikely
# unlikliness: sum of weights of all edges, weights are number oof positions by which two strings differ

# input, n , k, 1   n < 1000, k < 10
# n = number of samples
# k = length of string

# each line after is a string of dna

# output
# length of min tree

# can construct and adjacency matrix 
# each row is one of the strings, and each col is one of the strings
# in each edge posiiton, copmute the hamming distance (# of differences in characters)

# Need to construct the minimum distance spanning tree

# note that a spanning tree will have n -1 edges
# note that every column and row will have at least one edge used

# could try a greedy approach if the graph was bigger

# could try a brute force , try all possible combinations, check if their valid



# Approch:

# Lazy Prims algorithm

# perform breadth first search, but use a priority qeue to sort nodes/edges base on
# the shortest edge distance

# we pop the first edge of the qeue, which would be the shortest one
# if the node has not been visited, we visit it
# we add its edges to the priority qeuee
# If we visit a node we add the edge we used to the MST 
# the PQ is empty , we stop

# if there is 

def string_to_binary(s):
    nucleotide_to_bits = {'A': 1, 'C': 2, 'G': 4, 'T': 8}
    binary = 0
    for nucleotide in s:
        binary = (binary << 4) | nucleotide_to_bits[nucleotide]
    return binary

# ! seems to have some issues
def ham_dist_fast(s1, s2):
  binary_1 = string_to_binary(s1)
  binary_2 = string_to_binary(s2)

  and_result = binary_1 & binary_2

  distance = 0
  while and_result != 0:
      if and_result & 0b1111 == 0:
          distance += 1
      and_result >>= 4 
  return distance

def ham_dist(s1,s2):
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def get_input():
    n, k = [int(string) for string in input().split()]
    strings = [input() for _ in range(n)]
    return n, k, strings

def adjacency_matrix(strings):

    n = len(strings)
    adjacency = np.zeros((n,n))

    for i in range(0,n):
      for j in range(0,n):
        if i == j:
          adjacency[i][j] = np.inf
          continue

        s1 = strings[i]
        s2 = strings[j]
        adjacency[i][j] = ham_dist(s1,s2)
    
    return adjacency

def get_min_edge(adj_mat, node_index):
    min_edge_node = np.argmin(adj_mat[:, node_index])
    edge = (adj_mat[node_index][min_edge_node], node_index, min_edge_node)
    return edge

def add_edges(pq, u, visited, adj_mat):
    visited[u]= True

    for v in range(adj_mat.shape[0]):
      if v == u:
        continue
      if not visited[v]:
        pq.put((adj_mat[u][v], u, v))

def get_mst(adj_mat):
    # edge = (adjmat(u,v), u,v)
  
    considering_edges = PriorityQueue()
    n = adj_mat.shape[0]
    visited = [False] * n
    mst_cost = 0
    mst = []

    add_edges(considering_edges, 0, visited, adj_mat)

    # while we have not made an mst, that has an edge for every node
    while len(mst) < (n -1) and considering_edges:
      cur_edge = considering_edges.get()
      weight, u, v = cur_edge

      if visited[v] or weight == np.inf:
        continue
      

      mst.append(cur_edge)
      mst_cost += weight
      add_edges(considering_edges, v, visited, adj_mat)
    
    return mst_cost, mst
    
n, k, strings = get_input()

adj_mat = adjacency_matrix(strings)

mst_cost, mst_list = get_mst(adj_mat)

print(int(mst_cost))
for edge in mst_list:
  print(int(edge[1]), int(edge[2]))





