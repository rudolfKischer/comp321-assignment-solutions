inputarr = ['abcd', 'aaaa', 'ababab', '.']
count = 0
while True:
    inputl = inputarr[count].strip()
    count+=1
    if inputl == ".":
        break
    l = len(inputl)
    for i in range(1,len(inputl)+1):
        if l % i != 0:
            continue
        else:
            factor = l // i
            if (inputl[:i])*factor == inputl:
                print(factor)
                break