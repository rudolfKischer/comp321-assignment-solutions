def winner_is(turn_number):
    return "Ollie" if turn_number % 2 == 0 else "Stan"

def get_winner(stones, valid_moves):
    # Initialize table where the number 
    table = [False] * (stones + 1)
    for i in range(1, stones + 1):
        for move in valid_moves:
            if i - move >= 0 and not table[i - move]:
                table[i] = True
                break

    return winner_is(table[stones])

def main():
    results = []
    while True:
        try:
            line = input().split()
            if not line:
                break
            
        except (ValueError, EOFError):
            break


        n_stones, m = int(line[0]), int(line[1])
        valid_moves = [int(x) for x in line[2:m+2]]
        #valid_moves = sorted(valid_moves, reverse=True)
        results.append(get_winner(n_stones, valid_moves))

    for winner in results:
        print(f"{winner} wins")

main()