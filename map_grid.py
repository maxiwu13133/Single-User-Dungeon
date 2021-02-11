import combat
import random
import colors
import doctest

def valid_options_constant():
  VALID_OPTIONS = ("1", "2", "3", "4")
  return VALID_OPTIONS


def get_user_choice():
  """Ask user for direction
  
  :postcondition: stores input into variable
  :return: a string
  """
  direction = input("Type a number to move:\n1 = up\n2 = down\n3 = left\n4 = right\n")
  if direction == 'quit':
    quit()
    
  return direction


def validate_move(direction, coord):
  """Check if character can move in direction

  :param direction: a string
  :precondition: must be a string of a number 
  :param coord: a list
  :precondition: must be a list with two indices
  :postcondition: checks direction and coord to see if they are valid
  :return: a boolean
  
  >>> validate_move('1', [2, 0])
  False
  >>> validate_move('d', [3, 3])
  True
  """
  if direction == '1' and coord[1] == 0:
    return False

  if direction == '2' and coord[1] == 4:
    return False

  if direction == '3' and coord[0] == 0:
    return False

  if direction == '4' and coord[0] == 4:
    return False

  else:
    return True


def move_character_y(direction):
  """Check direction to return a value 

  :param direction: a string 
  :precondition: a string of a number
  :postcondition: checks direction and returns value accordingly
  :return: an int

  >>> print(move_character_y('1'))
  -1
  >>> print(move_character_y('3'))
  0
  """
  if direction == '1':
    return -1

  if direction == '2':
    return 1
    
  else:
    return 0


def move_character_x(direction):
  """Check direction to return a value 

  :param direction: a string 
  :precondition: a string of a number
  :postcondition: checks direction and returns value accordingly
  :return: an int

  >>> print(move_character_x('4'))
  1
  >>> print(move_character_x('7'))
  0
  """
  if direction == '3':
    return -1

  if direction == '4':
    return 1

  else:
    return 0


def health_gain(player_health):
  """Change health based on current health

  :param direction: an int
  :precondition: must be an integer between 1 to 10
  :postcondition: changes health and prints current health
  :return: an int

  >>> health_gain(8)
  'Current health: 10'
  >>> health_gain(10)
  'Current health: 10'
  """
  if player_health < 9:
    player_health += 2
    print(f'Current health: {colors.cyan(player_health)}')
    return player_health

  elif player_health == 9:
    player_health += 1
    print(f'Current health: {colors.cyan(player_health)}')
    return player_health

  else:
    print(f'Current health: {colors.cyan(player_health)}')
    return player_health


def character_coord(direction, coord):
  """Change coord list

  :param direction: a string
  :precondition: must be a string of a number 
  :param coord: a list
  :precondition: must be a list with two indices
  :postcondition: adds value of direction to coord indices
  :return: a list

  >>> print(character_coord('1', [2, 2]))
  [2, 1]
  >>> print(character_coord('4', [1, 3]))
  [2, 3]
  """
  coord[0] += move_character_x(direction)
  coord[1] += move_character_y(direction)
  return coord


def random_encounter(player_health):
  """Generate random int

  If the random int is 1, engage in battle

  :param: player_health: an int
  :precondition: must be an integer between 1 and 10
  :postconditon: generates random int, if it's 1, fight a wild kibble bag 
  :return: 3 integers
  """
  luck = random.randint(1, 4)
  if luck == 1:
    print(colors.yellow("A wild kibble bag has appeared"))
    remaining_health, enemies_killed, kibble = combat.combat(player_health)
    return remaining_health, enemies_killed, kibble

  else:
    remaining_health = health_gain(player_health)
    return remaining_health, 0, 0


def map_draw(coord):
  """Display map and character location

  :param coord: a list
  :precondition: must be a list with two indices
  :postcondition: displays lists with one of the indices of one of the lists being the character 
  :return: five lists

  >>> map_draw([2, 2])
  - - - - -
  - - - - -
  - - # - -
  - - - - -
  - - - - -
  >>> map_draw([0, 4])
  - - - - #
  - - - - -
  - - - - -
  - - - - -
  - - - - -
  """
  grid = ['-', '-', '-', '-', '-']
  for y_location in range(0, 5):
    if coord[1] == y_location:
      for x_location in range(0, 5):
        if coord[0] == x_location:
          grid_copy = grid[:]
          grid_copy[x_location] = '#'
          print(' '.join(grid_copy))
    else:
      print(' '.join(grid))
      
      
def map_board(coord, player_health):
  """Combine helper functions

  :param coord: a list
  :preconditon: must be a list with two indices
  :param player_health: an int
  :preconditon: must be an integer between 1 and 10
  :postcondition: combines helper functions to display map and health and trigger battles
  :return: 3 integers

  >>> map_board([2, 2], 8):
  - - - - -
  - - - - -
  - - # - -
  - - - - -
  - - - - -
  Current health: 8
  >>> map_board([4, 4], 10):
  - - - - -
  - - - - -
  - - - - -
  - - - - -
  - - - - #
  Current health: 10
  """
  direction = get_user_choice()
  valid_move = validate_move(direction, coord)
  
  if direction in valid_options_constant():
    if valid_move:
      coord = character_coord(direction, coord)
      map_draw(coord)
      remaining_health, enemies_killed, kibble = random_encounter(player_health)
      return remaining_health, enemies_killed, kibble

    else:
      print(colors.red('You can not go in that direction!'))
      map_draw(coord)
      return player_health, 0, 0

  else:
    map_draw(coord)
    print(colors.red("Invalid input"))
    return player_health, 0, 0
