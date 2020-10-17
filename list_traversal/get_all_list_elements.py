from ListIterator import ListIterator
from util.get_all_using_iterator import get_all_elements_sorted
from node.ListNode import ListNode


def get_all_list_elements_sorted(l1, l2):
    if l1 is None:
        return get_all_elements_sorted(ListIterator(l2), None)

    if l2 is None:
        return get_all_elements_sorted(ListIterator(l1), None)

    return get_all_elements_sorted(ListIterator(l1), ListIterator(l2))


test_l1 = ListNode(1)
test_l1.next_node = ListNode(2)
test_l1.next_node.next_node = ListNode(4)
test_l2 = ListNode(1)
test_l2.next_node = ListNode(3)
test_l2.next_node.next_node = ListNode(4)
assert ([1, 1, 2, 3, 4, 4] == get_all_list_elements_sorted(test_l1, test_l2))
assert ([1, 2, 4] == get_all_list_elements_sorted(test_l1, None))
assert ([1, 3, 4] == get_all_list_elements_sorted(None, test_l2))
