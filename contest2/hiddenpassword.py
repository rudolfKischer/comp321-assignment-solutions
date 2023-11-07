from collections import defaultdict
inputl = input().split()
pw = inputl[0]
message = inputl[1]

s = set()
added = set()
d = defaultdict(int)
for c in pw:
    s.add(c)
    d[c] +=1
newmessage = ""
for c in message:
    if c in s and c not in added:
        newmessage += c
        if d[c] <= 1: 
            added.add(c)
        d[c]-=1
if newmessage == pw:
    print("PASS")
else:
    print("FAIL")


