# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    self.items = []

  def __str__(self):
    roomDetails = ''
    roomDetails += f'Location:   {self.name}\n'
    roomDetails += f'  Info:     {self.description}\n'

    content = ''
    for item in self.items:
      content =+ item

    roomDetails += f'  Contents: {content}\n'

    return roomDetails