d = {}
while True:
    s = input()
    if s=="***":
        break
    else:
        if s in d:
            d[s]+=1
        else:
            d[s] = 1

maxvotes = -1
maxname = None
isTie = False
for k,v in d.items():
    if v>maxvotes:
        maxname = k
        maxvotes = v
        isTie = False
    elif v == maxvotes:
        isTie = True
if isTie:
    print("Runoff!")
else:
    print(maxname)