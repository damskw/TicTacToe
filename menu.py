from os import system, name

class TextColors:
  RED = '\033[91m'
  END = '\033[0m'

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

def get_menu_option():
  is_menu_presented = True
  while is_menu_presented:
    selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. Random AI vs Random AI\n"
                    "3. Human vs Random AI\n"
                    "4. Human vs Unbeatable AI\n")
    is_valid_input = check_menu_input(selected_option)
    if is_valid_input:
      is_menu_presented = False
    else:
      clear()
      print(TextColors.RED + "\tError: Incorect value. Please provide numbers 1-4" + TextColors.END)
  clear()
  return selected_option