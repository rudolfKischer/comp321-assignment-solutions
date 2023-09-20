from sys import stdin
import bisect

def get_data():
    data = {}
    case_number = 0

    while True:
        # Try to read n, if unsuccessful, break out of the loop
        try:
            n = int(stdin.readline())
        except ValueError:
            break

        # Read the n numbers
        n_numbers = [int(stdin.readline()) for _ in range(n)]

        # Read m and then m queries
        m = int(stdin.readline())
        m_queries = [int(stdin.readline()) for _ in range(m)]

        # Store the data for this case
        data[case_number] = (n_numbers, m_queries)

        case_number += 1

    return data



def find_closest_sums(case_num, numbers, queries):
    numbers = sorted(numbers)
    print(f"Case {case_num+1}:")
    for q in queries:
        closest = float('inf')
        front_pointer = 0
        back_pointer = len(numbers) - 1

        while front_pointer < back_pointer:
            current_sum = numbers[front_pointer] + numbers[back_pointer]

            if abs(current_sum - q) < abs(closest - q):
                closest = current_sum

            if q == current_sum:
                closest = current_sum
                break

            if current_sum < q:
                front_pointer += 1
            else:
                back_pointer -= 1

        print(f'Closest sum to {q} is {closest}.')

def main():
    data = get_data()
    for key, value in data.items():
        numbers,queries = value[0],value[1]
        find_closest_sums(key, numbers, queries)

main()