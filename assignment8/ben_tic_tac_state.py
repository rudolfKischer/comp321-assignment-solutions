def find_winner(game_state):
    W = [
        0b000000111, 0b000111000, 0b111000000,  # horizontals
        0b001001001, 0b010010010, 0b100100100,  # verticals
        0b100010001, 0b001010100                # diagonals
    ]
    
    xpos = game_state >> 9
    opos = ~(game_state >> 9) & game_state
    
    for wpat in W:
        if (xpos & wpat) == wpat:
            return "X wins"
        if (opos & wpat) == wpat:
            return "O wins"

    if (game_state & 0b111111111) == 0b111111111:
        return "Cat's"

    return "In progress"

    
def main():
    n = int(input())
    games = [int(input(), 8) for _ in range(n)]

    for game in games:
        print(find_winner(game))

main()
