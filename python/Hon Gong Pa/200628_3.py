list_a = ['안', '녕', '하', '세', '요']
list_a[-1] = '염'
print(list_a)

list_a = ['247','나무진주']
print(list_a[1][3]) # 리스트 안의 리스트

list_b = ['하이욤', '안녕?']
print("list_a + list_b = ", list_a + list_b)
print(len(list_a + list_b))
print(list_b * 3)

# 리스트에 요소 추가하기

list_a.append("구슬")
print(list_a)

list_a.insert(2, "사이")
print(list_a)
print(list_b)

list_a.extend(list_b) # 세 개 다 원본이 바뀌는 파괴적 함수
print(list_a)

list_a = [0, 1, 2, 3, 4]
del list_a[3]
print(list_a)
list_a = [0, 1, 2, 3, 4]
list_a.pop(2)
print(list_a)
list_a = [0, 1, 2, 3, 4, 5, 6]
del list_a[2:4]
print(list_a)

list_c = [1, 2, 1, 2, 1, 2]
list_c.remove(2)
print(list_c)

list_a = ['레이너', '타이커스','제라툴']
print('케리건' in list_a)
print('제라툴' in list_a)
print('제라툴' not in list_a)

