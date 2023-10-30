def compare_dna(dna1, dna2):
    # Just counting differences
    return sum(a != b for a, b in zip(dna1, dna2))

def find_parent(node, parents):
    # Find the leader of the pack
    if node != parents[node]:
        parents[node] = find_parent(parents[node], parents)
    return parents[node]

def merge_sets(u, v, parents, ranks):
    parentU = find_parent(u, parents)
    parentV = find_parent(v, parents)
    if parentU != parentV:
        if ranks[parentU] < ranks[parentV]:
            parentU, parentV = parentV, parentU
        parents[parentV] = parentU
        if ranks[parentU] == ranks[parentV]:
            ranks[parentU] += 1

def build_tree(num, sequences):
    edges = []
    for i in range(num):
        for j in range(i+1, num):
            diff = compare_dna(sequences[i], sequences[j])
            edges.append((diff, i, j))
    edges.sort()

    parents = [i for i in range(num)]
    ranks = [0] * num
    tree = []
    total_diff = 0
    for diff, first, second in edges:
        if find_parent(first, parents) != find_parent(second, parents):
            merge_sets(first, second, parents, ranks)
            tree.append((first, second))
            total_diff += diff

    return total_diff, tree

# Grabbing the numbers and sequences
samples, length = map(int, input().split())
sequences = [input().strip() for _ in range(samples)]

diff_value, tree = build_tree(samples, sequences)
print(diff_value)
for start, end in tree:
    print(start, end)
