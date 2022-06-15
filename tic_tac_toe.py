from time import sleep
from board import display_board, get_dirty_board, get_empty_board, is_board_full, get_winning_player, full_board_message, show_AI_vs_AI_winning_message, show_AI_winning_message, show_winning_message
from coordinates import get_empty_squares, get_human_coordinates, get_random_ai_coordinates, minimax
from menu import check_play_again, get_menu_option, clear, get_player_name_and_choice, get_players_names, goodbye, show_AI_vs_AI_welcome_message, show_logo
from os import system, name
from clint.textui import colored


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def main():
    clear()
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
                    is_game_running = False
                    current_player = None

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
                    is_game_running = False
                    current_player = None

        if game_mode == HUMAN_VS_RANDOM_AI:
            if welcome:
                human_player, choice = get_player_name_and_choice()
                current_player = choice
                welcome = False
                clear()
            while current_player == " X ":
                if not is_board_full(board): 
                    display_board(board)
                    if choice == " X ":
                        row, column = get_human_coordinates(board, human_player)
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
                            show_winning_message(human_player)
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
                            input("AI has made a move. Confirm by pressing enter. ")
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
                    is_game_running = False
                    current_player = None

            while current_player == " O ":
                if not is_board_full(board):
                    display_board(board)
                    if choice == " O ":
                        row, column = get_human_coordinates(board, human_player)
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
                            show_winning_message(human_player)
                        else:
                            show_AI_winning_message(human_player)
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
                            input("AI has made a move. Confirm by pressing enter. ")
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
                    is_game_running = False
                    current_player = None

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
                        input("AI has moved. Acknowledge it's movement by pressing enter. ")
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
                        input("AI has moved. Acknowledge it's movement by pressing enter. ")
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
            board = get_dirty_board()
            test = get_empty_squares(board)
            print(test)
            current_player = " O "
            choice = minimax(board, current_player)
            print(choice)
            is_game_running = False


if __name__ == "__main__":
    main()