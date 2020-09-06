# 284. Peeking Iterator

class BSTPeekingIterator(object):
    def __init__(self, bst_iterator):
        self.iter = bst_iterator
        self.peeked = False
        self.peeked_val = None

    def has_next(self):
        return self.peeked or self.iter.has_next()

    def next_val(self):
        if self.peeked:
            next_val = self.peeked_val
            self.peeked_val = None
            self.peeked = False

            return next_val
        else:
            return self.iter.next_val()

    def peek(self):
        if not self.peeked:
            self.peeked = True
            self.peeked_val = self.iter.next_val()

        return self.peeked_val
