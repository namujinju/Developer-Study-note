# 자연수 n을 이진수로 바꾸고 1의 갯수를 센 후 그 갯수를 다시 이진수로 바꾸는 작업을 반복한다.
# 1이 나올 때까지 반복한다.
# 이 작업의 단계 수를 구하는 함수를 작성해라.


def bin_count(n, ans=0):
    if n == 1:
        print(f"n = {n}")
        print(f"steps : {ans}")
        return ans
    else:
        m = bin(n)
        print(f"n = {n} ---> {m}")
        n = bin(n).count("1")
        return bin_count(n, ans+1)

# Test
n = 4703248792347
bin_count(n)
