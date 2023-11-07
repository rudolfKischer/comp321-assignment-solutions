from collections import defaultdict
s = input()
d = defaultdict(int)
for c in s:
    d[c]+=1
numodds = 0
for v in d.values():
    if v % 2 != 0:
        numodds += 1
if numodds == 0:
    print(0)
else:
    print(numodds-1)