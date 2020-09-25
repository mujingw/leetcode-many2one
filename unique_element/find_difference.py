# 389. Find the Difference

from single_number import single_number


def find_difference(s, t):
    return chr(single_number(map(lambda x: ord(x), s + t)))


assert ("e" == find_difference("abcd", "abcde"))
assert ("a" == find_difference("loft", "aloft"))
assert ("a" == find_difference("float", "loft"))
