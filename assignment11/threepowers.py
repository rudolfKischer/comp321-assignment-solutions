
# S = powers of 3

# S_s = subset of S 
#SU_s = sum of the subset of s



# if all S_s were ordered by their sum what , what is the set at the nth position?

# input
# N = list of all n
# stop reading input when n equals 0
# |N| <= 100

# sum i^3 = [(n(n+1)) / 2]^2

# to get the nth set

# intuitively the set increases in order of binary

# ie. if we have our list [...81, 27, 9, 3 ,1]
# and we want to get the 7th set
# we will need to convert 7 to binary
# We will need to do n-1 because we index at 0, 
# 7 - 1 = 6
# 6 -> ... 0 0 1 1 0
# the ones that are included then are the plces where the bit is 1
#   -> ... 0 0 9 3 0

# to represnet this as math
# 6 -> ... 0 0 1 1 0
# i=-> ... 4 3 2 1 0
# ->   ... 3^i 
# ->   ... 3^2 , 3^1

for k in iter(lambda:int(input()),0):print(f"{{ {', '.join(str(3**i)for i in range(len(bin(k-1))-2)if(k-1)&1<<i)} }}")





# t = list(iter(lambda: int(input()), 0))
# for k in t:
#     print(f"{{ {', '.join(str(3 ** i) for i in range(len(bin(k - 1)) - 3, -1, -1) if (k - 1) & (1 << i))} }}")


# SLIGHTLY MORE CONCISE

# def get_input():
#     return list(iter(lambda: int(input()), 0))

# def bit_indices(n):
#     return [i for i, bit in enumerate(bin(n)[2:][::-1]) if bit == '1']

# def kth_sum(k):
#     return [3 ** i for i in bit_indices(k - 1)]

# test_cases = get_input()
# for test_case in test_cases:
#     print(f'{{ {", ".join(map(str, kth_sum(test_case)))} }}')

# Readable submission

# def get_input():
#     N = []
    
#     n_i = int(input())
#     while n_i != 0:
#         N.append(n_i)
#         n_i = int(input())
#     return N

# def bit_indices(n):
#     indices = []
#     i = 0
#     while n:
#         if n & 1:
#             indices.append(i)
#         n >>= 1
#         i += 1
#     return indices

# def kth_sum(k):
#     return [ 3 ** i for i in bit_indices(k-1) ]


# test_cases = get_input()

# for test_case in test_cases:
#     ser = kth_sum(test_case)
#     str_ser = ", ".join(map(str,ser))
#     print(f'{{ {str_ser} }}')


