import numpy as np
import re
import os

#
# Printing the sky.
#
def print_stars(star_coords, x_size, y_size):
  matrix = [['***'] * x_size for i in range(y_size)]
  for (x,y) in star_coords:
    matrix[y][x] = " # "

  for row in matrix:
    print(str.join('', row))

#
# Update the positions on the night sky, takes tuples 
# representing each star's movement delta.
# 
def update_stars(stars, velocities):
  limits = (max_x, max_y)
  for i in range(len(stars)):
    new_pos = np.add(stars[i], velocities[i])    
    stars[i] = modulo_tuple(new_pos, limits)


def modulo_tuple(dividend, divisor):
  return (np.mod(dividend,divisor))

in_file = open("input.txt");

pos_coords = list()
velocities = list()
max_x = 0
max_y = 0

#
# Parse every line and create one tuple representing the 
# star's starting coordinates and one tuple representing
# the delta of the stars movement each night.
#
for line in in_file:
  match_object = re.search(r"<\s*([\s-]\d+),\s*([\s-]\d+)>.*<\s*([\s-]\d+),\s*([\s-]\d+)>",line.strip())

  pos_x, pos_y, vel_x, vel_y = match_object.groups()
  if int(pos_x) > max_x:
    max_x = int(pos_x)
  if int(pos_y) > max_y:
    max_y = int(pos_y)
  pos_coords.append((int(pos_x), int(pos_y)))
  velocities.append((int(vel_x), int(vel_y)))

for i in range(len(pos_coords)):
  pos_coords[i-1] = modulo_tuple(pos_coords[i-1], (max_x, max_y))

#
# Run a loop for the user. Manually run until a pattern
# is found that matches a language the human knows.
# 
continue_response = True
while continue_response:
  os.system('cls' if os.name == 'nt' else 'clear')
  print_stars(pos_coords, max_x, max_y)
  if (input('\n Continue? (y/n)') != 'n'):
    update_stars(pos_coords, velocities)
  else:
    continue_response = False
