
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
      self.right = Tree(value)
    else:
      self.left = Tree(value)
  def search(self,value):
    if value > self.value:
      return self.right
    else:
      return self.left
