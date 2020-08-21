def twosum(nums, target):
    numsObj = {}

    for i in range(len(nums)):
        current = nums[i]
        match = target - current

        if match in numsObj:
            return [i, numsObj[match]]
        else:
            numsObj[current] = i


nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))
