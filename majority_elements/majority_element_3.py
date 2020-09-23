# 229. Majority Element II

from majority_element_general import get_majority_element


def majority_element(nums):
    return get_majority_element(nums, 3)


assert ([3] == majority_element([3, 2, 3]))
assert ([1, 2] == majority_element([1, 1, 1, 3, 3, 2, 2, 2]))
assert ([] == majority_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
assert ([] == majority_element([1, 2, 3, 4, 5, 6, 7, 8]))
assert ([] == majority_element([1, 2, 3, 4]))
assert ([1] == majority_element([1, 1, 1, 2]))
assert ([1] == majority_element([1, 2, 1, 1]))
