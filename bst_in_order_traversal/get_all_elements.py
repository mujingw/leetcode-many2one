# 1305. All Elements in Two Binary Search Trees

from BSTIterator import BSTIterator
from util.merge_using_iterator import merge_using_iterator
from node.TreeNode import TreeNode


def get_all_elements(root1, root2):
    return merge_using_iterator(BSTIterator(root1), BSTIterator(root2))


test_root1 = TreeNode(2)
test_root1.left = TreeNode(1)
test_root1.right = TreeNode(4)
test_root2 = TreeNode(1)
test_root2.left = TreeNode(0)
test_root2.right = TreeNode(3)
assert ([0, 1, 1, 2, 3, 4] == get_all_elements(test_root1, test_root2))
