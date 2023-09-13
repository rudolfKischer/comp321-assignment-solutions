

largest_dif = int(input())

line_string = input()

head_counts = {
  'M': 0,
  'W': 0
}

def let_in(person):
    head_counts[person] += 1

def get_inbalance(person):
  #how many men are we over?
  inbalance = head_counts['M'] - head_counts['W']
  #how many women are we over?
  if person == 'W':
      inbalance = -inbalance
  return inbalance

def can_be_let_in(person):
  return (get_inbalance(person) + 1) <= largest_dif

def can_anyone_be_let_in(line):
    if len(line) <= 0:
       return False

    best_spot_to_let_in = 0
    if len(line) > 1 and get_inbalance(line[0]) >= 1 and get_inbalance(line[1]) < 1:
        best_spot_to_let_in = 1

    person_to_let_in = line[best_spot_to_let_in]

    if can_be_let_in(person_to_let_in):
       del line[best_spot_to_let_in]
       let_in(person_to_let_in)
       return True
    return False

def let_people_in(line):
    line = list(line)
    while can_anyone_be_let_in(line):
      continue
   
    head_count = head_counts['M'] + head_counts['W']
    print(head_count)


let_people_in(line_string)
      

       
  
      
      