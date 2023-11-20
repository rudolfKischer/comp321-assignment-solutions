
from cgi import test

from queue import Queue


test_cases = []

num_of_test_cases = int(input())
for i in range(num_of_test_cases):
    n_t = [int(j) for j in input().split()]
    n = n_t[0]
    t = n_t[1]
    buttons = [int(k) for k in input().split()]
    test_cases.append([n,t,buttons])

print(test_cases)



for test_case in test_cases:
    n = test_case[0]
    t = test_case[1]
    buttons = test_case[2]

    # perform bfs until we find the the button time
    # cant got above 3600 or below 0

    search_queue = Queue()

    search_queue.put((0,0))

    closest_time = 0
    closest_time_button_presses = 0
    solved = False

    while not search_queue.empty():
        curr_time, curr_button = search_queue.get()
        if curr_time == t:
            print(test_case)
            print(curr_button, 0)
            solved = True
            break
        if (abs(t - curr_time) < abs(t - closest_time)): #or (abs(t - curr_time) == abs(t - closest_time) and curr_button < closest_time_button_presses):
            closest_time = curr_time
            closest_time_button_presses = curr_button
        if curr_time > 3600 or curr_time < 0:
            continue
        for button in buttons:
            if curr_time + button <= 3600 and curr_time + button >= 0:
                search_queue.put((curr_time + button, curr_button + 1))
    if solved:
        continue
    
    print(test_case)
    print(closest_time_button_presses, abs(t - closest_time))





