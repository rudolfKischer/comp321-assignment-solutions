import numpy as np

# N apple trees
# triangular land

# given triangle vertices
# calculate area of triangle
# loop over all points and check if they are in the triangl

# first three lines are the coordinates


def get_input():
    vertices = [ input().split() for _ in range(0,3)]
    vertices = [ [int(x),int(y)] for x, y in vertices]
    vertices = [ np.array(vertice) for vertice in vertices]

    n = int(input())

    apples = [ input().split() for _ in range(n)]
    apples = [ [int(x),int(y)] for x, y in apples]
    apples = [ np.array(apple) for apple in apples]

    return vertices, apples

def get_area(A,B,C):
    AB = B - A
    AC = C - A
    # area of a tirangel is half the parallelogram
    # thea area of the parallelgoram is given by the cross product
    return 0.5 * abs(np.cross(AB, AC))

def contains(A,B,C,P):
    
    ABC = get_area(A,B,C)

    PBC = get_area(P,B,C) #A1

    PAC = get_area(P,A,C) #A2

    PAB = get_area(P,A,B)

    return ABC == (PBC + PAC + PAB)


    # AB = B - A
    # BC = C - B
    # CA = A - C
    # AP = P - A
    # BP = P - B
    # CP = P - C
    # return np.cross(AB,AP) >= 0 and np.cross(BC,BP) >= 0 and np.cross(CA,CP) >= 0
    

vertices, apples = get_input()
A, B, C = vertices
area = get_area(A, B, C)
# num of apples
num_of_apples = sum([ contains(A, B, C, apple) for apple in apples ])
print(f'{area:.1f}')
print(num_of_apples)