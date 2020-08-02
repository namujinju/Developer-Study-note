def calc(my, *arg):
    print(arg[0][0][0])
    if arg[0][0][0] == "times":
        return my * arg[0][0][1]
    elif arg[0][0][0] == "plus":
        return my + arg[0][0][1]
    elif arg[0][0][0] == "minus":
        return my - arg[0][0][1]
    else:
        return my // arg[0][0][1]


def zero(*arg):
    my = 0

    if arg == ():
        return my
    else:
        return calc(my, arg)


def one(*arg):
    my = 1
    if arg == ():
        return my
    else:
        return calc(my, arg)


def two(*arg):
    my = 2
    if arg == ():
        return my
    else:
        return calc(my, arg)


def three(*arg):
    my = 3
    if arg == ():
        return my
    else:
        return calc(my, arg)


def four(*arg):
    my = 4
    if arg == ():
        return my
    else:
        return calc(my, arg)


def five(*arg):
    my = 5
    if arg == ():
        return my
    else:
        return calc(my, arg)


def six(*arg):
    my = 6
    if arg == ():
        return my
    else:
        return calc(my, arg)


def seven(*arg):
    my = 7
    if arg == ():
        return my
    else:
        return calc(my, arg)


def eight(*arg):
    my = 8
    if arg == ():
        return my
    else:
        return calc(my, arg)


def nine(*arg):
    my = 9
    if arg == ():
        return my
    else:
        return calc(my, arg)


def plus(num):
    return ("plus", num)


def minus(num):
    return ("minus", num)


def times(num):
    return ("times", num)


def divided_by(num):
    return ("divided_by", num)


print(seven(times(five())))
