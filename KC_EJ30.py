'''
    KC_EJ30
    Crear un programa que simule una máquina expendedora de refrescos con las siguientes características:
        · Las bebidas disponibles son: Fanta, Pepsi, 7Up.
        · Todas las bebidas tienen un costo de 1€.
        · La máuina recibe monedas de 10, 20, 50 céntimos y de 1 y 2 €.
    El programa deberá permitir que el usuario seleccione una bebida e ingrese una a una las monedas.
    El programa deberá detenerse cuando el importe del refresco haya sido completado y, de ser necesario, determinar el sobrante y las monedas a devolver.
'''


_EUROS = (2, 1, 0.5, 0.2, 0.1)
_MONEDAS = (2, 1, 50, 20, 10)
_REFRESCOS = {"fanta": 1, "pepsi": 2, "7up": 3}
_PRECIO = 1
vueltas = {"2": 0, "1": 0, "0.5": 0, "0.2": 0, "0.1": 0}

    
# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_refresco(msg):
    refresco_pedido = None
    marca = None

    while refresco_pedido is None:
        refresco_pedido = valida_refresco(input(msg))

        if refresco_pedido is None:
            print("\n\tRefresco no disponible. Elige una de las 3 opciones.\n")

    for k, v in _REFRESCOS.items():
        if v == refresco_pedido:
            marca = k       

    return refresco_pedido, marca


# Función que se encarga de validar que el valor que le llega es numérico entre 1 y 3, o una clave del diccionario de refrescos, o devolverá 'None'
def valida_refresco(str_refresco):
    refresco_valido = None
    
    if str_refresco.isdigit():
        try:
            refresco_valido = int(str_refresco)

            if refresco_valido < 1 or refresco_valido > 3:
                refresco_valido = None
        except:
            refresco_valido = None
    else:
        for k, v in _REFRESCOS.items():
            if k == str_refresco.lower():
                refresco_valido = v            

    return refresco_valido

    
# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_moneda(msg):
    moneda_pedida = None

    while moneda_pedida is None:
        moneda_pedida = valida_moneda(input(msg))

        if moneda_pedida is None:
            print("\n\tMoneda no admitida.\n")

    return moneda_pedida


# Función que se encarga de validar que el valor que le llega es numérico y está en la lista de monedas, o devolverá 'None'
def valida_moneda(str_moneda):
    try:
        moneda_valida = int(str_moneda)

        if moneda_valida not in _MONEDAS:
            moneda_valida = None
        elif moneda_valida > 2:
            moneda_valida = moneda_valida / 100
        
    except:
        moneda_valida = None

    return moneda_valida


# Función para recopilar el pago en monedas
def pagar():
    pagado = False
    suma = 0
    
    while not pagado:
        moneda = pide_moneda("\nIntroduce una moneda: ")
        suma += moneda
        
        if suma >= _PRECIO:
            pagado = True
            
    return suma


# Función para calcular el sobrante
def devolucion(suma):
    resto = (suma - _PRECIO)
    
    while resto != 0:
        for ficha in _EUROS:
            cociente = resto // ficha
            resto = round(resto % ficha, 2)
        
            vueltas[str(ficha)] += cociente 
        
            if resto == 0:                    
                break

# Ejecución del código principal
if __name__ == "__main__":

    print("Esta máquina expendedora de refrescos tiene las siguientes opciones:\n")
    print("\t· 1  -->  Fanta  ...  1€\n\t· 2  -->  Pepsi  ...  1€\n\t· 3  -->  7Up    ...  1€")
    refresco, marca = pide_refresco("\nIntroduce la opción o la marca del refresco que deseas: ")
    print("\nSólo se admiten monedas de:")
    print("\t· 10 céntimos (introducir 10)\n\t· 20 céntimos (introducir 20)\n\t· 50 céntimos (introducir 50)\n\t· 1 € (introducir 1)\n\t· 2 € (introducir 2)")

    suma = pagar()
    
    print("\n\t¡¡ Aquí tiene su lata de {} !!".format(marca.capitalize()))
    
    if suma > _PRECIO:
        devolucion(suma)
        
        print("\n\tY ahora le devuelvo:")
        for key in vueltas.keys():
            if vueltas[key] != 0:
                if key == "1":
                    tipo = "euro"
                    mon = int(key)
                else:
                    tipo = "centimos"
                    mon = int(float(key) * 100)
                    
                if vueltas[key] > 1:
                    sufijo = "s"
                else:
                    sufijo = ""
                    
                print("\t\t{} moneda{} de {} {}".format(int(vueltas[key]), sufijo, int(mon), tipo))
    
    print("\n\t¡ Gracias por su compra !\n\t¡ Que tenga un buen día !")

    