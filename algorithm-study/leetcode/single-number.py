from collections import Counter
from functools import reduce
# 내 처음 풀이

# def singleNumber(nums):
#     hash_table = {}
#     for i in nums:
#         if not i in hash_table:
#             hash_table[i] = 1
#         else:
#             del hash_table[i]
#     return list(hash_table.keys())[0]

# 더 나은 풀이


# def singleNumber(nums):
#     hash_table = {}
#     for i in nums:
#         hash_table[i] = 1
#     for i in hash_table:
#         if hash_table[i] == 1:
#             return i


# def singleNumber(nums):
#     dict_counter = Counter(nums)
#     for i in dict_counter:
#         if dict_counter[i] == 1:
#             return i


# 혁명적 풀이
# XOR 연산 이용
def singleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums)


nums = [2, 2, 1]
# nums = [4, 1, 2, 2, 1]
print(singleNumber(nums))
