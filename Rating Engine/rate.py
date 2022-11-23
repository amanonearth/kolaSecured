



def rating(xss, sqli):
    lst = []
    if xss:
        lst.append(1)
    else:
        lst.append(0)

    if sqli:
        lst.append(1)
    else:
        lst.append(0)

    val = sum(lst) / len(lst)
    if val == 0.25:
        wrating = 4
    elif val == 0.50:
        wrating = 3
    elif val == 0.75:
        wrating = 2
    elif val == 1.0:
        wrating = 1
    return wrating