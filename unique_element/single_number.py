# 136. Single Number

def single_number(nums):
    return reduce(lambda x, y: x ^ y, nums)


assert (1 == single_number([2, 2, 1]))
assert (9 == single_number([1, 2, 3, 2, 3, 1, 9]))
