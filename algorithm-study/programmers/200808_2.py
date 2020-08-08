# 폰켓몬


def solution(nums):
    return min(len(set(nums)), len(nums)/2)


nums = [3, 3, 3, 2, 2, 4]
print(solution(nums))
