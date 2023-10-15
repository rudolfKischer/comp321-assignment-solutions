#rawinput = input().split()
rawinput = ["20","7"]
print('starting')
d = {}
d[(1,2)] = 3
print(d[(1,2)])
n = int(rawinput[0])
k = int(rawinput[1])
dyn = [None for _ in range(n)]
dyn[0] = "N"
dyn[1] = "A"
for i in range(2,n):
    dyn[i] = dyn[i-2] + dyn[i-1]
for v in dyn:
    #print(v)
    x=2