import numpy as np


def get_input():
  test_cases = []
  n = input()
  n = int(n)
  for i in range(n):
    m = int(input())
    segments = [ np.array(input().split(), dtype=float) for _ in range(m) ]
    
    test_cases.append(segments)
  return test_cases

def get_location(segments):

    location = np.array([0.0,0.0], dtype=float)
    bearing = 0.0

    for segment in segments:
      angle = segment[0]
      length = segment[1]
      bearing += angle
      bearing_rad = np.radians(bearing + 90)
      direction = np.array([np.cos(bearing_rad), np.sin(bearing_rad)])
      vec = length * direction
      location += vec
    
    x = location[0]
    y = location[1]

    print(f'{x:.5f} {y:.5f}')

test_cases = get_input()

for test_case in test_cases:
   
   get_location(test_case)


