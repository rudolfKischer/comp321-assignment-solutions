import numpy as np


def calculate_distance(commands):
    position = np.array([0.0,0.0], dtype=float)
    angle = 0.0

    actions = {
        'fd': lambda position, angle, value: (position + value * np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))]), angle),
        'bk': lambda position, angle, value: (position - value * np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))]), angle),
        'lt': lambda position, angle, value: (position, angle + value),
        'rt': lambda position, angle, value: (position, angle - value)
    }

    for command in commands:
        # print(f'position: {position}, angle: {angle}')
        action, value = command.split()
        value = float(value)
        position, angle = actions[action](position, angle, value)

    return round(np.linalg.norm(position))

def get_input():
    test_cases = []
    n = input()
    n = int(n)
    for i in range(n):
        m = int(input())
        commands = [ input() for _ in range(m) ]
        
        test_cases.append(commands)
    return test_cases

test_cases = get_input()

for test_case in test_cases:
    print(calculate_distance(test_case))