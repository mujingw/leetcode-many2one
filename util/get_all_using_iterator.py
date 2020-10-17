from PeekingIterator import PeekingIterator


def get_all_elements_sorted(iter1, iter2):
    res = []

    if not iter1:
        get_remaining_elements(res, iter2)

        return res

    if not iter2:
        get_remaining_elements(res, iter1)

        return res

    peeking_iter1, peeking_iter2 = PeekingIterator(iter1), PeekingIterator(iter2)

    while peeking_iter1.has_next() and peeking_iter2.has_next():
        if peeking_iter1.peek() < peeking_iter2.peek():
            res.append(peeking_iter1.next_val())
        else:
            res.append(peeking_iter2.next_val())

    get_remaining_elements(res, peeking_iter1)
    get_remaining_elements(res, peeking_iter2)

    return res


def get_remaining_elements(res, iterator):
    if not iterator:
        return

    while iterator.has_next():
        res.append(iterator.next_val())
