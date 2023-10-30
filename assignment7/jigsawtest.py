import numpy as np
from queue import PriorityQueue
import random
import time 
import itertools

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

    xor_result = binary_1 ^ binary_2  # Use XOR to find differing bits

    distance = 0
    while xor_result != 0:
        if xor_result & 0b1111:  # If the last 4 bits are not all zero
            distance += 1
        xor_result >>= 4
    return distance

def ham_dist(s1,s2):
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def ham_dist2(s1,s2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(s1, s2))))


def get_input():
    n, k = [int(string) for string in input().split()]
    strings = [input() for _ in range(n)]
    return n, k, strings

def adjacency_matrix(strings):

    n = len(strings)
    adjacency = np.zeros((n,n))

    for i in range(0,n):
      for j in range(i,n):
        if i == j:
          adjacency[i][j] = np.inf
          continue

        s1 = strings[i]
        s2 = strings[j]
        adjacency[i][j] = ham_dist(s1,s2)
    
    # for i in range(0,n):
    #   for j in range(0,i):
    #     adjacency[i][j] = adjacency[j][i]
    
    return adjacency

def add_edges(pq, u, visited, adj_mat):
    visited[u]= True

    for v in range(n):#range(u+1, adj_mat.shape[0]):
      if v == u:
        continue
      if not visited[v]:
        weight = adj_mat[u][v]
        if u > v:
          weight = adj_mat[v][u]

        pq.put((weight, u, v))



    

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
    


def generate_test_case(n , k ):
  # max n = 1000
  # max k = 10
  strings = []
  for _ in range(n):
    string = ""
    for _ in range(k):
      string += random.choice("ACGT")
    strings.append(string)
  return (n, k, strings)

def generate_test_cases(m):
  test_cases = []
  for _ in range(m):
    n = random.randint(1, 1000)
    k = random.randint(1, 10)
    test_cases.append(generate_test_case(n, k))
  return test_cases

def test():
  test_cases = generate_test_cases(1)
  for test_case in test_cases:
    n, k, strings = test_case
    print("n: ", n, "k: ", k)
    for string in strings:
      print(string)
    adj_mat = adjacency_matrix(strings)
    mst_cost, mst_list = get_mst(adj_mat)
    print("n: ", n, "k: ", k, "mst_cost: ", mst_cost)

n, k, strings = get_input()

adj_mat = adjacency_matrix(strings)
# print(adj_mat)

mst_cost, mst_list = get_mst(adj_mat)


print(int(mst_cost))
for edge in mst_list:
  print(int(edge[1]), int(edge[2]))

# test()

# test ham_dist
# test_case = generate_test_case(2, 5)
# n, k, strings = test_case
# print(strings)
# print(ham_dist_fast(strings[0], strings[1]))

# # test ham_dist_fast, and compare to ham_dist for correctness with a bunch of test cases
# # print if ther are different
# test_cases = generate_test_cases(100)
# for test_case in test_cases:
#   n, k, strings = test_case
#   print("n: ", n, "k: ", k)
#   start = time.time()
#   distances_slow = []
#   for i, j in itertools.combinations(range(n), 2):
#     distances_slow.append(ham_dist(strings[i], strings[j]))
#   end = time.time()
#   print("ham_dist time: ", end - start)
#   start = time.time()
#   distances_fast = []
#   for i, j in itertools.combinations(range(n), 2):
#     distances_fast.append(ham_dist_fast(strings[i], strings[j]))
#   end = time.time()
#   print("ham_dist_fast time: ", end - start)
#   if distances_slow != distances_fast:
#     print("different")
#     break
#   else:
#     print("same")
  
