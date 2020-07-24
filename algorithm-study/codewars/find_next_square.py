def find_next_square(sq):
    n = (sq ** 0.5 + 1) ** 2
    if int(n) == n:
        return n
    else:
        return -1

# 참고
# x = sq**0.5
# return -1 if x % 1 else (x+1)**2