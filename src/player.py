# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, currentRoom):
    self.name = name
    self.currentRoom = currentRoom
    self.carrying = []

  def __str__(self):
    return f'\nHello {self.name}, hope you\'re ready, let\'s get going...\n'

  def movePlayer(self, direction):
    # check if theres a vaild room in the direction given
    # if so, update the current position and print
    if getattr(self.currentRoom, f'{direction}_to') is not None:
      self.currentRoom = getattr(self.currentRoom, f'{direction}_to')
      print(self.currentRoom)
    else:
      print('Sorry, cannot go that way...', '\n')
