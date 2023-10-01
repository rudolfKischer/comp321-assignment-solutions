n, lph = tuple([int(i) for i in input().split()])

problems = [int(input()) for i in range(n)]



problems.sort()
hrs = 5

tot = 0
count = 0

max_val = lph * hrs

for i in problems:
    if (tot + i) > max_val:
        break

    tot += i
    count += 1

print(count)

 
