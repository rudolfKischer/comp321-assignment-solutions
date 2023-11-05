def find_inserted_dna_length(o, m):
    start = 0
    end_o = len(o)
    end_m = len(m)
    while start < end_o and start < end_m and o[start] == m[start]:
        start += 1
    while end_o > start and end_m > start and o[end_o-1] == m[end_m-1]:
        end_o -= 1
        end_m -= 1
    return end_m - start

import sys

o_seq = sys.stdin.readline().strip()
m_seq = sys.stdin.readline().strip()

length = find_inserted_dna_length(o_seq, m_seq)
print(length)
