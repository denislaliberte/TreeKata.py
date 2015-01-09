import unittest
from Tree import Tree

class Tree_test(unittest.TestCase):

  def test_get_node_value(self):
    tree = Tree(1)
    self.assertEqual(tree.getValue(),1)

  def test_not_found(self):
    tree = Tree(1)
    self.assertEqual(tree.search(2),None)

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
    tree.addMultiple([5,3,7,15,13,17])
    self.assertEqual(tree.search(3).getValue(),3)
    self.assertEqual(tree.search(13).getValue(),13)

  def test_3_level_of_children_tree(self):
    tree = Tree(10)
    tree.addMultiple([5,3,7,15,13,17,1,4,6,8,11,14,16,19])
    self.assertEqual(tree.search(10).getValue(),10)
    self.assertEqual(tree.search(13).getValue(),13)
    self.assertEqual(tree.search(1).getValue(),1)
    self.assertEqual(tree.search(7).getValue(),7)

  def test_get_one_level_height(self):
    tree = Tree(10)
    self.assertEqual(tree.heightCount(),1)

  def test_get_two_level_height(self):
    tree = Tree(10)
    tree.add(5)
    self.assertEqual(tree.heightCount(),2)

  def test_get_right_height(self):
    tree = Tree(10)
    tree.addMultiple([11,13])
    self.assertEqual(tree.heightCount(),3)

  def test_not_balanced(self):
    tree = Tree(10)
    tree.addMultiple([15,17,18])
    self.assertFalse(tree.is_balanced())

  def test_balanced(self):
    tree = Tree(10)
    tree.addMultiple([5,15])
    self.assertTrue(tree.is_balanced())

  def test_balanced_sub_tree(self):
    tree = Tree(10)
    tree.addMultiple([5,4,3,2,15,16,13,17])
    self.assertFalse(tree.is_balanced())
