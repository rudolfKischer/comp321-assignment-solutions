from functools import lru_cache
seen_boards = {}

def count_pebbles(board):
    count = 0
    while board:
        count += board & 1
        board >>= 1
    return count

@lru_cache(maxsize=None)
def count_min_pebbles(board: list):
    if board in seen_boards:
        return seen_boards[board]
    
    min_remaining_pebbles = count_pebbles(board)
    for i in range(21):
        # Check if the bits at this 3-bit chunk represent a valid right-move
        if (board & (7 << i)) == (6 << i):
            # Apply a 000 mask to this chunk and then set it to be 001
            new_board = board & (~(7 << i))
            new_board |= (1 << i)
            min_remaining_pebbles = min(min_remaining_pebbles, count_min_pebbles(new_board))
        
        if (board & (7 << i)) == (3 << i):
            new_board = board & (~(7 << i))
            #print((4 << i))
            new_board |= (4 << i)
            min_remaining_pebbles = min(min_remaining_pebbles, count_min_pebbles(new_board))
        
    seen_boards[board] = min_remaining_pebbles
    return min_remaining_pebbles

def main():
    n_games = int(input())
    games = [input().strip() for _ in range(n_games)]
    for board in games:
        # Conver to binary
        board = int(board.replace('o', '1').replace('-', '0'), 2)
        # print("Size of board: {} is {}".format(bin(board), len(bin(board))))
        print(count_min_pebbles(board))
        seen_boards.clear()
main()