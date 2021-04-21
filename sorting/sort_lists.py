# 148. Sort List

from util.ListUtil import find_mid_split
from util.ListUtil import merge_sorted
from node.ListNode import ListNode
from list_traversal.get_all_list_elements import get_all_list_elements_sorted


def sort_list(head):
    if not head or not head.next_node:
        return head

    if not head.next_node.next_node:
        first = head
        second = head.next_node

        if first.val > second.val:
            second.next_node = first
            first.next_node = None

            return second
        else:
            return first

    mid = find_mid_split(head)
    l1 = sort_list(head)
    l2 = sort_list(mid)

    return merge_sorted(l1, l2)


test_list = ListNode(3, ListNode(1, ListNode(4, ListNode(1, ListNode(5, ListNode(9, ListNode(2, ListNode(6))))))))
assert([1, 1, 2, 3, 4, 5, 6, 9], get_all_list_elements_sorted(None, merge_sorted(test_list, None)))
