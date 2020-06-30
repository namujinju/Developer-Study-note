# 영어 문자열 리스트를 입력받는다. 
# 대소문자 구분 없이 중복된 문자가 있으면 제외, 없으면 capitalize 해서 출력하는 함수를 만들어라.


# 대소문자 구분 없이 중복된 문자가 없는지 체크하는 함수
def check_no_repeat(text):
    return len(set(text.lower())) == len(text)

# 풀이 함수
def my_sol(text):

    # 제외하기
    checked_list = list(filter(check_no_repeat, text))

    # Capitalize 하기
    # capitalize 함수를 lambda로 지정, map으로 새 리스트 만들기
    capi = lambda x: x.title()
    
    return list(map(capi, checked_list))

text = ["tycHus finDlaY", "FENIX", "sArah KeRRigan", "JiM rAYNor", "VoRaZuN"]

my_sol(text)


