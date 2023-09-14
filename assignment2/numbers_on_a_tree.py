


def get_node_number(path):
    if len(path) == 0:
        return 1
    
    L_R = int(path.pop() == 'R')
    return  2 * get_node_number(path) + L_R

def get_num_nodes(h):
    return 2**(h+1)
    
def get_input():
    input_list = input().split(' ')
    h = int(input_list[0])
    path = []
    if len(input_list) > 1:
        path = list(input_list[1])
    return h, path

def get_node_label(h, path):
    return get_num_nodes(h) - get_node_number(path)

print(get_node_label(*get_input()))

