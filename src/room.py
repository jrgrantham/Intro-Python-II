# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    self.items = items

  def returnItems(self):
    output = '  Contents: '
    if self.items:
      for item in self.items:
        output += f'{item.name}, '
    else:
      output += 'This place is empty.'
    return output

  def __str__(self):
    roomDetails = ''
    roomDetails += f'Location:   {self.name}\n'
    roomDetails += f'  Info:     {self.description}\n'
    roomDetails += f'{self.returnItems()}\n'
    return roomDetails