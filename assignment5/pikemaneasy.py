def main():
    '''
    n: # of problems in contest
    length: total length of contest in mins
    t_0: time in minutes required to solve first problem
    time for remaining t1,...,tn times:
    t_i = ((a*t_(i-1) + b) mod c) + 1, i in [1,N-1]
    '''
    n,length = list(map(int,input().split()))
    a,b,c,t0 = list(map(int,input().split()))
    penalty  = t0
    problems = 1  # Since the first problem is always solved
    times = [0]*n
    times[0] = t0
    for i in range(1,n):
        times[i] = (((a * times[i-1]+b) % c) + 1)
    times = sorted(times)
    for i in range(1,len(times)):
        t = times[i]
        if penalty + t <= length:
            problems += 1
            penalty += t
        else:
            break
    print(f"{problems} {penalty % (10**9 + 7)}")
    
main()