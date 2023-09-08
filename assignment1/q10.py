


def get_runs(bus_numbers_sorted):
    runs = []
    current_run = []
    for num in bus_numbers_sorted:
        if len(current_run) == 0 or int(num) == (int(current_run[-1]) + 1):
            current_run.append(num)
            continue
        runs.append(current_run)
        current_run = []
        current_run.append(num)
    runs.append(current_run)
    return runs

def get_bus_num_str(bus_numbers_str):
    bus_nums_list = sorted(bus_numbers_str.split(' '), key=int)
    runs = get_runs(bus_nums_list)
    bus_nums_strings = []
    for run in runs:
        if len(run) <= 2:
            bus_nums_strings.append(' '.join(run))
        else:
            bus_nums_strings.append(f'{run[0]}-{run[-1]}')

    bus_num_string = ' '.join(bus_nums_strings)
    return bus_num_string

num_length = input()
bus_numbers_str = input()
print(get_bus_num_str(bus_numbers_str))

