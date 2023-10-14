

def get_input():
    num_of_cases = int(input())
    cases = []
    for i in range(num_of_cases):
        n = input()
        case = []
        for _ in range(2):
            vec = list(map(int,input().split()))
            case.append(vec)
        cases.append(case)
    return cases


def get_min_product(case):
    vec1 = case[0]
    vec2 = case[1]

    vec1.sort()
    vec1.reverse()
    vec2.sort()

    return sum([a*b for a, b in zip(vec1, vec2)])

def get_min_products(cases):
    return list(map(get_min_product, cases))

def print_min_products(min_products):
    for i in range(len(min_products)):
        print(f"Case #{i + 1}: {min_products[i]}")
    

print_min_products(get_min_products(get_input()))




