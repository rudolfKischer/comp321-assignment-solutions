numrooms = 4
numstudentsraw = [2, 3, 3, 1]
numstudents = sorted(numstudentsraw)[::-1]

firstroomrem = numstudents[0]
currinpile = numstudents[0]
Lflag = False
for i in range(1,numrooms):
    if currinpile < numstudents[i]:
        print("impossible")
        Lflag = True
    firstroomrem -= numstudents[i]
    currinpile += numstudents[i]
    
if not Lflag and (firstroomrem > 0 or currinpile < numstudents[0]):
    print("impossible")
else:
    #print rooms
    roomorder = []
    blacklist = set()
    for n in numstudents:
        for i in range(len(numstudentsraw)):
            if i in blacklist:
                continue
            if numstudentsraw[i] == n:
                roomorder.append(i+1)
                blacklist.add(i)
    print(roomorder)
        
