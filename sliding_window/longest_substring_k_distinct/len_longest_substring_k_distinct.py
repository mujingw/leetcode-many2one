# 340. Longest Substring with At Most K Distinct Characters

import collections


def len_longest_substring_k_distinct(s, k):
    res = 0
    left, right = 0, 0
    window = collections.defaultdict(int)

    while right < len(s):
        ch = s[right]
        right += 1
        window[ch] += 1

        while len(window) > k:
            ch = s[left]
            left += 1
            window[ch] -= 1

            if window[ch] == 0:
                del window[ch]

        res = max(res, right - left)

    return res


assert (3 == len_longest_substring_k_distinct("eceba", 2))
assert (2 == len_longest_substring_k_distinct("aa", 1))
