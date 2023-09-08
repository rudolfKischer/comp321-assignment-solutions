num_cases = int(input())

def decode_alpha(alpha):
    if alpha == ' ':
      return '0'
    alpha_lower = alpha.lower()
    ascii_num = ord(alpha_lower)
    alpha_num = ascii_num - 97
    if alpha_num < 15:
        return str(alpha_num // 3 + 2) * ((alpha_num % 3) + 1)
    elif alpha_num < 19:
        return str(7) * ((alpha_num - 15) + 1)
    elif alpha_num < 22:
        return str(8) * ((alpha_num - 19) + 1)
    else: 
        return str(9) * ((alpha_num - 22) + 1)

def decode_string(string):
    string_builder = ''
    for i in range(0, len(string)):
        decoded_char = decode_alpha(string[i])
        if i > 0 and string_builder[-1] == decoded_char[0]:
            string_builder += ' '
        string_builder += decoded_char
    return string_builder

result_strings = []

for i in range(0,num_cases):
    text = input()
    decoded_numbers = decode_string(text)
    result_strings.append(f'Case #{i + 1}: {decoded_numbers}')

for result in result_strings:
    print(result)