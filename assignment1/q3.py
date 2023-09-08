samples_length = int(input())

sample_inputs = []

for i in range(0, samples_length):
    sample_input = int(input())
    sample_inputs.append(sample_input)

for sample_input in sample_inputs:
    remainder = sample_input % 2
    if remainder == 0:
        print(f'{sample_input} is even')
    else:
        print(f'{sample_input} is odd')