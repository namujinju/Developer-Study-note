def maxSubArray(nums):
    result, maxv = 0, 0
    if all(i < 0 for i in nums):
        return max(nums)  # 모든 원소가 음수일 때 그 중 가장 큰 수를 return
    else:

        for i in nums:
            result += i
            if result < 0:
                result = 0
            if maxv < result:
                maxv = result
        return maxv


nums = [-2, -1]
print(maxSubArray(nums))
