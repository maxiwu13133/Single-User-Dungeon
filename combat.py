import random
import colors
import doctest

def damage_speech_constant():
  DAMAGE_SPEECH = (colors.green('tickled'), colors.yellow('pierced'), colors.red('amputated'), colors.magenta('obliterated'), 
  colors.cyan("decimated"), colors.blue("deleted"))
  return DAMAGE_SPEECH


def valid_options_constant():
  VALID_OPTIONS = ("1", "2")
  return VALID_OPTIONS


def health_drop():
  """Determin of kibble bag drops kibble or not 
  
  If random int is 1, you get a kibble

  :postcondition: generate random int, if it's 1, get a value of 1
  :return: an int
  """
  
  if random.randint(1, 3) == 1:
    print(colors.yellow("The Kibble Bag dropped some kibble"))
    return 1
    
  else:
    return 0


def damage_calculation(attacker1_health, attacker2_health, attacker1_name, attacker2_name):
  """Calculate damage based on randomly generated int

  :param attacker1_health: an int 
  :preconditon: must be a positive integer
  :param attacker2_health: an int
  :preconditon: must be a positive integer
  :param attacker1_name: a string
  :preconditon: a string
  :param attacker2_name: a string
  :preconditon: a string
  :postcondition: calculates damage dealt between attacker1_name and attacker2_name and prints results
  :return: two integers (attacker1_health, attacker2_health)
  """
  damage = random.randint(1, 6)
  attacker2_health -= damage
  print(f"{attacker1_name} {damage_speech_constant()[damage - 1]} {attacker2_name} [{colors.red(damage)}]")
  
  if attacker2_health > 0:
      damage = random.randint(1, 6)
      attacker1_health -= damage
      print(f"{attacker2_name} {damage_speech_constant()[damage - 1]} {attacker1_name} [{colors.red(damage)}]")
      return attacker1_health, attacker2_health
      
  else:
      return attacker1_health, attacker2_health


def fight(player_health):
  """Calculate damage dealt until somebody dies

  :param player_health: an int
  :precondition: a positive integer
  :postconditon: continues to calculate damage to player and enemy until either of them dies
  :return a string(player_health), an int(kibble)
  """
  enemy_health = 5
  enemy = "Kibble Bag"
  while player_health > 0 and enemy_health > 0:
    enemy_roll = random.randint(1, 20)
    player_roll = random.randint(1, 20)
    
    if enemy_roll > player_roll:
      enemy_health, player_health = damage_calculation(enemy_health, player_health, f"the {enemy}", "You")

    elif enemy_roll < player_roll:
      player_health, enemy_health = damage_calculation(player_health, enemy_health, "You", f"the {enemy}")
  player_health, kibble = victorious(player_health, enemy_health, enemy)
  return player_health, kibble
    

def victorious(player_health, enemy_health, enemy):
  """Determine if the player or enemy won the fight

  :param player_health: an int
  :precondition: an integer positive or negative
  :param enemy_health: an int
  :precondition: an integer positive or negative
  :param enemy: a string
  :precondition: a string
  :return:
  """
  if player_health <= 0:
    print(colors.red("You were killed in combat"))
    quit()
    
  elif enemy_health <= 0:
    print(colors.green(f"You killed the {enemy}"))
    kibble = health_drop()
    return player_health, kibble


def flee(player_health):
  """Determine if player takes damage from randomly generated number

  :param player_health: an int
  :precondition: must be a positive integer
  :postconditon: generate random int, if random int is 1, generate another random int and deal damage to player
  :return: an int
  """
  if random.randint(1, 10) == 1:
    damage = random.randint(1, 4)
    player_health -= damage

    if player_health > 0:
      print(f"You took [{colors.red(damage)}] damage while running away and now have {colors.cyan(player_health)} hp")
      return player_health
      
    else:
      print(colors.red("You died trying to get away"))
      quit()
      
  else:
    print(colors.green("You got away safely"))
    return player_health


def combat(player_health):
  """Ask user for input and call helper function

  :param player_health: an int
  :precondition: must be a positive integer
  :postcondition: if user input is attack, calls fight function, if user input is flee, calls flee function
  :return: three integers
  """
  combat_state = 0
  while combat_state == 0:
    user_input = input("What would you like to do:\n1. Attack\n2. Flee\n")
    
    if user_input in valid_options_constant():
      combat_state += 1

      if user_input == "1":
        remaining_health, kibble = fight(player_health)
        print(f"Your remaining health is {colors.cyan(remaining_health)}")
        return remaining_health, 1, kibble
        
      elif user_input == "2":
        remaining_health = flee(player_health)
        return remaining_health, 0, 0

      elif user_input == "quit":
        quit()
        
    else:
      print(colors.red("Invalid input"))
