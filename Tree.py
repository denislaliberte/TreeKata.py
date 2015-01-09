
class Tree:
  value = None
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

  def addMultiple(self,values):
    for value in values:
      self.add(value)

  def search(self,value):
    if value == self.value:
      return self
    elif value > self.value and self.right:
      return self.right.search(value)
    elif value < self.value and self.left:
      return self.left.search(value)
    else:
      return None

  def heightCount(self):
    leftHeight = (self.left and self.left.heightCount()) or 0
    rightHeight = (self.right and self.right.heightCount()) or 0
    return (leftHeight > rightHeight and leftHeight + 1) or rightHeight + 1

  def is_balanced(self):
    leftHeight = (self.left and self.left.heightCount()) or 0
    rightHeight = (self.right and self.right.heightCount()) or 0
    leftBalanced = self.left.is_balanced() if self.left else True
    rightBalanced = self.right.is_balanced() if self.right else True
    return (( abs(leftHeight - rightHeight) <= 1) and leftBalanced and rightBalanced)

