import math

def get_dx(w,r):
    dx = math.sqrt((r**2)-(w/2)**2)
    #print(f"{r**2} - {(w/2)**2} = {r**2 - (w/2)**2}, sqrt({r**2 - (w/2)**2}) = {dx}")
    return dx

def get_true_coverages(sprinkler_positions,w):
    coverages = []
    for x,r in sprinkler_positions:
        coverage_r, coverage_l = x+get_dx(w,r), max(0,x-get_dx(w,r))
        #print(f"For sprinkler at position x={x} with radius r={r}, coverage=({coverage_l},{coverage_r})")
        coverages.append((coverage_l,coverage_r))
    return coverages

def min_sprinklers(coverages, l):
    coverages = sorted(coverages, key=lambda x: x[0])  # Sort only by left coverage
    distance = 0
    sprinklers_used = 0
    index = 0
    while distance < l and index < len(coverages):
        # Find the sprinkler with max right coverage among those whose left is <= distance
        max_right = -1
        selected_index = -1
        while index < len(coverages) and coverages[index][0] <= distance:
            if coverages[index][1] > max_right:
                max_right = coverages[index][1]
                selected_index = index
            index += 1
        
        if selected_index == -1:
            return -1  # No sprinkler can be used to cover this segment
        
        distance = max_right  # Update the distance to the right-most coverage of the selected sprinkler
        sprinklers_used += 1

    if distance < l:
        return -1  # Couldn't cover the entire lawn
    return sprinklers_used

def main():
    results = []
    line = input().split()
    while line != []:
        try:
            n, l, w = int(line[0]), int(line[1]), int(line[2])
            #print(f"n={n}, l={l}, w={w}")
        except (ValueError, IndexError) as e:  # Corrected the exception catching syntax
            #print(f"Exception caught: {e}")
            break
        else:
            sprinkler_positions = list(map(lambda x: [int(x[0]), int(x[1])], [input().split() for _ in range(n)]))
            #print(f"sprinkler_positions: {sprinkler_positions}")
            results.append(min_sprinklers(get_true_coverages(sprinkler_positions,w), l))
            #print(f"true_coverages: {result}")
        line = input().split()
        print(line)
    for result in results:
        print(result)
main()