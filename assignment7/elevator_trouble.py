def bfs(floors, start, goal, up, down):
    queue = [start]
    visited = set()
    distances = [0] * (floors + 1)

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return str(distances[current])
        
        if current + up <= floors and current + up not in visited:
            queue.append(current + up)
            distances[current + up] = distances[current] + 1

        if current - down > 0 and current - down not in visited:
            queue.append(current - down)
            distances[current - down] = distances[current] + 1

    return "use the stairs"

def main():
    f, s, g, u, d = list(map(int, input().split()))
    shortest_d = bfs(f, s, g, u, d)
    print(shortest_d)

main()