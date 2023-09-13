


from pprint import pprint

import random
import string

class UnionFind():
    
    def __init__(self):
        self.uf = {}

    def get_set_size(self, e):
        parent = self.find(e)
        return self.uf[parent]['size']
    
    def find(self, e):
        element = self.uf.get(e)
        if not element:
            self.uf[e] = {
                'parent': e,
                'size': 1
            }
        parent = self.uf[e]['parent']
        if parent != e:
            self.uf[e]['parent'] = self.find(parent)
        return self.uf[e]['parent']
    
    def union(self, e1, e2):
        e1_parent = self.find(e1)
        e2_parent = self.find(e2)
        if e1_parent != e2_parent:
            self.uf[e2_parent]['parent'] = e1_parent
            self.uf[e1_parent]['size'] += self.uf[e2_parent]['size']

def get_network_sizes(test_case):
    sizes = []
    uf = UnionFind()
    
    for relationship in test_case:
        uf.union(*relationship)
        sizes.append(uf.get_set_size(relationship[0]))
    
    return sizes

def get_relationships(num_relationships):
    relationships = []
    for _ in range(0,num_relationships):
        relationship_str = input()
        relationship_pair = relationship_str.split(' ')
        relationships.append(relationship_pair)
    return relationships


def get_test_cases(num_test_cases):
    test_cases = []
    for i in range(0, num_test_cases):
        num_relationships = int(input())
        test_case = get_relationships(num_relationships)
        test_cases.append(test_case)
    return test_cases

test_cases = get_test_cases(int(input()))


for test_case in test_cases:
    sizes = get_network_sizes(test_case)
    for size in sizes:
        print(size)



# Union Find
# can consider each network as a unique set
# if there is a relationship between two networks then we union them
# once we have done this for all relation ships
# we use the find operation to get the size of the group



# def get_network_size(network, person):
#     discovered = set()

#     discovery_queue = []

#     discovery_queue.append(person)

#     while len(discovery_queue) > 0:
#         current_person = discovery_queue.pop()
#         discovered.add(current_person)
#         friends = network[current_person]
#         for friend in friends:
#             if friend not in discovered:
#                 discovery_queue.append(friend)
    
#     return len(discovered)
            

# def add_relationship_to_network(relationship, friend_network):
#     alice, bob = relationship

#     #bob
#     bob_friends = friend_network.get(bob, set())
#     bob_friends.add(alice)
#     friend_network[bob] = bob_friends

#     #alice
#     alice_friends = friend_network.get(alice, set())
#     alice_friends.add(bob)
#     friend_network[alice] = alice_friends

#     return friend_network
    

# def get_friend_network(relationships):
#     friend_network = {}
#     for relationship  in relationships:
#         friend_network = add_relationship_to_network(relationship, friend_network)
#         # pprint(friend_network)
#         net_size = get_network_size(friend_network, relationship[0])
#         print(net_size)
#     return friend_network

def random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 6)))

def generate_test_case(max_friends, max_friendships, max_cases):
    # Maximum sum of F values across all test cases
    MAX_SUM_F = 100000

    # Create a pool of max_friends names
    all_names = set()
    while len(all_names) < max_friends:
        all_names.add(random_name())
    all_names = list(all_names)

    # Number of test cases
    t = random.randint(1, max_cases)
    print(t)

    total_f = 0
    for _ in range(t):
        # Ensure we don't exceed MAX_SUM_F
        if total_f >= MAX_SUM_F:
            break

        # Number of friendships
        n = min(random.randint(1, max_friendships), MAX_SUM_F - total_f)
        total_f += n
        print(n)

        friendships = set()
        for _ in range(n):
            while True:
                name1 = random.choice(all_names)
                name2 = random.choice(all_names)
                if name1 != name2 and (name1, name2) not in friendships and (name2, name1) not in friendships:
                    break
            friendships.add((name1, name2))
            print(name1, name2)



# generate_test_case(5,10, 100)