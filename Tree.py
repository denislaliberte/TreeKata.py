
class Tree:
  value = False
  children = False
  def __init__(self,value):
    self.value = value
  def getValue(self):
    return self.value
  def test(self):
    return "hello world"
  def add(self,value):
    self.children = Tree(value)
  def search(self,value):
    return self.children
