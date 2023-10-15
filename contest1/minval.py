import math
ints = ["9","9","9"]
def solve():
    ans = math.inf
    opps = ["+","-","*","/"]
    def rec(rem, curr):
        nonlocal ans
        if len(rem) == 1:
            for op in opps:
                if op == "/" and curr/int(rem[0])%1!=0:
                    continue
                v = eval(str(curr)+op+rem[0])
                if v>=0:
                    ans = min(int(v),ans)
        else:
            for op in opps:
                if op == "/" and curr/int(rem[0])%1!=0:
                    continue
                rec(rem[1:], eval(str(curr)+op+rem[0]))
    rec(ints[1:],int(ints[0]))
    print(ans)
solve()
'''def solve():
    ans = math.inf
    opps = ["+","-","*","/"]
    def rec(rem, currstr):
        nonlocal ans
        if len(rem)==1:
            for op in opps:
                #print(op, currstr[-1],int(rem[0]))
                if op == "/" and ((int(currstr[-2])/int(rem[0]))%1!=0 or (eval(currstr)/int(rem[0])%1!=0)):
                    continue
                v = eval(currstr+op+rem[0])
                if v>=0:
                    ans = int(min(v, ans))
        else:
            for op in opps:
                if op == "/" and (int(currstr)/int(rem[0]))%1!=0:
                    continue
                rec(rem[1:], "("+currstr+op+rem[0]+")")
    rec(ints[1:], ints[0])
    print(ans)
solve()
         '''   
            


    