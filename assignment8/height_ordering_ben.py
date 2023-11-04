def sort_and_count(kids: list) -> int:
    steps = 0

    for i in range(1, len(kids)):
        key = kids[i]
        j = i - 1
        while j >= 0 and kids[j] > key:
            kids[j + 1] = kids[j]
            j -= 1
            steps += 1
        kids[j + 1] = key

    return steps


def main():
    P = int(input())
    data_sets = [list(map(int, input().split())) for _ in range(P)]
    results = [(d[0],sort_and_count(d[1:])) for d in data_sets]
    for r in results:
        print(f"{r[0]} {r[1]}")

main()



