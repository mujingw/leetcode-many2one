# 1305. All Elements in Two Binary Search Trees

from BSTIterator import BSTIterator
from BSTPeekingIterator import BSTPeekingIterator
from struct.TreeNode import TreeNode


def get_all_elements(root1, root2):
    iter1 = BSTPeekingIterator(BSTIterator(root1))
    iter2 = BSTPeekingIterator(BSTIterator(root2))
    res = []

    while iter1.has_next() and iter2.has_next():
        if iter1.peek() < iter2.peek():
            res.append(iter1.next_val())
        else:
            res.append(iter2.next_val())

    while iter1.has_next():
        res.append(iter1.next_val())

    while iter2.has_next():
        res.append(iter2.next_val())

    return res


test_root1 = TreeNode(2)
test_root1.left = TreeNode(1)
test_root1.right = TreeNode(4)
test_root2 = TreeNode(1)
test_root2.left = TreeNode(0)
test_root2.right = TreeNode(3)
assert ([0, 1, 1, 2, 3, 4] == get_all_elements(test_root1, test_root2))
