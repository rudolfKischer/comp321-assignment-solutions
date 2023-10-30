def find_scariest_movie(N, H, L, horrors, pairs):
    HI = [float('inf')] * N

    for h in horrors:
        HI[h] = 0

    changes = True
    while changes:
        changes = False
        for x, y in pairs:
            if HI[x] > HI[y] + 1:
                HI[x] = HI[y] + 1
                changes = True
            elif HI[y] > HI[x] + 1:
                HI[y] = HI[x] + 1
                changes = True

    return HI.index(max(HI))

N, H, L = map(int, input().split())
horrors = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(L)]

print(find_scariest_movie(N, H, L, horrors, pairs))
