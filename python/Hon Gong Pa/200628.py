# 조건문 사용하여 양수, 음수, 0 판정
a = float(input("실수를 입력하세요."))

if a > 0:
    print("양수입니다")

if a == 0:
    print("0입니다")

if a < 0:
    print("음수입니다")

# 날짜/시간 활용하기

import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))


if now.hour < 12:
    print("현재 시각은 오전 {}시입니다.".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 오후 {}시입니다.".format(now.hour - 12))


# 계절 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄이다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름이다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을이다.".format(now.month))

if now.month == 12 or now.month <= 2:
    print("이번 달은 {}월로 겨울이다.".format(now.month))