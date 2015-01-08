import unittest
from Tree import Tree

class Tree_test(unittest.TestCase):
  def test_canary(self):
    self.assertEqual(True,True)
  def test_get_node_value(self):
    tree = Tree(1)
    self.assertEqual(tree.getValue(),1)
