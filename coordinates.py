from board import display_board
from menu import clear

class TextColors:
  RED = '\033[91m'
  END = '\033[0m'
  YELLOW = '\033[93m'
  BOLD = '\033[1m'
  GREEN = '\033[92m'

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
      coordinates = input(TextColors.RED + 
                    "Invalid coordinates, please try again. "
                    + TextColors.END)
      is_valid_input = check_coordinates_input(coordinates)  
    elif are_coordinates_taken:
      coordinates = input(TextColors.RED + 
                    "These coordinates are already taken, please try again. "
                    + TextColors.END)
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


def get_random_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass