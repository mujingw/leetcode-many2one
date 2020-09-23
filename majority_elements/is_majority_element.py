# 1150. Check If a Number Is Majority Element in a Sorted Array

from majority_element_general import get_majority_element


def is_majority_element(nums, num_to_check):
    majority_element_list = get_majority_element(nums, 2)

    return num_to_check in majority_element_list


assert (is_majority_element([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
assert (not is_majority_element([10, 100, 101, 101], 101))
