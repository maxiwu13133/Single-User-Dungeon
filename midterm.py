"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.

Ralph Li
Maximilian Wu
"""
import map_grid
import boss
import colors
import doctest


def game():
    """Run the game

  :postcondition: calls helper functions to run the game
  :return: string of text
  """
    print("""
    You wake up one day in an open field.
    \"Where am I?\" you wondered. Suddenly,
    you hear a booming voice, \"You have commited
    the highest level of treason. You have forgotten
    to feed the almighty cat this lunch. For this you
    must attone for you sins and collect ten bags of
    kibble...\"
      """)

    input(colors.green("Enter any key to continue...\n"))
    player_health = 10
    coord = [2, 2]
    map_grid.map_draw(coord)
    enemies_killed = 0
    kibble = 0

    while enemies_killed != 10:
        player_health, killed, kibble_gained = map_grid.map_board(coord, player_health)
        enemies_killed += killed
        kibble += kibble_gained
        print(colors.green(enemies_killed))

    boss.boss(player_health, kibble)
    print("""
    Exhausted from the fight you decide to take a break 
    and take a nap on the field. You awake in your bedroom
    and you hear your cat meowing outside. You check the time, 
    it's her lunch time, so you quickly rush out to feed her. 
    While pouring the kibble you wonder, \"Was that all just a dream...\"
  """)


def menu():
    """Determine if player wants to play, see controls, or quit

  :preconditions: there must be no param inputted
  :postcondition: will quit game, print controls, or call game() 
  """
    menu_state = 0
    while menu_state == 0:
        print(
            """
--------------------------------------
Welcome       /\\_______/\\
To           (  0     0  ) - meow
Kibble        \ == o == /
Land           \_______/
--------------------------------------
---------------------
\'P\' to play
\'C\' for controls
\'Quit\' to quit  
----------------------      
    """
        )
        player_input = input().lower()
        if player_input == 'p':
            menu_state += 1
            game()  # calls game

        elif player_input == 'c':
            print(
                """
--------------------------------------
Movement:
\'1\' moves you up
\'2\' moves you down
\'3\' moves you left
\'4\' moves you right
__________________________
Combat:
\'1\' fight enemy TO THE DEATH
\'2\' leave the fight
--------------------------------------
      """
            )
        elif player_input == 'quit':
            quit()

        else:
            print(colors.red("This is an invalid input"))


def main():
    """Drives the program."""
    menu()
    # doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
