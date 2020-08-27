from collections import Counter


def majorityElement(nums):
    numsObj = {}
    n = len(nums)

    for i in nums:
        if i in numsObj:
            numsObj[i] += 1
        else:
            numsObj[i] = 1

        if numsObj[i] > n/2:
            return i


def majorityElement2(nums):
    counts = Counter(nums)
    # Counter 객체에서 key값을 가져올 때 get 함수를 쓴다.
    # 그 가져온 key 값을 기준으로 max를 정렬한다.
    return max(counts.keys(), key=counts.get)


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement2(nums))
