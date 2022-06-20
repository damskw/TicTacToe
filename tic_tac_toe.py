from time import sleep
from board import display_board, get_empty_board, is_board_full, get_winning_player, full_board_message, show_AI_vs_AI_winning_message, show_AI_winning_message, show_winning_message, won
#from coordinates import * #get_empty_squares, get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import check_play_again, get_menu_option, clear, get_player_name_and_choice, get_players_names, goodbye, loading, show_AI_vs_AI_welcome_message, show_logo
from os import system, name
from clint.textui import colored
from coordinates import *


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4




def main():
    #print(AI_PLAYER)
    #loading()
    #clear()
    show_logo()
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = " X "
    welcome = True
    ai_has_moved = False
    while is_game_running:
        if game_mode == HUMAN_VS_HUMAN:
            if welcome:
                player_one, player_two = get_players_names()
                welcome = False
                clear()
            while current_player == " X ":
                if not is_board_full(board): 
                    display_board(board)
                    row, column = get_human_coordinates(board, player_one)
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        display_board(board)
                        show_winning_message(player_one)
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        current_player = " O "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()

            while current_player == " O ":
                if not is_board_full(board):
                    display_board(board)
                    row, column = get_human_coordinates(board, player_two)
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        display_board(board)
                        show_winning_message(player_two)
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        current_player = " X "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()           

        if game_mode == HUMAN_VS_RANDOM_AI:
            if welcome:
                human_name, choice = get_player_name_and_choice()
                current_player = choice
                welcome = False
                clear()
            while current_player == " X ":
                if not is_board_full(board): 
                    display_board(board)
                    if choice == " X ":
                        row, column = get_human_coordinates(board, human_name)
                    else:
                        row, column = get_random_ai_coordinates(board)
                        ai_has_moved = True
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        display_board(board)
                        if choice ==" X ":
                            show_winning_message(human_name)
                        else:
                            show_AI_winning_message()
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        if ai_has_moved:
                            clear()
                            display_board(board)
                            confirmation = input("AI has made a move. Confirm by pressing enter. ")
                            if confirmation.lower() == "quit":
                                goodbye()
                            ai_has_moved = False
                            clear()
                            current_player = " O "
                        else:
                            current_player = " O "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()

            while current_player == " O ":
                if not is_board_full(board):
                    display_board(board)
                    if choice == " O ":
                        row, column = get_human_coordinates(board, human_name)
                    else:
                        row, column = get_random_ai_coordinates(board)
                        ai_has_moved = True
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        display_board(board)
                        if choice == " O ":
                            show_winning_message(human_name)
                        else:
                            show_AI_winning_message(human_name)
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        if ai_has_moved:
                            clear()
                            display_board(board)
                            confirmation = input("AI has made a move. Confirm by pressing enter. ")
                            if confirmation.lower() == "quit":
                                goodbye()
                            ai_has_moved = False
                            clear()
                            current_player = " X "
                        else:
                            current_player = " X "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()

        if game_mode == RANDOM_AI_VS_RANDOM_AI:
            if welcome:
                show_AI_vs_AI_welcome_message()
                welcome = False
                clear()
            while current_player == " X ":
                if not is_board_full(board):
                    row, column = get_random_ai_coordinates(board)
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        display_board(board)
                        show_AI_vs_AI_winning_message(current_player)
                        current_player = None
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        display_board(board)
                        confirmation = input("AI has moved. Acknowledge it's movement by pressing enter. ")
                        if confirmation.lower() == "quit":
                            goodbye()
                        clear()
                        current_player = " O "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    is_game_running = False
                    current_player = None
                    goodbye()

            while current_player == " O ":
                if not is_board_full(board):
                    row, column = get_random_ai_coordinates(board)
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        display_board(board)
                        show_AI_vs_AI_winning_message(current_player)
                        current_player = None
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        display_board(board)
                        confirmation = input("AI has moved. Acknowledge it's movement by pressing enter. ")
                        if confirmation.lower() == "quit":
                            goodbye()
                        clear()
                        current_player = " X "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    is_game_running = False
                    current_player = None
                    goodbye()

        if game_mode == HUMAN_VS_UNBEATABLE_AI:
            if welcome:
                human_name, choice = get_player_name_and_choice()
                current_player = choice                
                global AI_PLAYER
                global HUMAN_PLAYER
                AI_PLAYER = " X "
                HUMAN_PLAYER = " O "
                if choice.lower() == " x ":
                    AI_PLAYER = " O "
                    HUMAN_PLAYER = " X "
                elif choice.lower() == " o ":
                    AI_PLAYER = " X "
                    HUMAN_PLAYER = " O "

                welcome = False
                clear()
            while current_player == " X ":
                if not is_board_full(board): 
                    display_board(board)
                    if choice == " X ":
                        row, column = get_human_coordinates(board, human_name)
                    else:
                        row, column = get_unbeatable_ai_coordinates(board)
                        ai_has_moved = True
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        clear()
                        display_board(board)
                        if choice ==" X ":
                            show_winning_message(human_name)
                        else:
                            show_AI_winning_message(human_name)
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        if ai_has_moved:
                            clear()
                            display_board(board)
                            confirmation = input("AI has made a move. Confirm by pressing enter. ")
                            if confirmation.lower() == "quit":
                                goodbye()
                            ai_has_moved = False
                            clear()
                            current_player = " O "
                        else:
                            current_player = " O "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()

            while current_player == " O ":
                if not is_board_full(board):
                    display_board(board)
                    if choice == " O ":
                        row, column = get_human_coordinates(board, human_name)
                    else:
                        row, column = get_unbeatable_ai_coordinates(board)
                        ai_has_moved = True
                    board[row][column] = current_player
                    wining_player = get_winning_player(board, current_player)
                    if wining_player == current_player:
                        is_game_running = False
                        current_player = None
                        clear()
                        display_board(board)
                        if choice == " O ":
                            show_winning_message(human_name)
                        else:
                            show_AI_winning_message(human_name)
                        play_again = check_play_again()
                        if play_again:
                            clear()
                            main()
                        else:
                            goodbye()
                    else:
                        if ai_has_moved:
                            clear()
                            display_board(board)
                            confirmation = input("AI has made a move. Confirm by pressing enter. ")
                            if confirmation.lower() == "quit":
                                goodbye()
                            ai_has_moved = False
                            clear()
                            current_player = " X "
                        else:
                            current_player = " X "
                else:
                    display_board(board)
                    full_board_message()
                    play_again = check_play_again()
                    if play_again:
                        clear()
                        main()
                    goodbye()
                    
def minimax(board, player):
  free = get_empty_squares(board)

  game_over, score = terminal_state(board, free)
  if game_over:
    result = {'index': None, 'score': score}
    return result

  moves = []
  for i in free:
    move = {"index": None, "score": None}
    move["index"] = i
    
    board[i // 3][i % 3] = player

    if player == AI_PLAYER:
      result = minimax(board, HUMAN_PLAYER)
    else:
      result = minimax(board, AI_PLAYER)
    move["score"] = result["score"]
    moves.append(move)

    board[i // 3][i % 3] = " . " #move["index"]

  if player == AI_PLAYER:
    best_score = -10000
    for i in moves:
      if i["score"] > best_score:
        best_score = i["score"]
        best_move = i
  else:
    best_score = 10000
    for i in moves:
      if i["score"] < best_score:
        best_score = i["score"]
        best_move = i
  return best_move

def get_unbeatable_ai_coordinates(board):
  ai_choice = minimax(board, AI_PLAYER)
  temp = ai_choice["index"]
  row = temp // 3
  column = temp % 3

  return row, column

def terminal_state(board, free):
  game_over = False
  score = None

  if won(board, HUMAN_PLAYER):
    game_over = True
    score = -10
  
  elif won(board, AI_PLAYER):
    game_over = True
    score = 10

  elif not free:
    game_over = True
    score = 0

  return game_over, score

if __name__ == "__main__":
    main()