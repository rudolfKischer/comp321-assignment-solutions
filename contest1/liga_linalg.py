import itertools
import random

def is_valid_combination(team):
    G, W, D, L, P = team
    if G != W + D + L:
        return False
    if P != 3*W + D:
        return False
    return True

def fill_missing_values(team):
    possible_values = list(range(101))
    missing_indices = [i for i, v in enumerate(team) if v == '?']

    # Adjust possible_values for points (P) 
    if 4 in missing_indices:
        possible_values = list(range(401))
    
    for values in itertools.product(possible_values, repeat=len(missing_indices)):
        new_team = team.copy()
        for idx, value in zip(missing_indices, values):
            new_team[idx] = value

        if is_valid_combination(new_team):
            return new_team

    return team  # if no valid combination found

def generate_test_case():
    N = 1000
    teams = []
    for _ in range(N):
        W = random.randint(0, 100)
        D = random.randint(0, 100 - W)
        L = 100 - W - D
        P = 3*W + D
        team = [100, W, D, L, P]
        # Randomly replacing some values with "?"
        for _ in range(random.randint(0, 2)):
            team[random.randint(0, 4)] = "?"
        teams.append(team)
    return N, teams

def read_input():
    N = int(input())
    data = []

    for _ in range(N):
        row = input().split()
        for i in range(len(row)):
            if row[i] != '?':
                row[i] = int(row[i])
        data.append(row)

    return N, data

if __name__ == "__main__":
    N, teams = read_input()

    for team in teams:
        filled_values = fill_missing_values(team)
        print(' '.join(map(str, filled_values)))

    # # Generating test case
    # N, test_teams = generate_test_case()
    # print(N)
    # # for team in test_teams:
    # #     print(' '.join(map(str, team)))
    # import time 
    # start = time.time()
    # for team in test_teams:
    #     filled_values = fill_missing_values(team)
    #     print(' '.join(map(str, filled_values)))
    #     end = time.time()
    # print(end - start)
    

