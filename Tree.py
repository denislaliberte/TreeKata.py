
class Tree:
  value = None
  left = None
  right = None

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
    if leftHeight > rightHeight:
      return leftHeight + 1
    else:
      return rightHeight + 1

  def is_balanced(self):
    leftHeight =0
    rightHeight =0
    if self.left:
      leftHeight = self.left.heightCount()
    if self.right:
      rightHeight = self.right.heightCount()
    diff = abs(leftHeight - rightHeight)
    return diff <= 1

