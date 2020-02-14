from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east. """),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Define room contents

# room['foyer'].items = ['torch', 'axe', 'bucket']

room['foyer'].items = [Items('torch', 'you need this to see in the dark'), Items('axe', 'this might be useful for...')]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print('\n -------------------------------\n',
'Welcome to your new adventure!!\n',
'-------------------------------\n')

name = input('Please enter your name : ')
player = Player(name, room['outside'])

print(player)
print(player.currentRoom)

directions = ['n', 's', 'e', 'w']

while True:

    playerInput = ''
    playerInput = input(
        'Please select an action:\n  To move, enter n, s, e, w\n  To get, or drop enter g or d + item\n  To quit, enter q\n  Input: ')

    print(f'  You entered \'{playerInput}\'\n-------------------------------------\n')
    splitInput = playerInput.split(' ')

    if playerInput in directions:
        player.movePlayer(playerInput)
    elif playerInput == 'q':
        print("\nGoodbye!!\n")
        exit()
    elif playerInput == 'p':
        print(player.carrying())
    elif len(splitInput) == 2:
        if splitInput[0] == 'g':
            print(splitInput[1])
            player.get(splitInput[1])
        elif splitInput[0] == 'd':
            player.drop(splitInput[1])
    else:
        print('  Invalid entry, please try again\n')
