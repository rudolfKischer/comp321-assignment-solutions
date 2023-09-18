import numpy as np
import sys

error_threshold = 10**(-5)

def ternary_search(f, a, b):
    while abs(b - a) > error_threshold:
        c = a + (b - a) / 3
        d = b - (b - a) / 3
        if f(c) < f(d):
            b = d
        else:
            a = c
    return (a, f(a))
    
def longest_distance(x, houses):
    distance = lambda house: np.linalg.norm(np.array([x,0]) - house)
    return max(map(distance, houses))

def get_shortest_max_distance(houses):
    houses = np.array(houses)
    f = lambda x: longest_distance(x, houses)
    return ternary_search(f, houses[:, 0].min(), houses[:, 0].max())

def test_cases():
    for line in sys.stdin:
        n = line.strip()
        if not n:
            continue
        n = int(n)
        if n == 0:
            return
        houses = [np.array(list(map(float, next(sys.stdin).split()))) for _ in range(n)]
        yield houses

tests = list(test_cases())

for test_case in tests:
    result = get_shortest_max_distance(test_case)
    result = [f"{num:.12f}" for num in result]
    print(*result)
