from os import system, name
from clint.textui import colored
import pyfiglet
import sys

def clear():
  if name == 'nt':
    _ = system('cls')

def show_logo():
  logo = pyfiglet.figlet_format("Tic Tac Toe")
  print(colored.yellow(logo))

def goodbye():
  goodbye = pyfiglet.figlet_format("Goodbye!")
  print(colored.yellow(goodbye))
  sys.exit()

def check_menu_input(selected_option):
  try:
    selected_option = int(selected_option)
  except ValueError:
    return False
  if selected_option > 4 or selected_option < 1:
    return False
  return True

def show_AI_vs_AI_welcome_message():
  message = input("You have chosen AI vs AI mode. Watch AIs fight with each other! ")
  if message.lower() == "quit":
    goodbye()

def show_menu():
  selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. Random AI vs Random AI\n"
                    "3. Human vs Random AI\n"
                    "4. Human vs Unbeatable AI\n")
  if selected_option.lower() == "quit":
    goodbye()
  return selected_option

def show_error_menu():
  selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. Random AI vs Random AI\n"
                    "3. Human vs Random AI\n"
                    "4. Human vs Unbeatable AI\n"
                    + colored.red 
                    ("\tError: Incorect value. Please provide numbers 1-4\n"))
  if selected_option.lower() == "quit":
    goodbye()
  return selected_option

def check_play_again():
  decision = input("\tThe game has ended. Would you like to play again? (y/n) ")
  while decision.lower() != "y" and decision.lower() != "n":
    decision = input(colored.red 
    ("\tI'm sorry, I didn't get that! Would you like to play again? Yes or no? (y/n) "))
  if decision.lower() == "n":
    return False
  return True

def get_menu_option():
  is_menu_presented = True
  is_wrong_input = False
  while is_menu_presented:
    if not is_wrong_input:
      selected_option = show_menu()
      is_valid_input = check_menu_input(selected_option)
    else:
      selected_option = show_error_menu()
      is_valid_input = check_menu_input(selected_option)
    if is_valid_input:
      is_menu_presented = False
    else:
      clear()
      is_wrong_input = True
  clear()
  return int(selected_option)

def get_players_names():
  player_one = input("You've chosen Human vs Human.\n"
                    "Please enter name for the first player (X): ")
  if player_one.lower() == "quit":
    goodbye()
  while len(player_one) == 0:
    player_one = input(colored.red 
                  ("\tI'm sorry, name cannot be empty. Please try again. "))
    if player_one.lower() == "quit":
      goodbye()
  player_two = input("Great! Now enter name for the second player (O): ")
  if player_two.lower() == "quit":
    goodbye()
  while len(player_two) == 0:
    player_two = input(colored.red 
                  ("\tI'm sorry, name cannot be empty. Please try again. "))
    if player_two.lower() == "quit":
      goodbye()

  return player_one, player_two

def get_player_name_and_choice():
  player_name = input("You've chosen Human vs AI.\n"
                    "Please enter your name: ")
  if player_name.lower() == "quit":
    goodbye()
  while len(player_name) == 0:
    player_name = input(colored.red 
                  ("\tI'm sorry, name cannot be empty. Please try again. "))
    if player_name.lower() == "quit":
      goodbye()
  choice = input("Please enter your symbol: X or O? ")
  if choice.lower() == "quit":
    goodbye()
  while choice.upper() != "X" and choice.upper() != "O":
    choice = input(colored.red
                    ("\tPlease enter X or O. "))
    if choice.lower() == "quit":
      goodbye()
  if choice.upper() == "X":
    choice = " X "
  elif choice.upper() == "O":
    choice = " O "

  return player_name, choice