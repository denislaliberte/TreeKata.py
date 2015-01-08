import unittest
from Tree import Tree

class Tree_test(unittest.TestCase):
  def test_canary(self):
    self.assertEqual(True,True)
  def test_get_node_value(self):
    tree = Tree(1)
    self.assertEqual(tree.getValue(),1)
  def test_add_first_child(self):
    tree = Tree(1)
    tree.add(2)
    self.assertEqual(tree.search(2).getValue(),2)