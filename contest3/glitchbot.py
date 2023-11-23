
import numpy as np

def get_input():
  pos = list(map(int, input().split()))
  n = int(input())
  moves = [input() for i in range(n)]

  return pos, moves






def get_position(moves):
    position = np.array([0,0])

    direction = np.array([1,0])

    left_turn = np.array([[0, 1], [-1, 0]])
    right_turn = np.array([[0, -1], [1, 0]])

    for move in moves:
        if move == 'Forward':
            position += direction
        elif move == 'Right':
           direction = np.dot(right_turn, direction)
        elif move == 'left':
           direction = np.dot(left_turn, right_turn)
    
    return position

pos, moves = get_input()

new_pos = get_position(moves)
print(new_pos)










  