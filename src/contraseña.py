def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isupper() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    return True