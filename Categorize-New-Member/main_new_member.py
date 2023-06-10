def open_or_senior(data):
    a = map(function, data)
    print(a)
    return a


def function(n):
    if n[0] >= 55 and n[1] > 7:
        return "Senior"
    else:
        return "Open"
