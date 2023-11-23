import math
inputs = []
for _ in range(int(input())):
    inputs.append([int(x) for x in input().split()])
    

for inputl in inputs:
    r = inputl[0]
    n = inputl[1]
    degs = inputl[2]
    minutes = inputl[3]
    sec = inputl[4]
    angle = degs + minutes/60 + sec / 3600
    #print(angle)
    remangle = 360 - n*angle
    print(angle, remangle)
    print((max(remangle,angle)/360)*math.pi*(r**2))