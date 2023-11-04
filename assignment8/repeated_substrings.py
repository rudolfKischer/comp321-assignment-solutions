def sort_cyclic_shifts(s):
    n = len(s)
    alphabet = 256
    p = [0] * n 
    c = [0] * n  
    cnt = [0] * max(alphabet, n)
    
    for i in range(n):
        cnt[ord(s[i])] += 1
    for i in range(1, alphabet):
        cnt[i] += cnt[i-1]
    for i in range(n):
        p[cnt[ord(s[i])]-1] = i
        cnt[ord(s[i])] -= 1
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1
    
    pn = [0] * n
    cn = [0] * n
    h = 0
    while (1 << h) < n:
        for i in range(n):
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0:
                pn[i] += n
        for i in range(classes):
            cnt[i] = 0
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1):
            p[cnt[c[pn[i]]]-1] = pn[i]
            cnt[c[pn[i]]] -= 1
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1 << h)) % n])
            if cur != prev:
                classes += 1
            cn[p[i]] = classes - 1
        c, cn = cn, c
        h += 1

    return p

def build_suffix_array(s):
    s += "$"
    sorted_shifts = sort_cyclic_shifts(s)
    return sorted_shifts[1:]

def build_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n-1)
    for i in range(n):
        rank[sa[i]] = i
    k = 0
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = sa[rank[i]+1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return lcp

def count_unique_repeated_substrings(s):
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)
    return sum(max(0, x - y) for x, y in zip(lcp, lcp[1:] + [0]))

def main():
    k = int(input())
    results = []
    for _ in range(k):
        s = input().strip()
        results.append(count_unique_repeated_substrings(s))

    for r in results:
        print(r)

main()