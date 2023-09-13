from queue import PriorityQueue

class Stack():
    
    def __init__(self):
        self.stack = []

    def throw(self, x):
        self.stack.append(x)
    
    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

class Queue():
    
    def __init__(self):
        self.queue = []

    def throw(self, x):
        self.queue.insert(0,x)
    
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return None

class PQueue():
    def __init__(self):
        self.pq = PriorityQueue()

    def throw(self, x):
        self.pq.put(-x)
    
    def remove(self):
        if self.pq.qsize() > 0:
            return -self.pq.get()
        return None

def check_input_pair(input_pair, data_structures):
    
    mode = int(input_pair[0])
    val = int(input_pair[1])

    data_structures_to_remove = []
    
    for name, structure in data_structures.items():

        if mode == 1:
            structure.throw(val)
        
        if mode == 2:
            removed_val = structure.remove()
            if removed_val != val:
                data_structures_to_remove.append(name)
    
    for name in data_structures_to_remove:
        del data_structures[name]

        
def check_input_pairs(input_pairs):
    
    data_structures = {
        'queue': Queue(),
        'priority queue': PQueue(),
        'stack': Stack()
    }

    for pair in input_pairs:
        check_input_pair(pair, data_structures)
    
    if len(data_structures) == 1:
        data_structure = list(data_structures.items())[0][0]
        return data_structure
    
    if len(data_structures) > 1:
        return 'not sure'
    
    if len(data_structures) == 0:
        return 'impossible'

not_done = True

outputs = []

while not_done:
    try:
        input_length_string = input()
        if input_length_string == '':
            not_done = False
            break
        input_length = int(input_length_string)
    except EOFError:
        not_done = False
        break

    input_pairs = []

    for i in range(0, input_length):
        input_pair = input()
        input_pair = tuple(input_pair.split(' '))
        input_pairs.append(input_pair)

    result = check_input_pairs(input_pairs)

    outputs.append(result)

for output in outputs:
    print(output)

