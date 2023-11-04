


num_of_cases = int(input())


cases = [ [int(x) for x in input().split()][1::] for i in range(num_of_cases) ]


def insertion_sort_step_count(test_case):
    # perform insertion sort on case
    # count the number of steps
    # a step is an insertion

    steps = 0

    # need to handle the case that it is already sorted

    # sort in ascending order
    for i in range(1, len(test_case)):
        j = i
        while j > 0 and test_case[j] < test_case[j-1]:
            # swap
            test_case[j], test_case[j-1] = test_case[j-1], test_case[j]
            j -= 1
            steps += 1
    return steps

for i, case in enumerate(cases):
    print(f"{i + 1} {insertion_sort_step_count(case)}")