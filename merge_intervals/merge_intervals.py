# 56. Merge Intervals

def merge(intervals):
    res = []
    intervals.sort(key=lambda x: x[0])
    curr_s, curr_e = intervals[0][0], intervals[0][1]

    for i, v in enumerate(intervals):
        next_s, next_e = v[0], v[1]

        if curr_e < next_s:
            res.append([curr_s, curr_e])
            curr_s, curr_e = next_s, next_e
        else:
            curr_e = max(curr_e, next_e)

    res.append([curr_s, curr_e])

    return res


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]
assert (merge(intervals1) == [[1, 6], [8, 10], [15, 18]])
assert (merge(intervals2) == [[1, 5]])