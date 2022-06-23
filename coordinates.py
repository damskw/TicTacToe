import random
from board import display_board, won
from menu import clear, goodbye
from clint.textui import colored

def rows():
  A = "a"
  B = "b"
  C = "c"
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
  row = coordinates[0]
  if row.upper().lower() != A and row.upper().lower() != B and row.upper().lower() != C:
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
  row_check = coordinates[0]
  if row_check.upper().lower() == A:
    row = 0
  elif row_check.upper().lower() == B:
    row = 1
  elif row_check.upper().lower() == C:
    row = 2
  return row

def get_human_coordinates(board, player_name):
  is_menu_presented = True
  is_wrong_input = False
  are_coordinates_taken = False
  while is_menu_presented:
    if not is_wrong_input and not are_coordinates_taken:
      coordinates = input(f"{player_name}, please enter coordinates: ")
      if coordinates.lower() == "quit":
        goodbye()
      is_valid_input = check_coordinates_input(coordinates)
    elif is_wrong_input and not are_coordinates_taken:
      coordinates = input(colored.red 
                    ("Invalid coordinates, please try again. "))
      if coordinates.lower() == "quit":
        goodbye()
      is_valid_input = check_coordinates_input(coordinates)  
    elif are_coordinates_taken:
      coordinates = input(colored.red 
                    ("These coordinates are already taken, please try again. "))
      if coordinates.lower() == "quit":
        goodbye()
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
        free_list.append(row * 3 + col)
  return free_list


def main():
  pass
  

if __name__ == "__main__":
    main()