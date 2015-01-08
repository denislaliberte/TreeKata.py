
class Tree:
  value = False
  left = False
  right = False
  def __init__(self,value):
    self.value = value
  def getValue(self):
    return self.value
  def add(self,value):
    if value > self.value:
      if self.right:
        self.right.add(value)
      else:
        self.right = Tree(value)
    else:
      if self.left:
        self.left.add(value)
      else:
        self.left = Tree(value)
  def search(self,value):
    if value > self.value:
      return self.right
    elif value < self.value:
      return self.left
    else:
      return self

