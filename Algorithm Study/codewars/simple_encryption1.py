from math import ceil
def decrypt(encrypted_text, n):
    [encrypted_text.pop() if i % 2 == 1 else encrypted_text.pop() for i in range(len(text))]

    pass


def encrypt(text, n):
    for k in range(n%4):
        text = "".join([text[i] for i in range(len(text)) if i%2 == 1] + [text[i] for i in range(len(text)) if i%2 == 0])
    return text

text = "This is a test!"

encrypted_text = encrypt(text, 1)
print(encrypted_text)



