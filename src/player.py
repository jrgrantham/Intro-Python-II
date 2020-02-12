# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, currentRoom):
    self.name = name
    self.currentRoom = currentRoom

  def __str__(self):
    return f'\nWelcome, {self.name}.\n'

  def movePlayer(self, direction):
    # check if theres a vaild room in the direction
    # if so, update the current position and print
    if getattr(self.currentRoom, f'{direction}_to') is not None:
      self.currentRoom = getattr(self.currentRoom, f'{direction}_to')
      print(self.currentRoom)
    else:
      print('Sorry, cannot go that way...', '\n')
