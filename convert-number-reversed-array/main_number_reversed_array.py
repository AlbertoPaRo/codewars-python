def digitize(n):
    str_value = ""
    valor = []
    num_str = list(str(n))
    num_str.reverse()
    for i in num_str:
        valor.append(int(i))
    return valor
