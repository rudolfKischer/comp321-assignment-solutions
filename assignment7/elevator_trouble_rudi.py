
# floors, start, foal, up, down
floors, start, goal, up, down = map(int, input().split())

#Want to run bfs 

def find_floor():

    discovery_queue = []
    discovery_queue.append((start,0))

    visited = [False] * floors


    while discovery_queue:
      considered = discovery_queue.pop(0)
      if considered[0] == goal:
        print(considered[1])
        return considered[1]
      if visited[considered[0]-1]:
        continue

      up_floor = considered[0] + up
      if up_floor <= floors:
        discovery_queue.append((up_floor, considered[1]+1))
      
      down_floor = considered[0] - down
      if down_floor > 0:
        discovery_queue.append((down_floor, considered[1]+1))
      
      visited[considered[0]-1] = True

    
    print("use the stairs")
    return None

find_floor()