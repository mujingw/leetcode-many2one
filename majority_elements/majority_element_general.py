# This method returns elements that appear
# more than floor(n/k) times in the nums array,
# assuming there are, in total, n elements in the nums array

from collections import Counter


def get_majority_element(nums, k):
    counter = Counter()

    for num in nums:
        counter[num] += 1

        if len(counter) == k:
            for key in counter.keys():
                counter[key] -= 1

                if counter[key] == 0:
                    del counter[key]

    return [element for element in counter.keys() if nums.count(element) > len(nums) / k]


assert ([1] == get_majority_element([1, 1, 2], 2))
assert ([1] == get_majority_element([1, 1, 2], 2))
assert ([] == get_majority_element([1, 2], 2))
assert ([1] == get_majority_element([1, 1, 1, 1, 1, 2, 3, 4, 5, 6], 4))
