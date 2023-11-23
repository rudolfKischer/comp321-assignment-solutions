import math
k = int(input())
sqrt = int(math.sqrt(k))+1
sieve = [1 for _ in range(sqrt+1)]
primeslessthanrootk = []
for i in range(2, sqrt):
  if sieve[i] == 1:
    primeslessthanrootk.append(i)
    for j in range(i*2, sqrt, i):
      sieve[j] = 0

bestsofar = 0
bestcount = -1
for p in primeslessthanrootk:
  curr = str(int(str(k), p))
  currcount = 0
  for i in range(len(curr)-1,-1,-1):
    if curr[i] == "0":
      currcount += 1
  if currcount>bestcount:
    bestcount = currcount
    bestsofar = p

