def findUnsortedSubarray(nums):
    n = len(nums)
    srtd = sorted(nums)
    for i in range(n):
        if nums[i] != srtd[i]:
            left = i
            break
    else:
        return 0

    for i in range(n-1, 0-1, -1):
        if nums[i] != srtd[i]:
            right = i
            break

    return right-left+1


def findUnsortedSubarray2(nums):
    n = len(nums)
    a = -float("inf")
    b = float("inf")

    for i in range(n):
        if nums[i] < nums[i-1]:
            b = min(b, nums[i])
    for i in range(n-2, 0-1, -1):
        if nums[i] > nums[i+1]:
            a = max(a, nums[i])

    for l in range(n):
        if b < nums[l]:
            break

    for r in range(n-1, 0-1, -1):
        if a > nums[r]:
            break

    if r <= l:
        return 0
    else:
        return r-l+1


nums = [1]
print(findUnsortedSubarray2(nums))
