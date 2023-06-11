def is_square(n):
    raiz_cuadrada = 0
    if n >= 0:
        raiz_cuadrada = n ** 0.5
        if raiz_cuadrada.is_integer():
            return (True)
        else:
            return (False)
    else:
        return (False)
