from re import L
class TextColors:
  RED = '\033[91m'
  END = '\033[0m'
  YELLOW = '\033[93m'
  BOLD = '\033[1m'
  GREEN = '\033[92m'

def get_empty_board():
    empty_board = [
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    ]
    return empty_board


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
  if " . " in board[0]:
    return False
  elif " . " in board[1]:
    return False
  elif " . " in board[2]:
    return False
  return True

def show_winning_message(winning_player):
  print(TextColors.GREEN + 
        "\tCongratulations," + 
        TextColors.BOLD +
        winning_player + 
        TextColors.END + 
         "You have won this game! ")


def get_winning_player(board, current_player):
  first_row = board[0][0] == board[0][1] == board[0][2] != ' . '
  second_row = board[1][0] == board[1][1] == board[1][2] != ' . '
  third_row = board[2][0] == board[2][1] == board[2][2] != ' . '
  frist_across = board[0][0] == board[1][1] == board[2][2] != ' . '
  second_across = board[0][2] == board[1][1] == board[2][0] != ' . '
  down_the_left_side = board[0][0] == board[1][0] == board[2][0] != ' . '
  down_the_middle = board[0][1] == board[1][1] == board[2][1] != ' . '
  down_the_right_side = board[0][2] == board[1][2] == board[2][2] != ' . '

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

  return None

if __name__ == "__main__":
    print("Should return None")
    print(get_winning_player())