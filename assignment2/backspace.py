input_chars = input()

char_stack = []

def process_chars(chars):

  for char in chars:
    if char == '<' and len(char_stack) > 0:
      char_stack.pop()
    else:
      char_stack.append(char)
  
  return ''.join(char_stack)

print(process_chars(input_chars))