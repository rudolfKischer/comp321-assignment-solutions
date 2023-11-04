# string sort on first two ;etters
# 500 test cases
# Each test case can have up to 200 strings
# one name per line
# names have 2 - 20 characters
# input ends when an input line has n =0

# output the names sorted by the first two characters in ascending order
# sort by ascii comparison, case sensitive
# if two names have the same first two letters, maintain the original order


def sort_names(names):
  func = lambda x: x[:2]
  return sorted(names, key=func)

solutions = []
n = int(input())
while n != 0:
  names = [input() for i in range(n)]
  solutions.append(sort_names(names))
  n = int(input())

for solution in solutions:
  print("\n".join(solution))
  print()