# 짝수와 홀수 구분

num = input()
num_end = int(num[-1])
if num_end % 2 == 0:
    print("짝수")

if num_end % 2 == 1:
    print("홀수")

if num_end > 0:
    raise NotImplementedError

