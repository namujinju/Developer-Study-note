# 함수 데코레이터

def test(function):
    def wrapper():
        print("인사 시작")
        function()
        print("인사 종료")
    return wrapper


@test
def hello():
    print("hello")



hello()
print()

from sympy import primerange
print(len(list(primerange(100,1000))))

print(__name__)


# 8장 클래스

