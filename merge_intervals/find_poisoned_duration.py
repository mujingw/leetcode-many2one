# 495. Teemo Attacking

from merge_intervals import merge


def find_poisoned_duration(start_times, duration):
    if not start_times:
        return 0

    res, intervals = 0, []

    for s in start_times:
        intervals.append([s, s + duration])

    merged = merge(sorted(intervals, key=lambda x: (x[0], -x[1])))

    for interval in merged:
        res += (interval[1] - interval[0])

    return res


assert (4 == find_poisoned_duration([1, 4], 2))
assert (3 == find_poisoned_duration([1, 2], 2))
