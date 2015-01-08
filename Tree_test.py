import unittest
from Tree import Tree

class Tree_test(unittest.TestCase):
  def test_get_node_value(self):
    tree = Tree(1)
    self.assertEqual(tree.getValue(),1)
  def test_add_first_child(self):
    tree = Tree(1)
    tree.add(2)
    self.assertEqual(tree.search(2).getValue(),2)
  def test_add_second_child(self):
    tree = Tree(2)
    tree.add(1)
    tree.add(3)
    self.assertEqual(tree.search(1).getValue(),1)
  def test_add_third_child(self):
    tree = Tree(2)
    tree.add(1)
    tree.add(3)
    tree.add(4)
    self.assertEqual(tree.search(3).getValue(),3)
  def test_add_two_left_child(self):
    tree = Tree(5)
    tree.add(1)
    tree.add(3)
    self.assertEqual(tree.search(1).getValue(),1)
  def test_2_level_of_children_tree(self):
    tree = Tree(10)
    for value in [5,3,7,15,13,17]:
      tree.add(value)
    self.assertEqual(tree.search(3).getValue(),3)
    self.assertEqual(tree.search(13).getValue(),13)
  def test_3_level_of_children_tree(self):
    tree = Tree(10)
    for value in [5,3,7,15,13,17,1,4,6,8,11,14,16,19]:
      tree.add(value)
    self.assertEqual(tree.search(10).getValue(),10)
    self.assertEqual(tree.search(13).getValue(),13)
    self.assertEqual(tree.search(1).getValue(),1)
    self.assertEqual(tree.search(7).getValue(),7)
  def test_balanced(self):
    tree = Tree(10)
    for value in [5,3,7,15,13,17,]:
      tree.add(value)
    self.assertFalse(tree.is_balanced())


