def solve(inputs):
  inputstr = ""
  for x in inputs:
    if x % 2 == 0:
      inputstr += "0"
    else:
      inputstr += "1"

  maxv = 0
  mem = set()
  def rec(s, curr):
    nonlocal maxv;
    maxv = max(maxv, curr)
    if s not in mem:
      for i in range(len(s)-1):
        if (s[i] == "0" and s[i+1] == "0") or (s[i] == "1" and s[i+1] == "1"):
          rec(s[:i]+s[i+2:], curr+2)
      mem.add(s)
  rec(inputstr, 0)
  print(len(inputs)-maxv)

input()
solve([int(x) for x in input().split()])
