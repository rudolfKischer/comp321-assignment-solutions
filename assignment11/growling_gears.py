import numpy as np

# Acceleration of multi gear engines
# Torque - RPM
# T = -aR^2 + bR + c

# derivative
# T' = -a2R + b

# 0 = -a2R + b
# -b = -a2R
# b/a = 2R
# b/a2 = R
# R = b / 2a

# t_n = number of test cases
#     n = number of gears per test case
#         a, b, c = coefficients of the polynomial per gear


# we want to find the gear for which the maximum torque is generated

# we can find the root of derivative with the bisection method for each
# then we can input the the result of the root finding into our function
# then we can compare this among our different gear ratios


def get_input():
    t_n = int(input())

    test_cases = []

    for _ in range(t_n):
        
        n = int(input())

        A = [ np.array([int(c_i)for c_i in input().split()]) for _ in range(n)]

        test_cases.append(A)
    
    return test_cases
    


test_cases = get_input()

def max_gear(A):
    
    max_gear_val = 0
    max_gear_index = 0

    for i in range(len(A)):
        a = A[i][0]
        b = A[i][1]
        c = A[i][2]

        vertex = b / (2 * a) 

        vertex_val = -a*vertex*vertex + b* vertex + c

        if vertex_val > max_gear_val:
            max_gear_val = vertex_val
            max_gear_index = i
    
    return max_gear_index


for test_case in test_cases:
    print(max_gear(test_case) + 1)


    

        






        
    
    


