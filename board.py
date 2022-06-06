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


def is_board_full(board):
  if " . " in board[0]:
    return False
  elif " . " in board[1]:
    return False
  elif " . " in board[2]:
    return False
  return True



def get_winning_player(board):
  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  pass


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