


n, a, b =  tuple([int(i) for i in input().split()])

days = [ int(input()) for i in range(n-1)]

def get_missing(days): 
    
    if not (b in days) and not (a in days):
       print(-1)
       return
    
    if not (a in days):
      print(a)
      return
    
    if not (b in days):
      print(b)
      return
        
    for i in range(a,b+1):
        print(i)

get_missing(days)
    

        
   
