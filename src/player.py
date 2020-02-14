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
      return carrying
    else:
      return 'You are carrying nothing\n'

  def movePlayer(self, direction):
    # check if theres a vaild room in the direction given
    # if so, update the current position and print
    newRoom = getattr(self.currentRoom, f'{direction}_to')
    if newRoom is not None:
      self.currentRoom = newRoom
      print(self.currentRoom)
    else:
      print('Sorry, cannot go that way...', '\n')

  def get(self, chosenItem):
    availableItems = [item.name.lower() for item in self.currentRoom.items]
    if chosenItem in availableItems:
      for item in self.currentRoom.items:
        if item.name.lower() == chosenItem:
          self.items.append(item)
          self.currentRoom.items.remove(item)
          print(f'You are now carrying a {item.name}')

  def drop(self, chosenItem):
    currentItems = [item.name.lower() for item in self.items]
    if chosenItem in currentItems:
      for item in self.items:
        if item.name.lower() == chosenItem:
          self.items.remove(item)
          self.currentRoom.items.append(item)
          print(f'You are no longer carrying a {item.name}')
