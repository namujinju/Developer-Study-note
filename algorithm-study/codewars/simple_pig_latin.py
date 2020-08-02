def pig_it(text):
    arr = text.split(" ")

    return " ".join(map(shifting, arr))


def shifting(word):
    if word.isalpha():
        return word[1:] + word[0] + "ay"
    else:
        return word


text = "Hello world !"

print(pig_it(text))
