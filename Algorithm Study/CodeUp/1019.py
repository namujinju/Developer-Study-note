# a, b, c = input().split(".")
# print("{:04d}.".format(int(a)) + "{:02d}".format(int(b)) + ".{:02d}".format(int(c)))

a,b,c = input().split(".")
print("%04d" % int(a), end = ".")
print("%02d" % int(b), end = ".")
print("%02d" % int(c))