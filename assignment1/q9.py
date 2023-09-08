

def pad_message(message, key):
    key_length = len(key)
    message_length = len(message)
    new_message_length = -int( -message_length // key_length ) * key_length # ceil the qoutient
    message += ' ' * (new_message_length - message_length)
    return message

def decrypt_message(message, key):
    message = pad_message(message, key)
    decoded_message = [''] * len(message)

    for i in range(0, len(message)):
        key_len = len(key)
        new_pos = (int(key[i % key_len]) - 1) + (i // key_len * key_len)
        decoded_message[i] = message[new_pos]
    
    return ''.join(decoded_message)

inputs = []

while True:
    key_string = input()
    key = key_string.split(" ")
    if int(key[0]) == 0:
        break
    message = input()
    inputs.append((message, key))

for message, key in inputs:
    key = key[1:]
    result = decrypt_message(message, key)
    print('\''+result+'\'')

    

    