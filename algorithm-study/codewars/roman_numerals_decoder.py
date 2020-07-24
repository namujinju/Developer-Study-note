def solution(roman):
    

    dict_roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    list_a = [] # 각 로마자 리스트
    for i in roman:
        list_a.append(dict_roman[i])


    dict_minus = {
        "IX": 2,
        "IV": 2,
        "XL": 20,
        "XC": 20,
        "CD": 200,
        "CM": 200
    }
    list_b = []
    for i in dict_minus:
        if i in roman:
            list_b.append(dict_minus[i])

    return sum(list_a) - sum(list_b)
