num_of_temps = int(input())

temps = input()

temps_list = temps.split(' ')

temps_list = [int(temp) for temp in temps_list]

if len(temps_list) != num_of_temps:
    print('wrong number of temps')
    exit()

cold_temps_count = 0

for temp in temps_list:
    if temp < 0:
        cold_temps_count += 1

print(cold_temps_count)
