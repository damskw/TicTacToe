from os import system, name

class TextColors:
  RED = '\033[91m'
  END = '\033[0m'
  YELLOW = '\033[93m'
  BOLD = '\033[1m'
  GREEN = '\033[92m'

def clear():
  if name == 'nt':
    _ = system('cls')

def check_menu_input(selected_option):
  try:
    selected_option = int(selected_option)
  except ValueError:
    return False
  if selected_option > 4 or selected_option < 1:
    return False
  return True

def show_menu():
  selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. Random AI vs Random AI\n"
                    "3. Human vs Random AI\n"
                    "4. Human vs Unbeatable AI\n")
  return selected_option

def show_error_menu():
  selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. Random AI vs Random AI\n"
                    "3. Human vs Random AI\n"
                    "4. Human vs Unbeatable AI\n"
                    + TextColors.RED + 
                    "\tError: Incorect value. Please provide numbers 1-4\n" 
                    + TextColors.END)
  return selected_option

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
                    "Please enter name for the first player: ")
  player_two = input("Great! Now enter name for the second player: ")
  return player_one, player_two