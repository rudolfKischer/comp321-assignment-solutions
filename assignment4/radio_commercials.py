from functools import lru_cache

def get_input():
    N_P = input().split()
    N, P = int(N_P[0]), int(N_P[1])
    seq = tuple([(int(val) - P) for val in input().split()])
    return N, P, seq

def max_profit(seq):
    if not seq:
        return 0
    @lru_cache(maxsize=None)
    def max_profit_aux(start):
        if start == 0:
            return seq[start]
        return max(seq[start], max_profit_aux(start-1) + seq[start])
    return max([ max(max_profit_aux(i),0) for i in range(len(seq)) ])

N, P, seq = get_input()
print(max_profit(seq))



# TESTING CODE BELOW

def brute_force(seq):
    max_profit = 0
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            profit = sum(seq[i:j+1])
            if profit > max_profit:
                max_profit = profit
    return max_profit

max_N = 100#000
max_P = 1000
students_listening = 2000

import random
def make_test_case():
    n = random.randint(0, max_N)
    p = random.randint(0, max_P)
    seq = [random.randint(0, students_listening) for _ in range(n)]
    seq = tuple([val - p for val in seq])
    return n, p, seq

def test(num_of_test_cases):
    for _ in range(num_of_test_cases):
        n, p, seq = make_test_case()
        print(seq)
        print(max_profit(seq))
        print(brute_force(seq))
        assert max_profit(seq) == brute_force(seq)

# test(10000)




    
    

# Below is the same function using a traditional look up table

# max_profs = [None] *  len(seq)
# def max_profit(start):
#     if max_profs[start]:
#         return max_profs[start]

#     if start == (len(seq) - 1):
#         max_profs[start] = seq[start]
#         return seq[start]
    
#     max_profs[start] = max(seq[start], seq[start] + max_profit(start+1))
#     return max_profs[start]



