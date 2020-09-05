# 173. Binary Search Tree Iterator

class BSTIterator(object):
    def __init__(self, root):
        self.s = []
        self.push_all_left(root)

    def has_next(self):
        return len(self.s) > 0

    def next_val(self):
        if self.has_next():
            curr = self.s.pop()
            self.push_all_left(curr.right)
            return curr.val
        else:
            return -1

    def peek(self):
        if self.has_next():
            return self.s[-1].val

    def push_all_left(self, root):
        while root:
            self.s.append(root)
            root = root.left
