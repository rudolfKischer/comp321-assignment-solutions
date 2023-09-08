bit_flips = int(input())

init_data = input()
final_data = input()

def flip_bits(bit_s):
    bit_length = len(bit_s)
    mask = ((1 << bit_length) - 1)
    return bin(~int(bit_s, 2) & mask)[2:].rjust(bit_length, '0') 

if (bit_flips % 2) == 1:
    init_data = flip_bits(init_data)
    
if  init_data == final_data:
    print("Deletion succeeded")
else:
    print("Deletion failed")



