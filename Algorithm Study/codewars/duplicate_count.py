def duplicate_count(s):
    s = s.lower()
    for i in list(set(s)):
        s = s.replace(i, "", 1)
    return len(set(s))

print(duplicate_count("aaAAA123"))