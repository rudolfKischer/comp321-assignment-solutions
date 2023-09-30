
# row of n squares
# to jump forward, it must be +1 to the prev jump
# to jump nback, it must be exact same
# first jump is from square 1 to square 2

def get_input():
    return [input() for _ in range(int(input()))]

def get_cost(squares, []):
    
    max_num = nums[-1]
    start = 0
    for i in range(1,max_num+1):
        
    
    


def get_cheapest_jumps(squares, position):
    

    for i in range(0,position):
        get
    
    
    




# def get_cheapest_jumps(squares, position):
#     if position == 0:
#         return 0, 0 # cost, length of last jump
#     if position == 1:
#         return 1, 1 # cost, length of last Jump
    
#     cheapest_jumps = [get_cheapest_jumps(squares,i) for i in range(0,position)]

#     for i in range(0,position):
#         if cheapest_jumps[i] != 


#     return 
    
    
#     return min()

    
    

    

    
def brute_force(squares, position, last_jump_length, num_jumps, cost, path):
    
    # if num_jumps > 4:
    #     return float('inf')
    # print(f'({position},{last_jump_length},{num_jumps})')
    cost = cost + int(squares[position])
    path.append(position)
    print(path)
    if position == len(squares):
        return cost
    
    if position == 0 and num_jumps ==0:
        return brute_force(squares, position+1, 1, num_jumps+1, cost,path)
    
    backwards = float('inf')
    forward = float('inf')

    if position + (last_jump_length + 1) < len(squares):
        forward = brute_force(squares, position + last_jump_length + 1,last_jump_length + 1, num_jumps+1, cost, path)
    if position - last_jump_length >= 0:
        backwards = brute_force(squares, position - last_jump_length,last_jump_length, num_jumps+1, cost,path )

    
    return min(backwards,forward)

    


squares = get_input()

print(brute_force(squares, 0, 0, 0, 0, []))
