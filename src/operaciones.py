def factorial(n):
    if not isinstance(n, int) or n < 0:  # Valida que sea entero positivo
        raise ValueError("El factorial solo está definido para enteros no negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)