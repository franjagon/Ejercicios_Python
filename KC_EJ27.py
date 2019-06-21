'''
    KC_EJ27
    Crear un programa que contenga una función es_palindromo(texto) y determine si dicho texto es un palíndromo.
'''

    
# Función que se encarga de solicitar el texto al usuario mientras no introduzca un valor válido
def pide_texto(msg):
    texto = None

    while texto is None:
        texto = input(msg)

        if len(texto) != 0 and len(texto) > 2:
            return texto
        else:
            texto = None
            print("\n\ttexto no válido.\n")


# Función que se encarga de montar una lista a partir de los caracteres de un texto. Elimina o sustituye todos los caracteres que no nos interesan.
def montarLista(texto):
    lista_texto = []

    texto = texto.lower().replace(" ", "").replace(".", "").replace(",", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "")\
                         .replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "")\
                         .replace("}", "").replace("<", "").replace(">", "").replace("+", "").replace("-", "").replace("*", "").replace("/", "")\
                         .replace("_", "").replace("\\", "").replace("@", "").replace("|", "").replace("#", "").replace("%", "").replace("$", "")\
                         .replace("€", "").replace("·", "").replace("&", "").replace("=", "").replace("'", "").replace("\"", "")\
                         .replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")\
                         .replace("ä", "a").replace("ë", "e").replace("ï", "i").replace("ö", "o").replace("ü", "u")\
                         .replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u")\
                         .replace("â", "a").replace("ê", "e").replace("î", "i").replace("ô", "o").replace("û", "u")
    
    for letra in texto:
            lista_texto.append(letra)

    return lista_texto

    
# Función que se encarga de analizar si el texto es un palíndromo
def es_palindromo(texto):
    sn = ""
    lista_texto = montarLista(texto)
    lista_reves = lista_texto[:]
    lista_reves.reverse()
    
    if lista_texto != lista_reves:
        sn = "no "
        
    return sn


# Ejecución del código principal
if __name__ == "__main__":

    texto = pide_texto("Introduce un texto y te diré si es o no un palíndromo: ")
    
    print("El texto: '{}' {}es un palíndromo".format(texto, es_palindromo(texto)))

