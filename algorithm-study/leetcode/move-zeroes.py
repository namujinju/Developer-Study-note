# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in nums:
#             if not i:
#                 nums.remove(i)
#                 nums.append(0)

# def moveZeroes(nums):

#     nums.sort(key=lambda x: not x)


# nums = [0, 1, 0, 3, 12]
# print(moveZeroes(nums))

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
