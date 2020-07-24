def order(sen):
    if sen == "":
        return ""
    sen_list = list(sorted(sen.split(" ")))
    index_list = []
    for i in sen_list:
        index_list.append("".join(sorted(i))[0])
    return " ".join([x for _,x in sorted(zip(index_list,sen_list))])




#def order(sen):
#    return " ".join(sorted(sen.split(), key=lambda x: int("".join(filter(str.isdigit, x)))))

sen = "df3 sdfkjn2dkflj 1dsf f4fdsfn"
print(order(sen))


# 1. isdigit()
# "문자열".isdigit()처럼 사용하지만
# filter(함수, 리스트) 등에 들어갈 때는
# filter(str.isdigit, x) 처럼 str.isdigit 함수를 만들고 x는 매개변수
# 
# 2. sorted 함수의 기본 매개변수 key
# key = lambda ~ 형태로 많이 사용한다.