
end_token = '$'

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class SuffixTree:

    def __init__(self):
        self.root = SuffixTreeNode()

    def insert(self,s):
        # Check if s is prefix of any other string before inserting
        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = SuffixTreeNode()
            curr = curr.children[c]
            if curr.is_end:
                return True
            
        curr.children[end_token] = SuffixTreeNode()
        curr.is_end = True
        return False
        

    



def main():
    n = int(input())
    results = []
    for _ in range(n):
        numbers = int(input())
        t = SuffixTree()
        f = False
        for i in range(numbers):
            f = t.insert(input())
            if f:
                break
        results.append(f)
    for r in results:
        print("NO") if r else print("YES")

main()
    

                