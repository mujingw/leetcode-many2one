from PeekingIterator import PeekingIterator


def merge_using_iterator(iter1, iter2):
    peeking_iter1, peeking_iter2 = PeekingIterator(iter1), PeekingIterator(iter2)
    res = []

    while peeking_iter1.has_next() and peeking_iter2.has_next():
        if peeking_iter1.peek() < peeking_iter2.peek():
            res.append(peeking_iter1.next_val())
        else:
            res.append(peeking_iter2.next_val())

    while peeking_iter1.has_next():
        res.append(peeking_iter1.next_val())

    while peeking_iter2.has_next():
        res.append(peeking_iter2.next_val())

    return res
