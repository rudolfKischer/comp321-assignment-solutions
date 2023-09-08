import random

digits_ascii = {
    0: [
        "***",
        "* *",
        "* *",
        "* *",
        "***"
    ],
    1: [
        "  *",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    2: [
        "***",
        "  *",
        "***",
        "*  ",
        "***"
    ],
    3: [
        "***",
        "  *",
        "***",
        "  *",
        "***"
    ],
    4: [
        "* *",
        "* *",
        "***",
        "  *",
        "  *"
    ],
    5: [
        "***",
        "*  ",
        "***",
        "  *",
        "***"
    ],
    6: [
        "***",
        "*  ",
        "***",
        "* *",
        "***"
    ],
    7: [
        "***",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    8: [
        "***",
        "* *",
        "***",
        "* *",
        "***"
    ],
    9: [
        "***",
        "* *",
        "***",
        "  *",
        "***"
    ]
}

digits = {tuple(value): key for key, value in digits_ascii.items()}

def read_code():
    lines = []
    for i in range(0,5):
        lines.append(input())
    return lines

def read_digit(lines):
    digit = []
    for i in range(0,len(lines)):
        digit.append(lines[i][0:3])
        if len(lines[i]) >= 3:
            lines[i] = lines[i][4:]
    return str(digits[tuple(digit)])

def print_lines(lines):
    for line in lines:
        print(line)

def check_safety(lines):
    digits = []
    boom = False
    while len(lines[0]) >= 3:
        try:
            digit = read_digit(lines)
        except KeyError:
            boom = True
            break
        digits.append(digit)
    digits = ''.join(digits)
    num = int(digits)

    if not boom and num % 6 == 0:
        return 'BEER!!'
    else:
        return 'BOOM!!'

def main():
    lines = read_code()
    response = check_safety(lines)
    print(response)
    

        
# main()

def make_num(num):
    num_str = str(num)
    lines = [[] for _ in range(5)]
    for char in num_str:
        ascii_num = digits_ascii[int(char)]
        for ascii_num_line, line in zip(ascii_num, lines):
            line.append(ascii_num_line)

    joined_lines = []
    for line in lines:
        joined_lines.append(' '.join(line))
    
    return joined_lines

def test(num):
    lines = make_num(num)
    # for line in lines:
    #     print(line)
    response = check_safety(lines)
    safe = num % 6 == 0

    if safe:
        return response == 'BEER!!'
    else:
        return response == 'BOOM!!'

def run_tests(test_length):
    failed = []
    for i in range(0,test_length):
        new_num = random.randint(0,10000000)
        result = test(new_num)
        # print()
        if not result:
            failed.append(new_num)
    return failed
        


        


    

        
num = int(input())

print(test(num))



    
     