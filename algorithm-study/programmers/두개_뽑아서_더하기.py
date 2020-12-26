from itertools import combinations as comb

def solution(numbers):
    comb_array = comb(numbers, 2) # combination(조합)으로 numbers 배열의 두 원소를 뽑은 튜플의 집합 배열을 생성

    sum_array = map(lambda x: x[0]+x[1], comb_array) # 각 튜플의 원소들을 map을 이용해 더한다.
    # sum_array = [x[0]+x[1] for x in comb_array] # list comprehension을 이용하는 방법

    answer = list(set(sum_array)) # set으로 중복을 제거한다. 자동으로 오름차순으로 정렬된다. 리스트로 변환.

    return answer

# 테스트
numbers = [2,1,3,4,1]
solution(numbers)

