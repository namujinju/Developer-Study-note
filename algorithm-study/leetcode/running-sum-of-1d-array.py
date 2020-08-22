def runningSum(nums):
    result = [nums[0]]
    for i in nums[1:]:
        result.append(result[-1]+i)
    return result


nums = [1, 2, 3, 4]
print(runningSum(nums))
