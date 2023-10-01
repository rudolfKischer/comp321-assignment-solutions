def get_input():
    n = input()
    
    trees = [ (int(i) + 1) for i in input().split()]
    return trees

def get_party(trees):
    trees.sort()
    trees.reverse()
    
    time = 0
    for i in range(len(trees)):
        addtional_time = trees[i] + i
        if addtional_time > time:
            time = addtional_time
    return time + 1



print(get_party(get_input()))
    
    
    



