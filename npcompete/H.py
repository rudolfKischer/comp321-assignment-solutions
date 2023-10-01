

m, max_pill, max_pill_day = tuple([int(i) for i in input().split()])



picos = []

numbers = list(range(1, (min(max_pill,m)//2 + 1)+1))
if m <= max_pill:
   numbers.append(m)

for i in numbers:
  if m % i == 0:
      pills_per_day = m / i
      if pills_per_day <= max_pill_day:
          picos.append(i)

print(len(picos))
a = [print(x) for x in picos]
      

