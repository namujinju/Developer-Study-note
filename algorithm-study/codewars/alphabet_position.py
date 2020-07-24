
# 내 코드

# def alphabet_position(text):
#     import string     
#     list_a = []
#     for i in text:
#         pos = ord(i.lower()) - 96
#         if pos > 0:
#             list_a.append(str(pos))
#     return " ".join(list_a)

# 모범 답안

def alphabet_position(text):
    return " ".join(str(ord(c.lower()) - 96) for c in text if c.isalpha()) # 배열 전체를 join으로 조합

