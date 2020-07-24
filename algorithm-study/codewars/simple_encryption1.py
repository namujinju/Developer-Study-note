
def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    m = len(encrypted_text)

    for k in range(n):
        new_arr = []
        
        text_0 = [i for i in encrypted_text[:m//2]]
        text_1 = [i for i in encrypted_text[m//2:]]
        for i in range(m//2):
            new_arr.append(text_1.pop(0))
            new_arr.append(text_0.pop(0))
        new_arr += text_1
        encrypted_text = "".join(new_arr)
    return "".join(new_arr)

def encrypt(text, n):
    if n <= 0:
        return text

    for k in range(n):
        text = "".join([text[i] for i in range(len(text)) if i%2 == 1] + [text[i] for i in range(len(text)) if i%2 == 0])
    return text

text = "This is a test!"

encrypted_text = encrypt(text, 4)

print(encrypted_text)
print(decrypt(encrypted_text, 4))

a = [1,2]
print(a[3:2])

print()



