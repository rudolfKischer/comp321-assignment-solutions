

n, next_round_max, max_same_school = tuple([int(i) for i in input().split()])



# (team_num, school)

teams = [list(map(int,input().split())) for i in range(n)]

def get_next_teams(teams):
    teams_accepted = []

    teams_extra = []

    school_count = {}

    for team in teams:
      if len(teams_accepted) >= next_round_max:
         break
      school = team[1]
      this_school_count = school_count.get(school, 0)
      if this_school_count < max_same_school:
          teams_accepted.append(team[0])
          school_count[school] = this_school_count + 1
          continue
      
      teams_extra.append(team)


    if len(teams_accepted) < next_round_max:
       for team in teams_extra:
          if len(teams_accepted) >= next_round_max:
              break
          teams_accepted.append(team[0])
    
    return teams_accepted

out = [print(team) for team in get_next_teams(teams)]
  






  










