from node.ListNode import ListNode


class ListIterator(object):
    def __init__(self, head_node):
        self.curr = ListNode(-1)
        self.curr.next_node = head_node

    def has_next(self):
        return self.curr.next_node is not None

    def next_val(self):
        if self.has_next():
            self.curr = self.curr.next_node
        else:
            return -1

        return self.curr.val
