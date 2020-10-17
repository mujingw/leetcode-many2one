from node.ListNode import ListNode
from list_traversal.get_all_list_elements import get_all_list_elements_sorted


def get_length(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next_node

    return count


def find_mid(head):
    if not head or not head.next_node:
        return head

    prev, slow, fast = None, head, head

    while fast and fast.next_node:
        prev = slow
        slow = slow.next_node
        fast = fast.next_node.next_node

    prev.next_node = None

    return slow

# 21. Merge Two Sorted Lists


def merge_sorted(l1, l2):
    dummy = ListNode(float("inf"))
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next_node = l1
            l1 = l1.next_node
        else:
            curr.next_node = l2
            l2 = l2.next_node

        curr = curr.next_node

    while l1:
        curr.next_node = l1
        curr = curr.next_node
        l1 = l1.next_node

    while l2:
        curr.next_node = l2
        curr = curr.next_node
        l2 = l2.next_node

    return dummy.next_node


assert(0 == get_length(None))
assert(1 == get_length(ListNode(1)))
assert(3 == get_length(ListNode(1, ListNode(2, ListNode(3)))))

assert(3 == find_mid(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))).val)
assert(2 == find_mid(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))).val)

test_l1 = ListNode(1, ListNode(3, ListNode(4)))
test_l2 = ListNode(2, ListNode(5))
assert([1, 2, 3, 4, 5] == get_all_list_elements_sorted(merge_sorted(test_l1, test_l2), None))
