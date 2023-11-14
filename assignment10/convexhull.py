from math import atan2

def calculate_polar_angle_and_distance(p0, p1):
    angle = atan2(p1[1] - p0[1], p1[0] - p0[0])
    distance = (p1[0] - p0[0])**2 + (p1[1] - p0[1])**2
    return (angle, distance)

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def find_convex_hull(points: list):
    if all(p == points[0] for p in points):
        return [points[0]]
    
    lm_point = min(points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(points, key=lambda p: calculate_polar_angle_and_distance(lm_point, p))
    sorted_points.remove(lm_point)
    sorted_points.insert(0, lm_point)

    stack = [sorted_points[0], sorted_points[1]] # Add the first two points

    for i in range(2, len(sorted_points)):
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], sorted_points[i]) <= 0:
            stack.pop()

        stack.append(sorted_points[i])

    return stack

def main():
    output = []
    n = int(input())
    while n != 0:
        points = [tuple(map(int,input().split())) for _ in range(n)]
        output.append(find_convex_hull(points))
        n = int(input())
    for points in output:
        print(len(points))
        for p in points:
            print(f"{p[0]} {p[1]}")

main()