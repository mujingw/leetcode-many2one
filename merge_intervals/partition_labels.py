# 763. Partition Labels

from merge_intervals import merge


def partition_labels(s):
    res, char_to_interval = [], {}

    for i, ch in enumerate(s):
        if ch not in char_to_interval:
            char_to_interval[ch] = [i, i]
        else:
            char_to_interval[ch][1] = i

    merged_intervals = merge(sorted(char_to_interval.values(), key=lambda x: x[0]))

    for interval in merged_intervals:
        res.append(interval[1] - interval[0] + 1)

    return res


s = "ababcbacadefegdehijhklij"
assert ([9, 7, 8] == partition_labels(s))
