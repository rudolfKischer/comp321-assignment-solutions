from random import randint
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_eos = False

class PrefixTrie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,s):
        curr_root = self.root
        for c in s:
            if c not in curr_root.children:
                curr_root.children[c] = TrieNode()
            
            curr_root = curr_root.children[c]

            if curr_root.is_eos:
                return True
            
        curr_root.is_eos = True
        return False

def generate_phone_numbers(n):
    return ["".join([str(randint(0,9)) for _ in range(10)]) for _ in range(n)]

def main():
    n = int(input())
    results = []
    for _ in range(n):
        numbers = int(input())
        t = PrefixTrie()
        f = False
        for i in range(numbers):
            f = t.insert(input())
            if f:
                break
        results.append(f)
    for r in results:
        if r:
            print("NO")
        else:
            print("YES")
main()
#test()
    

                