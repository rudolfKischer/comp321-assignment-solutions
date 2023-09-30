
import matplotlib.pyplot as plt
import random
error_threshold = 1e-5

def convex_hull(points):
    if len(points) <= 1:
        return points


    points = sorted(set(map(tuple, points)))

    def build(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull += p,
        return hull

    return build(points)[:-1] + build(points[::-1])[:-1]

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    

def ternary_search(f, a, b):
    iters_limit = 60
    iters = 0
    while abs(b - a) > error_threshold:
        c = a + (b - a) / 3
        d = b - (b - a) / 3
        if f(c) < f(d):
            b = d
        else:
            a = c

        if iters > iters_limit:
            break
        iters += 1
    return (a, f(a)**0.5)

def get_shortest_max_distance(houses):
    
    houses = convex_hull(houses)
    
    def longest_distance(x):
        max_distance = float('-inf')
        for house in houses:
            distance_square = (house[0] - x)**2 + house[1]**2
            distance = distance_square #**0.5
            max_distance = max(max_distance, distance)
        return max_distance
    
    min_x = -200000
    max_x = 200000
    
    return ternary_search(longest_distance, min_x, max_x)

def test_cases():
    while True:
        n = input().strip()
        if not n:
            continue
        n = int(n)
        if n == 0:
            return

        # Using a list comprehension to read and convert data
        houses = [list(map(float, input().split())) for _ in range(n)]
        yield houses




def generate_cases(t):
    # return as a list of test cases
    from random import randint, uniform
    min_val = -200000
    max_val = 200000
    n = 50000

    test_cases = []
    for _ in range(t):
        test_case = []
        for _ in range(n):
            x = randint(min_val, max_val)
            y = randint(min_val, max_val)
            test_case.append([x, y])
        test_cases.append(test_case)
    return test_cases


# tests = list(test_cases())
tests = generate_cases(10)

for test_case in tests:
    result = get_shortest_max_distance(test_case)
    result = [f"{num:.12f}" for num in result]
    print(*result)

# def print_generate_test_cases(t):
#     from random import randint, uniform
#     test_cases = generate_cases(t)
#     for test_case in test_cases:
#         print(len(test_case))
#         for house in test_case:
#             print(*house)
#         print()


# def generate_points(n, lower_bound=-100, upper_bound=100):
#     """Generate n random points."""
#     return [(random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound)) for _ in range(n)]

# def plot_points(points, hull):
#     """Plot the points and their convex hull."""
#     plt.scatter(*zip(*points), c='blue', marker='o')
#     plt.scatter(*zip(*hull), c='red', marker='o')
#     plt.plot(*zip(*hull + [hull[0]]), c='red')
#     plt.show()

# points = generate_points(100)
# hull = convex_hull(points)
# plot_points(points, hull)