# 1305. All Elements in Two Binary Search Trees

from BSTIterator import BSTIterator
from util.get_all_using_iterator import get_all_elements_sorted
from node.TreeNode import TreeNode


def get_all_bst_elements_sorted(root1, root2):
    if not root1:
        return get_all_elements_sorted(None, BSTIterator(root2))

    if not root2:
        return get_all_elements_sorted(BSTIterator(root1), None)

    return get_all_elements_sorted(BSTIterator(root1), BSTIterator(root2))


test_root1 = TreeNode(2)
test_root1.left = TreeNode(1)
test_root1.right = TreeNode(4)
test_root2 = TreeNode(1)
test_root2.left = TreeNode(0)
test_root2.right = TreeNode(3)
assert ([0, 1, 1, 2, 3, 4] == get_all_bst_elements_sorted(test_root1, test_root2))
assert ([0, 1, 3] == get_all_bst_elements_sorted(None, test_root2))
assert ([1, 2, 4] == get_all_bst_elements_sorted(test_root1, None))
