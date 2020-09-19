# 904. Fruit Into Baskets

from len_longest_substring_2_distinct import len_longest_substring_2_distinct


def total_fruits(tree):
    return len_longest_substring_2_distinct(tree)


assert (3 == total_fruits([1, 2, 1]))
assert (3 == total_fruits([0, 1, 2, 2]))
assert (4 == total_fruits([1, 2, 3, 2, 2]))
assert (5 == total_fruits([3,3,3,1,2,1,1,2,3,3,4]))