def increment_string(string):
    s = ""
    num = ""

    for i in range(len(string)):
        if string[i].isdigit():
            s = string[:i]
            num = string[i:]
            break
    print(num)

    if not num:
        s = string
        num = '1'
    

    else: num = '0' * (len(num) - len(str(int(num)+1))) +str(int(num) + 1)
    
    return s+num

string = "foobar099"
print(increment_string(string))