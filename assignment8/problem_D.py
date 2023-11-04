
import random
# Are given n strings
# if the string can be represented as one of its subtrings repeated k times then it is pattern representable
# if the string is not pattern representable, print 0
# Otherwise, print the smallest k


# For this problem, you are going to look for cases where a long input string consists of a repeated pattern. 
# We say string s1 is a prefix of string s if there exists some (possibly empty) string s2 such that s is the concatenation of s1 and s2. 
# We say pattern p explains string s if s is a prefix of p x n for some sufficiently large n.



def is_pattern_representable(string):
  # for each i, repeat the substring up to i, until it is the length of the string or larger
  # then slice it and compare it to the string
  for i in range(1, len(string)):
    substring = string[:i]
    # divide and round up
    multiplier = len(string) // len(substring) + (len(string) % len(substring) > 0)
    # print(f"substring: {substring}, multiplier: {multiplier}")

    p_n = (substring * multiplier)[:len(string)]
    # print(f"{p_n}")
    # print(f"{string}")
    # print()
    if p_n == string:
      return i
  return 0


def main():
  n = int(input())
  strings = [input() for i in range(n)]
  for string in strings:
    print(is_pattern_representable(string))

main()



def get_test_strings():
    # 200 test cases
    # each string is 70 printable  asciie characters

    #generate test cases by 
    # pick a random number between 1 and 70
    # generate a random string of that length
    # repeat that string a until it is 70 characters long
    # slice it to 70 characters

    test_cases = []

    for i in range(200):
        length = random.randint(1, 70)
        # only use alphabet characters
        new_string = "".join([chr(random.randint(97, 122)) for i in range(length)])

        multiplier = 70 // length + (70 % length > 0)
        new_string = (new_string * multiplier)[:70]
        test_cases.append(new_string)
    
    return test_cases

# for string in get_test_strings():
#     # print(string)
#     print(is_pattern_representable(string))