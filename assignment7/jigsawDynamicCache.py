from queue import PriorityQueue
# import random
# import time 
# import itertools
from functools import lru_cache

@lru_cache(maxsize=None)
def ham_dist(s1,s2):
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))



def get_input():
    n, k = [int(string) for string in input().split()]
    strings = [input() for _ in range(n)]
    return n, k, strings

def adj_mat(s1, s2):
    return ham_dist(*tuple(sorted((s1, s2))))
    # return ham_dist(s1, s2)


def add_edges(pq, u, visited, strings):
    visited[u]= True

    for v in range(len(strings)):
      if v == u:
        continue
      if not visited[v]:
        weight = adj_mat(strings[u], strings[v])
        pq.put((weight, u, v))

def get_mst(strings):
    # edge = (adjmat(u,v), u,v)
  
    considering_edges = PriorityQueue()
    n = len(strings)
    visited = [False] * n
    mst_cost = 0
    mst = []

    add_edges(considering_edges, 0, visited, strings)

    # while we have not made an mst, that has an edge for every node
    while len(mst) < (n -1) and considering_edges:
      cur_edge = considering_edges.get()
      weight, u, v = cur_edge

      if visited[v] or weight == np.inf:
        continue
      

      mst.append(cur_edge)
      mst_cost += weight
      add_edges(considering_edges, v, visited, strings)
    
    return mst_cost, mst


def main():
  n, k, strings = get_input()

  mst_cost, mst_list = get_mst(strings)


  print(int(mst_cost))
  for edge in mst_list:
    print(int(edge[1]), int(edge[2]))

main()



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
    mst_cost, mst_list = get_mst(strings)
    print("n: ", n, "k: ", k, "mst_cost: ", mst_cost)

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
  
