w = [int(x) for x in input().split()][0]
divs = [0] + [int(x) for x in input().split()] + [w]

s = set()
for i in range(len(divs)):
  for j in range(i+1, len(divs)):
    s.add(divs[j] - divs[i])

print(" ".join([str(x) for x in sorted(list(s))]))

