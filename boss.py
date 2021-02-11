import random
import colors
import doctest

def damage_speech_constant():
  DAMAGE_SPEECH = (colors.green('tickled'), colors.yellow('pierced'), 
  colors.red('amputated'), colors.magenta('obliterated'), 
  colors.cyan("decimated"), colors.blue("deleted"))
  return DAMAGE_SPEECH

def attacking(player_dodge, boss_attack, player_health, boss_health):
  """Calculate damage to boss and player from randomly generated integers

  :param player_dodge: an int
  :precondition: must be a positive integer between 1 and 2
  :param boss_attack: an int
  :precondition: must be a positibe integer between 1 and 2
  :param player_health: an int
  :precondition: must be a positive integer
  :param boss_health: an int
  :precondition: must be a positive integer
  :postcondition: calculates damage dealt to player and boss and prints result
  :return: two integers (boss_health, player_health)
  """
  if int(player_dodge) == boss_attack:
    damage = random.randint(1, 3)
    player_health -= damage
    print(f"You took {colors.red(damage)} damage\nCurrent health: {colors.cyan(player_health)}")
    damage = random.randint(1, 6)
    boss_health -= damage
    print(f"You {damage_speech_constant()[damage - 1]} King Kibble [{colors.red(damage)}]")
    return boss_health, player_health

  else:
    print(colors.yellow("You managed to dodge the attack!"))
    damage = random.randint(1, 6)
    boss_health -= damage
    print(f"You {damage_speech_constant()[damage - 1]} King Kibble [{colors.red(damage)}]")
    return boss_health, player_health


def regain_health(player_health, kibble):
  """Heal player using kibble

  :param player_health: an int 
  :precondition: must be a positive integer 
  :param kibble: an int 
  :precondition: must be a positive integer 
  :postcondition: increase player_health using kibble 
  :return: two integers (player_health, kibble)
  """
  if kibble != 0:
    if player_health < 9:
      player_health += 2
      kibble -= 1
      print(f'You ate a bit of kibble\nCurrent health: {colors.cyan(player_health)}')
      return player_health, kibble

    elif player_health == 9:
      player_health += 1
      kibble -= 1
      print(f'You ate a bit of kibble\nCurrent health: {colors.cyan(player_health)}')
      return player_health, kibble

    else:
      print(f'You are max health\nCurrent health: {colors.cyan(player_health)}')
      return player_health, kibble

  else:
    print(colors.red("You are out of kibble"))
    return player_health, kibble


def boss(player_health, kibble):
  """Ask user for input and call helper functions 

  :param player_health: an int
  :precondition: must be a positive integer 
  :param kibble: an int
  :precondition: must be a positive integer
  :postcondition: ask user input and calls regain_health() if it's 3, attacking() if it's 1 or 2
  :return: prints results 
  """
  boss_health = 25
  print(colors.red("King Kibble has arrived! You must dodge left or right to avoid his attacks"))

  while boss_health > 0 and player_health > 0:
    print(f"1. Dodge right\n2. Dodge left\n3. Heal (You have {kibble} kibble)")
    choice = input()

    if choice == 'quit':
      quit()

    if choice == "1" or choice == "2":
      attack_side = random.randint(1, 2)
      boss_health, player_health = attacking(choice, attack_side, player_health, boss_health)

    elif choice == "3":
      player_health, kibble = regain_health(player_health, kibble)

    else:
      print("Invalid Input")

  if player_health < 0:
    print(colors.red("King Kibble has ground you to a pulp R.I.P"))
    quit()

  elif boss_health < 0:
    print(colors.green("Congrats! You have defeated King Kibble"))
    