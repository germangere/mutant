from menuFunctions import ejecutarEjemplo, ingresarADN

print('\nHola! Bienvenido al detector de mutantes')

def menu():
    print('Cómo deseas proceder?\n')
    print('1 - Ejecutar ADN de ejemplo')
    print('2 - Ingresar ADN')
    print('0 - Hoy no quiero juzgar a nadie\n')
    opcion = input()
    print('\n')
    match opcion:
        case '1':
            ejecutarEjemplo()
            print('\nQué te pareció el ejemplo?')
            print('Probás un ADN propio? \n')
            menu()
        case '2':
            ingresarADN()
            print('\nSeguimos?')
            menu()
        case '0':
            print('Ya vendrás con más maldad, saludos!')
        case _:
            print('Esa no es una opción válida. Probá de nuevo')
            menu()

menu()