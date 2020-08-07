# def rgb(r, g, b):

#     return "".join([("0"+(hex(i).upper())[2:])[-2:] if 0 <= i <= 255 else "00" * (i < 0) + "FF" * (i > 255) for i in [r, g, b]])


# 모범 답안


def rgb(r, g, b):
    def round(x): return min(255, max(x, 0))

    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# 값이 정해진 범위에서 벗어났을 때 min, max를 이용해 그 범위 안으로 값을 집어넣는다.
# 16진수를 표기하는 방법
(r, g, b) = (1, 2, 17)
print(rgb(r, g, b))
