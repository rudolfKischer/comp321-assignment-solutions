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

count = 0
for p in primeslessthanrootk:
  while k % p == 0:
    k = k // p
    count+=1

if k == 1:
  print(count)
else:
  print(count+1)

