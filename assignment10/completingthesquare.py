import math
corners = []
for _ in range(3):
    corners.append(tuple(map(int,input().split())))

def find_reflection_point(a: tuple,b: tuple, c: tuple):
    if (a[0] - b[0]) == 0:
        # reflected across the x axis
        print(f"{a[0] + (a[0] - c[0])} {c[1]}")
        return
    A = (a[1]-b[1])/(a[0] - b[0])
    B = -1
    C = b[1] - A*b[0]
    line = 2*(A*c[0] + B*c[1] + C)/(A**2 + B**2)
    print(f"{round(c[0] - A*line)} {round(c[1] - B*line)}")
    
A = abs(math.dist(corners[0],corners[1]))
B = abs(math.dist(corners[0],corners[2]))
C = abs(math.dist(corners[1],corners[2]))
h = max(A,B,C)
if A == h:
    find_reflection_point(corners[0],corners[1],corners[2])

elif B == h:
   find_reflection_point(corners[0],corners[2],corners[1])

else:
   find_reflection_point(corners[1],corners[2],corners[0])






