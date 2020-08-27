def shuffle(nums, n):
    return [nums[i//2+n*(i % 2)] for i in range(len(nums))]


def shuffle2(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans
