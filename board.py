from re import L
from clint.textui import colored

def get_empty_board():
    empty_board = [
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    ]
    return empty_board

def get_dirty_board():
    dirty_board = [
    [" X ", " O ", " . "],
    [" X ", " O ", " . "],
    [" . ", " . ", " . "],
    ]
    return dirty_board

def display_board(board):
  print("    1", "  2", "  3")
  print("A  " + board[0][0] + "|" + board[0][1] + "|" + board[0][2])
  print("   ---+---+---")
  print("B  " + board[1][0] + "|" + board[1][1] + "|" + board[1][2])
  print("   ---+---+---")
  print("C  " + board[2][0] + "|" + board[2][1] + "|" + board[2][2])
  print("   ---+---+---")

def full_board_message():
  print("\t There's no more space to move! The game has ended with a tie. ")

def is_board_full(board):
  check = []
  for row in range(3):
    for col in range(3):
      check.append(board[row][col])
  if " . " not in check:
    return True 
  else:
    return False

def show_winning_message(winning_player):
  print(colored.green 
        ("\tCongratulations, " + 
        winning_player) +
        colored.white 
         ("! You have won this game! "))

def show_AI_winning_message(player):
  print(colored.red 
        ("\tYou have failed, ") + 
        player +
        colored.white 
         ("! AI has won this game! "))

def show_AI_vs_AI_winning_message(player):
  print(player + " has won this game.")


def get_winning_player(board, current_player):
  first_row = board[0][0] == board[0][1] == board[0][2] != ' . '
  second_row = board[1][0] == board[1][1] == board[1][2] != ' . '
  third_row = board[2][0] == board[2][1] == board[2][2] != ' . '
  frist_across = board[0][0] == board[1][1] == board[2][2] != ' . '
  second_across = board[0][2] == board[1][1] == board[2][0] != ' . '
  down_the_left_side = board[0][0] == board[1][0] == board[2][0] != ' . '
  down_the_middle = board[0][1] == board[1][1] == board[2][1] != ' . '
  down_the_right_side = board[0][2] == board[1][2] == board[2][2] != ' . '
  no_winner = board[0][0] != ' . ' and board[0][1] != ' . ' and board[1][0] != ' . ' and board[1][1] != ' . ' and board[2][1] != ' . '

  if down_the_left_side:
    winning_player = current_player
    return winning_player
  
  if down_the_middle:
    winning_player = current_player
    return winning_player

  if down_the_right_side:
    winning_player = current_player
    return winning_player

  if first_row:
    winning_player = current_player
    return winning_player

  if second_row:
    winning_player = current_player
    return winning_player

  if third_row:
    winning_player = current_player
    return winning_player

  if frist_across:
    winning_player = current_player
    return winning_player

  if second_across:
    winning_player = current_player
    return winning_player

  if no_winner:
    return None

  return None

def won(board, current_player):

  first_row = board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player
  second_row = board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player
  third_row = board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player
  frist_across = board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player
  second_across = board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player
  down_the_left_side = board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player
  down_the_middle = board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player
  down_the_right_side = board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player

  if first_row or second_row or third_row or frist_across or second_across or down_the_left_side or down_the_middle or down_the_right_side:
    return True

  return False