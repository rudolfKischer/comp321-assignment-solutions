s = input()
curr = 1
for c in s:
    if c =="A":
        if curr == 1:
            curr = 2
        elif curr == 2:
            curr = 1
    elif c == "B":
        if curr == 2:
            curr = 3
        elif curr == 3:
            curr = 2
    elif c == "C":
        if curr == 1:
            curr = 3
        elif curr == 3:
            curr = 1
print(curr)