from board import display_board
from menu import clear

class TextColors:
  RED = '\033[91m'
  END = '\033[0m'

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
  if int(coordinates[1]) > 3 or int(coordinates[1]) < 1:
    return False
  if coordinates[0] != A and coordinates[0] != B and coordinates[0] != C:
    return False
  return True

def get_human_coordinates(board, player_name):
  is_menu_presented = True
  is_wrong_input = False
  A = rows()[0]
  B = rows()[1]
  C = rows()[2]
  while is_menu_presented:
    if not is_wrong_input:
      coordinates = input(f"{player_name}, please enter coordinates: ")
      is_valid_input = check_coordinates_input(coordinates)
    else:
      coordinates = input(TextColors.RED + 
                    "Invalid coordinates, please try again. "
                    + TextColors.END)
      is_valid_input = check_coordinates_input(coordinates)  
    if is_valid_input:
      is_menu_presented = False
    else:
      clear()
      display_board(board)
      is_wrong_input = True
  if coordinates[0] == A:
    row = 0
  elif coordinates[0] == B:
    row = 1
  elif coordinates[0] == C:
    row = 2
  column = int(coordinates[1]) - 1
  clear()
  return row, column

  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """


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


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 