num_of_lines = int(input())


lines = []

for i in range(0, num_of_lines):
    lines.append(input())

for line in lines:
    chars = [0] * 26

    for char in line:
        if char.isalpha():
            char = char.lower()
            ascii_code = ord(char) 
            alpha_position = ascii_code - 97
            chars[alpha_position] = 1
    
    pangram = all([char == 1 for char in chars])

    if pangram:
        print('pangram')
    else:
        chars_missed = ''
        for i in range(0,len(chars)):
            if chars[i] == 0:
                ascii_char = chr(i + 97)
                chars_missed += ascii_char
        print(f'missing {chars_missed}')

                


            

