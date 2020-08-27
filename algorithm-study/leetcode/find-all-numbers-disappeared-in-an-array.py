def findDisappearedNumbers(nums):
    return list(set([i+1 for i in range(len(nums))])-set(nums))


nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(findDisappearedNumbers(nums))
