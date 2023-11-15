from isMutantFunction import isMutant

def isValidString(cadena):
    caracteresPermitidos = ('A', 'T', 'C', 'G')
    if len(cadena) != 6: return False
    validString = True
    for char in cadena:
        if caracteresPermitidos.count(char) < 1:
            validString = False
    return validString

def ejecutarEjemplo():
    dnaMutante = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    dnaHumano = ["ATGCGA","CAGTGC","TTCTGT","AGGATG","CGCCTA","TCAATG"]
    dnaInvalido = ["ATGCGa","CAGTGC","TTCTGT","AGGATG","CGCCTA","TCAATG"]
    ejemploMutant = isMutant(dnaMutante)
    ejemploHuman = isMutant(dnaHumano)
    print('El ADN de ejemplo mutante es:\n')
    mostrarMatriz(dnaMutante)
    print(f'\nLa función arroja: {ejemploMutant}')
    print('\nPor lo tanto:')
    mostrarResultado(ejemploMutant)
    print('\n-----------------------------')
    print('El ADN de ejemplo humano es:\n')
    mostrarMatriz(dnaHumano)
    print(f'\nLa función arroja: {ejemploHuman}')
    print('\nPor lo tanto:')
    mostrarResultado(ejemploHuman)
    print('\n-----------------------------')
    print('El ADN de ejemplo inválido es:\n')
    mostrarMatriz(dnaInvalido)
    print('\nLa función arroja:')
    print(isMutant(dnaInvalido))

def ingresarADN():
    dna = []
    print('Bien! Vamos a ingresar el ADN.\nRecordá que debe ser de longitud 6 y sólo caracteres permitidos (A, C, G, T)\n')
    for i in range(6):
        firstLoop = True
        validString = False
        while firstLoop or not validString:
            firstLoop = False
            cadena = input(f'Ingresá la cadena {i+1}.\n')
            validString = isValidString(cadena)
            if not validString: print('\nCometiste un error de tipeo')
        dna.append(cadena)
    print('\nPerfecto! El ADN ingresado es')
    mostrarMatriz(dna)
    dnaUsuario = isMutant(dna)
    print('\nLa funcion arroja:')
    print(dnaUsuario)
    print('Por lo tanto:')
    mostrarResultado(dnaUsuario)

def mostrarMatriz(lista):
    for string in lista:
        for char in string:
            print(char, end=' ')
        print()

def mostrarResultado(result):
    if result:
        print('--- ES MUTANTE ---')
    else:
        print('--- ES HUMANO ---')