# def rob(nums):
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return max(nums)

#     return max(rob(nums[:-2])+nums[-1], rob(nums[:-1]))

def rob(nums):
    n = len(nums)
    if not nums:
        return 0
    obj = {}
    obj[0] = 0
    obj[1] = nums[0]
    for i in range(2, n+1):
        obj[i] = max(obj[i-2] + nums[i-1], obj[i-1])
    return obj[n]


# memoization 없이
def rob2(nums):
    if not nums:
        return 0
    prevRob = maxRob = 0
    for i in range(0, len(nums)):
        temp = maxRob
        maxRob = max(prevRob+nums[i], maxRob)
        prevRob = temp
    return maxRob


nums = [183, 219, 57, 193, 94, 233]
print(rob(nums))
