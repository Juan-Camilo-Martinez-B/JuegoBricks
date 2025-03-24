def es_palindromo(texto):
    texto_limpio = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto_limpio == texto_limpio[::-1]