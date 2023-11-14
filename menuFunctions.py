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
    print(f'El ADN de ejemplo mutante es {dnaMutante}')
    print(f'La función arroja: {isMutant(dnaMutante)}\n')
    print(f'El ADN de ejemplo humano es {dnaHumano}')
    print(f'La función arroja: {isMutant(dnaHumano)}\n')
    print(f'Un ADN de ejemplo inválido es {dnaInvalido}')
    print(f'La función arroja:')
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
    print(f'\nPerfecto! El ADN ingresado es {dna}\n')
    print(f'La funcion arroja: {isMutant(dna)}\n')

