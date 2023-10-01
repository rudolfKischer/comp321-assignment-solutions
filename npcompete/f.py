
vowels = "aeiou"
vowels_y = "aeiouy"

line = input()
print(sum([ (c in vowels) for c in line]), sum([ (c in vowels_y) for c in line]))

