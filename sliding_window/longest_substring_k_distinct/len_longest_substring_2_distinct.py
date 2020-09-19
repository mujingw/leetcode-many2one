# 159. Longest Substring with At Most Two Distinct Characters

from len_longest_substring_k_distinct import len_longest_substring_k_distinct


def len_longest_substring_2_distinct(s):
    return len_longest_substring_k_distinct(s, 2)


assert (3 == len_longest_substring_2_distinct("eceba"))
assert (5 == len_longest_substring_2_distinct("ccaabbb"))