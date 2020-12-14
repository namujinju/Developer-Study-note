from math import*
from random import choice, randrange, sample, shuffle
print(sin(1))

print(ceil(2.6))

print(tau)

print()

list_a = [1,2,3,4,5]
print(choice(list_a))
print(sample(list_a, k=3))
print(choice(list_a))
shuffle(list_a)
print(list_a)

print()

# sys모듈

import sys

print(sys.argv)

# os 모듈
import os
# 
# print(os.name)
# print(os.getcwd())
# print(os.listdir())

# datetime 모듈

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# 문자열 리스트 등 앞에 *을 붙이면 요소 하나하나가 매개변수로 지정

import time
print("시간 정지 5초")
time.sleep(3)
print("시간 정지 완료")

# urllib 모듈

# from urllib import request
# 
# target = request.urlopen("https://www.naver.com")
# output = target.read()
# print(output)
# 