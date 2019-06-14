'''
    KC_EJ05
    Crear un programa que solicite el año y mes de nacimineto de dos personas y muestre el resultado de compararlas.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_valor(msg, moy):
    pedido = None
    tupla_mes = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                 "Noviembre", "Diciembre")

    while pedido is None:
        if moy == 'M':
            pedido = input(msg).capitalize()

            if pedido not in tupla_mes:
                pedido = None

        elif moy == 'Y':
            pedido = valida_year(input(msg))

        if pedido is None:
            print("\n\tEntrada no válida.\n")

    return pedido


# Función que se encarga de validar que el valor que le llega es numérico entero, o devolverá 'None'
def valida_year(str_year):
    try:
        year_valido = int(str_year)

        if year_valido < 0:
            year_valido = None
    except:
        year_valido = None

    return year_valido


# Ejecución del código principal
if __name__ == "__main__":
    month_years = []

    for n in range(0, 2):
        par = []
        par.append(pide_valor("Introduce un mes de nacimiento: ", 'M'))
        par.append(pide_valor("Introduce un año de nacimiento: ", 'Y'))
        month_years.append(par)

    print(month_years)
    if month_years[0] == month_years[1]:
        print(True)
    else:
        print(False)