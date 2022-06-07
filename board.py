from re import L


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
  print("I'm sorry, the board is full!")

def is_board_full(board):
  if " . " in board[0]:
    return False
  elif " . " in board[1]:
    return False
  elif " . " in board[2]:
    return False
  return True

def show_winning_message(winning_player):
  print(f"Congratulations {winning_player}, you have won the game!")


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



# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    
    display_board(board)
    
    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1)) 

    board_2 = [
      [".", "O", "O"],
      [".", "O", "X"],
      [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2)) 

    board_3 = [
      ["O", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3)) 

    board_4 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
      ["X", "O", "O"],
      ["X", "O", "."],
      ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))