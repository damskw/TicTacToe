import random
from board import display_board, get_empty_board, won
from menu import clear
from clint.textui import colored

def rows():
  A = "A".upper().lower()
  B = "B".upper().lower()
  C = "C".upper().lower()
  return A, B, C

def check_coordinates_input(coordinates):
  A = rows()[0]
  B = rows()[1]
  C = rows()[2]
  if len(coordinates) > 2 or len(coordinates) < 2:
    return False
  try:
   if int(coordinates[1]) > 3 or int(coordinates[1]) < 1:
     return False
  except ValueError:
    return False
  if coordinates[0] != A and coordinates[0] != B and coordinates[0] != C:
    return False
  return True

def check_free_coordinates(board, row, column):
  if board[row][column] != ' . ':
    return False
  return True

def row_input_change(coordinates):
  A = rows()[0]
  B = rows()[1]
  C = rows()[2]
  if coordinates[0] == A:
    row = 0
  elif coordinates[0] == B:
    row = 1
  elif coordinates[0] == C:
    row = 2
  return row

def get_human_coordinates(board, player_name):
  is_menu_presented = True
  is_wrong_input = False
  are_coordinates_taken = False
  while is_menu_presented:
    if not is_wrong_input and not are_coordinates_taken:
      coordinates = input(f"{player_name}, please enter coordinates: ")
      is_valid_input = check_coordinates_input(coordinates)
    elif is_wrong_input and not are_coordinates_taken:
      coordinates = input(colored.red 
                    ("Invalid coordinates, please try again. "))
      is_valid_input = check_coordinates_input(coordinates)  
    elif are_coordinates_taken:
      coordinates = input(colored.red 
                    ("These coordinates are already taken, please try again. "))
      are_coordinates_taken = False
      is_valid_input = check_coordinates_input(coordinates) 
    if is_valid_input:
      row = row_input_change(coordinates)
      column = int(coordinates[1]) - 1
      is_valid_coordinates = check_free_coordinates(board, row, column)
      if is_valid_coordinates:
        is_menu_presented = False
      else:
        clear()
        display_board(board)
        are_coordinates_taken = True
    else:
      clear()
      display_board(board)
      is_wrong_input = True
  clear()
  return row, column


def get_random_ai_coordinates(board):
  getting_coordinates = True
  while getting_coordinates:
    row = random.randint(0,2)
    column = random.randint(0,2)
    are_free_coordinates = check_free_coordinates(board, row, column)
    if are_free_coordinates:
      getting_coordinates = False
      clear()
      return row, column
    else:
      getting_coordinates = True


def get_empty_squares(board):
  free_list = []
  for row in range(0,3):
    for col in range(0,3):
      if board[row][col] == " . ":
        free_list.append((row, col))
  return free_list

def minimax():
  pass

def get_unbeatable_ai_coordinates():
  pass


def main():
  pass

if __name__ == "__main__":
    main()