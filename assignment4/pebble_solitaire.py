
import re
from functools import lru_cache
pebble = 'o'

moves = {
    'oo-' : '--o',
    '-oo' : 'o--'
}

def get_moves(board):
    return [
        board[:match.start()] + move + board[match.end():]
        for potential_move, move in moves.items()
        for match in re.finditer(potential_move, board)
    ]

@lru_cache(maxsize=None)
def get_min_pebble_solve(game_board):
    moves = get_moves(game_board)
    if not moves:
        return game_board.count(pebble)
    return min(map(get_min_pebble_solve, moves))

for game in [input() for _ in range(int(input()))]:
    print(get_min_pebble_solve(game))
