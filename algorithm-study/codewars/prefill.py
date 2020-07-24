def prefill(n,v):
    try:
        list_v = []

        try:
            n = int(n)
        except Exception:
            pass

        for i in range(n):
            list_v.append(v)
        return list_v
    except  TypeError:
        print("{} is invalid".format(n))

print(prefill(prefill(0,0), 0))