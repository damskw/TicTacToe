from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option, clear
from os import system, name

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    game_mode = get_menu_option() # Returns int value of chosen game option
    board = get_empty_board()
    is_game_running = True
    current_player = " X "
    while is_game_running:
        if game_mode == HUMAN_VS_HUMAN:
            while current_player == " X ":
                display_board(board)
                get_human_coordinates(board, current_player)
                current_player = " O "
            while current_player == " O ":
                display_board(board)
                get_human_coordinates(board, current_player)
                current_player = " X "


        # current_player = 'X'
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates


        # x, y = get_human_coordinates(board, current_player)
        
        # board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop


        # winning_player = get_winning_player(board)
        # its_a_tie = is_board_full(board)


if __name__ == "__main__":
    main()