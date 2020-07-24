def create_phone_number(n):
    m = "".join(map(str, n))
    return "({}) {}-{}".format(m[:3], m[3:6], m[6:])