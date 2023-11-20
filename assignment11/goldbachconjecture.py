

# Gold bachs conjecture
# need to find a a unique way to represent a given even number as the sum of two prime numbers

# primes are greter than 1

# every number greater than 2 can be written as sum of primes

# n = number of cases
# each line contains a test case
# x = even numbers between [4, 32000]

# give the number of ways the number can be represented as two primes 
# then list the representaitons

#ex
#4 has 1 representaiton(s)
# 2+2

#26 has 3 representations(s)
#3+23
#7+19
#13+13

# What do we know about the primes it can be?
# well we know that they have to be less than the x
# let q and p be our primes, then we have
# x = p + q
#
# this means we have
# q = x-p

# so given p we can find q

# what we can do is get p_1 to p_k , where k < n
# so that is all the prime numbers up to n

# we can use the sive of erostetenes to generate primes up to n
# O(sqrt(n) log log n)

# then we can go through each p_i, and fing the matching q_i
# if q_i is in our primes , then it is a valid combination
# note we only have to do this for all p_i less than x/2


def get_input():
    n = int(input())

    X = [ int(input()) for _ in range(n) ]

    return X

def print_output(x, P_Q):
    
    out_str = f'{x} has {len(P_Q)} representation(s)'
    print(out_str)

    for p,q in P_Q:
        print(f'{p}+{q}')
    print()

def primes(n):
    # sieve of eratosthenes
    # - make an array up to n, with TF values, prime or not prime
    # - set 0 and 1 to be not prime
    # - keep 2 as prime, mark all multiples of 2 as not prime
    # - go to next k that is prime, mark all K multiples as not prime
    
    # - we can start at k^2 because  multiple of 1 - (k-1) will have already be crossed out
    primes =[]
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    k = 2

    while k < (n+1):
        # if its not a prime we just go to the next
        if not is_prime[k]:
            k +=1
            continue
        
        j = k * k 
        while j < (n+1):
            is_prime[j] = False
            j += k
        primes.append(k)
        k += 1
    
    return primes

def get_representations(x):
    x_primes = primes(x)
    x_primes = set(x_primes)
    representations = []

    for p in x_primes:
        if p > (x / 2.0):
            break
        q = x - p
        if q in x_primes:
            representations.append((p,q))

    return representations
        

X = get_input()

for x in X:
    print_output(x, get_representations(x))
    
    



