# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, currentRoom, items=[]):
    self.name = name
    self.currentRoom = currentRoom
    self.items = items

  def __str__(self):
    return f'\nHello {self.name}, hope you\'re ready, let\'s get going...\n'

  def carrying(self):
    carrying = 'You are carrying:\n'
    for item in self.items:
      carrying += f'{item}, '
    if self.items:
      print(carrying)
    else:
      print('You are carrying nothing\n')

  def movePlayer(self, direction):
    # check if theres a vaild room in the direction given
    # if so, update the current position and print
    newRoom = getattr(self.currentRoom, f'{direction}_to')
    if newRoom is not None:
      self.currentRoom = newRoom
      print(self.currentRoom)
    else:
      print('Sorry, cannot go that way...', '\n')

  def get(self):
    print(self.currentRoom.items)