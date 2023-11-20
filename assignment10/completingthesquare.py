
import numpy as np
# need to find the corner of the circle

# input is three lines, each line contains two integers dentoing xand y

def get_input():
    A = np.array(input().split(), dtype=int)
    B = np.array(input().split(), dtype=int)
    C = np.array(input().split(), dtype=int)
    return A, B, C



def get_corner(A, B, C):
    
    AB = B - A
    BC = C - B
    CA = A - C

    AB_BC = np.dot(AB,BC)
    if AB_BC == 0:
        return A + BC

    BC_CA = np.dot(BC,CA)
    if BC_CA == 0:
        return B + CA

    # CA_AB = np.dot(CA,AB)
    
    return C + AB


corner = get_corner(*get_input())

print(f'{corner[0]} {corner[1]}')

