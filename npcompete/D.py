import math

n, r, w, h = tuple([int(i) for i in input().split()])
x, y, v = [], [], []

for i in range(n):
  nLine = input().split()
  x.append(int(nLine[0]))
  y.append(int(nLine[1]))
  v.append(int(nLine[2]))

value = 0
for i in range(len(x)):
  if x[i] - r > 0 and y[i] - r > 0 and x[i] + r < w and y[i] + r < h:
    area = r**2 * math.pi
  
  elif x[i] - r <= 0:
    area = 1/2 * r**2 * math.pi + math.asin(x[i]/r) + x[i] * (1-x[i]**2)**(1/2)
  elif y[i] - r <= 0:
    area = 1/2 * r**2 * math.pi + math.asin(y[i]/r) + y[i] * (1-y[i]**2)**(1/2)
  
  elif x[i] >= w:
    area = 1/2 * r**2 * math.pi + math.asin((w-x[i])/r) + (w-x[i])*(1-(w-x[i])**2)**(1/2)
  elif y[i] >= h:
    area = 1/2 * r**2 * math.pi + math.asin((h-y[i])/r) + (h-y[i])*(1-(h-y[i])**2)**(1/2)

  avgValue = area * v[i] / (w*h)
  value += avgValue

print(value)

