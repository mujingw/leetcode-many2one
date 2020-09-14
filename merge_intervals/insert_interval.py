# 57. Insert Interval

from merge_intervals import merge


def insert(intervals, new_interval):
    intervals.append(new_interval)

    return merge(intervals)


assert ([[1, 5], [6, 9]] == insert([[1, 3], [6, 9]], [2, 5]))
assert ([[1, 2], [3, 10], [12, 16]] == insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
