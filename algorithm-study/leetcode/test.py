nums = [0, 1, 2, 3, 4, 5]
n = 3

print([nums[i//2+n*(i % 2)] for i in range(len(nums))])
