# 21. Merge Two Sorted Lists

from ListIterator import ListIterator
from util.merge_using_iterator import merge_using_iterator
from node.ListNode import ListNode


def merge_two_lists(l1, l2):
    return merge_using_iterator(ListIterator(l1), ListIterator(l2))


test_l1 = ListNode(1)
test_l1.next_node = ListNode(2)
test_l1.next_node.next_node = ListNode(4)
test_l2 = ListNode(1)
test_l2.next_node = ListNode(3)
test_l2.next_node.next_node = ListNode(4)
assert ([1, 1, 2, 3, 4, 4] == merge_two_lists(test_l1, test_l2))
