n = int(input())

people = [list(map(int, input().split())) for i in range(n)]


def sort_a(x):
    return x[0]



people_sorted = people.copy()
people_sorted.sort(key=sort_a)

for i in range(len(people_sorted)):
    people_sorted[i].append(i+1)

print(people_sorted) 

for person in people_sorted:
    person_rank = person[2]
    person_b_range = person[1]
    person
    for j in range(person_rank,person_b_range):
        other_person_a_range = people[j][0]
        if other_person_a_range < person_rank:
            
        
        
