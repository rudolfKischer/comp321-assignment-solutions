N = int(input())

def count_lucky_numbers(curr_num: int) -> int:
    num_digits = len(str(curr_num))
    if curr_num % num_digits != 0:
        return 0
    
    if num_digits == N:
        return 1
    curr_num *= 10
    count = 0
    
    start_digit = 1 if curr_num == 0 else 0
    
    for next_digit in range(start_digit, 10):
        count += count_lucky_numbers(curr_num + next_digit)
        
    return count

print(count_lucky_numbers(0))
