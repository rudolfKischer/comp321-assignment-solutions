
# a set of friends owe eachother money, or are owed money
# no one wants tos speak to eachotehr
# each friend is only willing to speak to a subset of friends
# Need to see if its possible for everyone to get even, by gonly givin money between friends


# n = number of friends,    2 ,= n <= 10 000
# m = the number of friend ships    0 <= m <= 50 000

# n lines, each with an int o
# o = amound to money owed    , -10 000 <= 0 <- 10 000

# m lines, each contains in a pair (x,y)
# (x,y) indicates that person x and y are still friends

# for this problem, we can create teh freindship network

# within the friendship network we are going to have some number of connected compoenents
# each componenet represents the group of friends that are willing to talk to eachother

# if A is friends with B, 
# but A is not friends C, but needs to give C money, 
# then A can give the money to B, and then the money to C

# so we can balance out anyone who is in our connected friend group

# For this problem, we just want to balance everyone
# its not like each person ows a perticular person money
# so for each connected component if we can balance out , 
#then we everyone can get the right amount of money

# to check if a component is balanced out, all we have to do is check if the sum
# of all the money owed is equal to 0

# another way to look at this is a network problem
# each person who owes money is a source
# each persone who is owed money is a sink
# the output from each source needs to be equal to the amount the sinks can drain
# if they are not equal, someone will still be owed money, 
# or somone will owe money

# to accomplish this we can built

# we can compute this some by running BFS on our graph
# We choose a random node to start at 
# as we go along we start a running sum
# once our queue is empty, if our sum is not 0, then we know that it is impossible

# if our qeue is empty and our sum is 0 then we pick a new node 
# from the list of unvisited nodes

# for our graph we are going to need a couple things
# - adjacency list
# - unvisted list
# - visted boolean array

# note that there will be 10, 000 people
# and 50, 000 relationship

# if we has sqrt(50, 000) = 223 people then every slot in the matrix would get used
# if we had 700 people, then about 10% of it would be filled

# 700 / 10 000 = 0.07, which means only 7% of the time more than 10% of the matrix is being used

# so it seems we shuold go for an adjacency list


def get_input():
  n, m = list(map(int,input().split()))
  debts = [int(input()) for i in range(n)]
  friends = [list(map(int,input().split())) for i in range(m)]
  return debts, friends

def adj_list(n, friends):
  adg = [ [] for _ in range(n) ]
  for rel in friends:
    f0 = rel[0]
    f1 = rel[1]
    adg[f0].append(f1) 
    adg[f1].append(f0)
  return adg

def get_unvisited(is_visited):
    unvisted = []
    for i in range(len(is_visited)):
       if not is_visited[i]:
          unvisted.append(i)
    return unvisted
   

def bal_debts(debts,adj_list):
    # boolean array for instantly check if a certain friend has been checked
    is_visited = [ False ] * len(adj_list)
    # list of unvisited, so we can quickly grab a new one, when reach the end

    for person in range(len(adj_list)):
      if is_visited[person]:
        continue
       
      running_sum = 0
      exploration_queue =[person]

      while len(exploration_queue) > 0:
        
        cur = exploration_queue.pop(0)
        if is_visited[cur]:
          continue
        
        is_visited[cur] = True
        running_sum += debts[cur]

        for friend in adj_list[cur]:
            if not is_visited[friend]:
              exploration_queue.append(friend)

      
      if running_sum != 0:
         print("IMPOSSIBLE")
         return
    
    print("POSSIBLE")
    

debts, friends = get_input()
friend_graph = adj_list(len(debts), friends)

bal_debts(debts, friend_graph)




