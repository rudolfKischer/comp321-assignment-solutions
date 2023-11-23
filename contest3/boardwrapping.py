from math import atan2
import numpy as np
def calculate_polar_angle_and_distance(p0, p1):
    angle = atan2(p1[1] - p0[1], p1[0] - p0[0])
    distance = (p1[0] - p0[0])**2 + (p1[1] - p0[1])**2
    return (angle, distance)

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def find_convex_hull(points: list):
    points = list( map(list,points))
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

def get_area(A,B,C):
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    AB = B - A
    AC = C - A
    return 0.5 * abs(np.cross(AB, AC))

def area_convex(points):
    p = points[0]
    area = 0
    for i in range(1, len(points)-1):
        area+=get_area(p,points[i],points[i+1])

    return area
        

def get_coords(x,y,w,h,v):
    M = [
        (-w/2,-h/2), (w/2,-h/2), (w/2, h/2), (-w/2,h/2)
    ]
    M = list(map(np.array,M))
    R = np.array([[np.cos(np.pi/180 * v), -np.sin(np.pi/180 * v)],
                 [ np.sin(np.pi/180 * v), np.cos(np.pi/180 * v)]])
    # transpose 
    # R = R.T
    
    X = np.array([x,y])
    for i in range(len(M)):
        M[i] = np.dot(M[i], R) + X

    return M

def plot_convex_hull(points, hull, squares):
    import matplotlib.pyplot as plt
    # add the first point to the end of the list
    hull.append(hull[0])
    for square in squares:
        square.append(square[0])
    # plot all the points, and draw a transparent polygon around the hull
    plt.scatter(*zip(*points))
    plt.plot(*zip(*hull))
    plt.fill(*zip(*hull), alpha=0.2)
    for square in squares:
        plt.plot(*zip(*square))
    plt.show()


def main():
    results = []
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        coords = []
        areas = []
        squares = []
        for _ in range(n):
          x,y,w,h,v = list(map(float,input().split()))
          square = get_coords(x,y,w,h,v)
          coords.extend(square)
          squares.append(square)
          # coords.append(get_coords(x,y,w,h,v))
          areas.append(w*h)

        convex = find_convex_hull(coords)
        plot_convex_hull(coords, convex, squares)
        convex_a = area_convex(convex)
        s=  sum(areas)
        results.append(s/convex_a * 100)

    for r in results:
        print(f'{r:.1f}  %')


        
main()