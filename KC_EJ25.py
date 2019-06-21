'''
    KC_EJ25
    Crear un programa que contenga un número aleatorio del 1 al 100 (sin mostrarlo) y permitir que el usuario intente adivinarlo.
    El usuario sólo tendrá 10 oportunidodes, en cada oportunidad fallida se le dará una pista para que sepa si debe intentarlo con un número mayor o menor.
'''
    

import random


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tNúmero no válido. Pon un valor numérico entero entre 0 y 100.\n")

    return numero_pedido


# Función que se encarga de validor que el valor que le llega es numérico entre 0 y 100, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = int(str_numero)

        if numero_valido < 0 or numero_valido > 100:
            numero_valido = None
    except:
        numero_valido = None

    return numero_valido


# Ejecución del código principal
if __name__ == "__main__":

    secreto = random.randint(0, 100)
    
    print("Tienes 10 oportunidades para adivinar mi número secreto.")
    
    for n in range(0, 10):
        numero = pide_numero("\n{}ª Oportunidad. Intenta adivinar: ".format(n + 1))
        
        if numero == secreto:
            pref = "Muy bien. "
            
            if n < 3:
                pref = "¡¡ IMPRESIONANTE !!  "
                
            print("\n\t\t{}Era el {}. Lo has adivinado a la {}ª.".format(pref, secreto, n + 1))
            
            break
        elif n == 9:
            print("\n\tLo siento. No has sido capaz de adivinar mi número. Era el {}.".format(secreto))
        else:
            mom = ""
            s1 = "n"
            s2 = "es"
            
            if numero < secreto:
                mom = "mayor"
            else:
                mom = "menor"
            
            if n == 3:
                s1, s2 = "", ""
                
            print("\nVa a ser que no.\nInténtalo de nuevo con una cifra {} (te queda{} {} oportunidad{}).".format(mom, s1, 9 - n, s2))
