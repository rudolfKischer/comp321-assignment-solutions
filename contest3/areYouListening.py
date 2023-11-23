import numpy as np

def get_input():
    cx, cy, n = map(int, input().split())

    circles = [list(map(int, input().split())) for i in range(n)]

    return [cx,cy], circles

def get_distances(pos, circles):
    cx, cy = pos
    
    circle_dists = []
    for circle in circles:
        x = circle[0]
        y = circle[1]
        r = circle[2]

        dist = int(np.sqrt((x-cx)**2 + (y-cy)**2))

        circle_dists.append(dist - r)    
    return circle_dists

def get_largest_dist():
    dists_rads = get_distances(*get_input())
    
    dists_rads_sorted_by_dist = sorted(dists_rads)

    print(max(dists_rads_sorted_by_dist[2], 0))


    



get_largest_dist()