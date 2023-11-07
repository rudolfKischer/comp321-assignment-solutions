from statistics import median


s = "abccabbcaabc"
l = len(s)
for i in range(1,l+1):
    if l % i != 0:
        continue
    currs = s[:i]
    currindex = i
    flag = True
    for j in range(1, (l // i)):
        currs = currs[-1] + currs[:-1]
        if s[currindex:currindex+i] != currs:
            flag = False
            break
        currindex += i
    if flag:
        print(i)
        break

