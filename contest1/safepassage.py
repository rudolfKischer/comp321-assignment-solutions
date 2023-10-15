import math
def solve():
    left = sorted([1,2,7,10])
    right = []
    mem = {}
    ans = math.inf
    def rec(left, right, currtime,go):
        print(left, right, currtime)
        nonlocal ans
        if go==1:
            if len(left)==2:
                ans = min(ans, currtime+max(left))
                return
            for i in range(len(left)):
                for j in range(i+1, len(left)):
                    newleft = left.copy()
                    newright = right.copy()
                    p1 = newleft.pop(j)
                    p2 = newleft.pop(i)
                    newright.append(p1)
                    newright.append(p2)
                    rec(newleft,newright,currtime+max(p1,p2),go*(-1))
        else:
            for i in range(len(right)):
                newleft = left.copy()
                newright = right.copy()
                p1 = newright.pop()
                newleft.append(p1)
                rec(newleft, newright, currtime+p1,go*(-1))
    rec(left, right, 0, 1)
    print(ans)
                
solve()

    
    
