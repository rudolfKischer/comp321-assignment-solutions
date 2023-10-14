
def get_input():
    n = int(input())
    return n

def get_bombs(n):
    return (n-2) if n >= 3 else 1
        
print(get_bombs(get_input()))
    