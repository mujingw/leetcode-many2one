# 169. Majority Element

from majority_element_general import get_majority_element


def majority_element(nums):
    return get_majority_element(nums, 2)


assert ([2] == majority_element([2, 2, 1, 1, 1, 2, 2]))
assert ([3] == majority_element([3, 2, 3]))
