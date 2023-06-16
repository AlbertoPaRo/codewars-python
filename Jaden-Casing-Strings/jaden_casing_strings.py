def to_jaden_case(string):
    a = ""
    unir = ""
    for i in string.split():
        a = i.capitalize()
        unir = unir + " " + a
    return (unir.strip())
