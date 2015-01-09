
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
    leftHeight = self.left.heightCount() if self.left else 0
    rightHeight = self.right.heightCount() if self.right else 0
    return  leftHeight + 1 if leftHeight > rightHeight else rightHeight + 1

  def is_balanced(self):
    childrenHeightisEqual = self.childrenHeightIsEqual()
    childrensIsBalanced = self.childrensIsBalanced()
    return (childrenHeightisEqual and childrensIsBalanced)

  def childrensIsBalanced(self):
    leftBalanced = self.left.is_balanced() if self.left else True
    rightBalanced = self.right.is_balanced() if self.right else True
    return (leftBalanced and rightBalanced)

  def childrenHeightIsEqual(self):
    leftHeight = self.left.heightCount() if self.left else 0
    rightHeight = self.right.heightCount() if self.right else 0
    return ( abs(leftHeight - rightHeight) <= 1)

