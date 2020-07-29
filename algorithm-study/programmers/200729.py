def solution(phone_book):
    n = len(phone_book)
    for i in range(n-1):
        for j in range(i+1, n):
            if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
                return False
    return True


# phone_book = ["123", "456", "789", "157", "486", "745"]
phone_book = ["12", "123", "1235", "567", "88"]

print(solution(phone_book))
