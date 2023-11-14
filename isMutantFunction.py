def isMutant(inputDna):
    dna = inputDna
    encontrados = 0

    def isValidDna():
        caracteresPermitidos = ('A', 'T', 'C', 'G')
        if len(dna) != 6: return False
        for i in range(6):
            if len(dna[i]) != 6: return False
            validString = True
            for j in range(6):
                for char in caracteresPermitidos:
                    if dna[i][j] == char:
                        validString = True
                        break
                    else:
                        validString = False
                if not validString: return False
        return validString

    def evaluarHorizontal():
        nonlocal encontrados
        for i in range(6):
            if encontrados > 1: break
            if dna[i][2] == dna[i][3]:
                if dna[i][4] == dna[i][3]:
                    if dna[i][5] == dna[i][4]: encontrados += 1
                    elif dna[i][1] == dna[i][2]: encontrados += 1
                elif dna[i][0] == dna[i][2]:
                    if dna[i][1] == dna[i][2]: encontrados += 1

    def evaluarVertical():
        nonlocal encontrados
        if encontrados > 1: return
        for i in range(6):
            if encontrados > 1: return
            if dna[2][i] == dna[3][i]:
                if dna[4][i] == dna[3][i]:
                    if dna[5][i] == dna[4][i]: encontrados += 1
                    elif dna[1][i] == dna[2][i]: encontrados += 1
                elif dna[0][i] == dna[2][i]:
                    if dna[1][i] == dna[2][i]: encontrados += 1

    def evaluarDiagonalNegativa():
        nonlocal encontrados
        if encontrados > 1: return
        for i in range(3):
            if encontrados > 1: return
            for j in range(3):
                if encontrados > 1: return
                if dna[i][j] == dna[i+1][j+1]:
                    if dna[i+1][j+1] == dna[i+2][j+2]:
                        if dna[i+2][j+2] == dna[i+3][j+3]:
                            encontrados += 1

    def evaluarDiagonalPositiva():
        nonlocal encontrados
        if encontrados > 1: return
        for i in range(3, 6):
            if encontrados > 1: return
            for j in range(3):
                if encontrados > 1: return
                if dna[i][j] == dna[i-1][j+1]:
                    if dna[i-1][j+1] == dna[i-2][j+2]:
                        if dna[i-2][j+2] == dna[i-3][j+3]:
                            encontrados += 1

    if isValidDna():
        evaluarHorizontal()
        evaluarVertical()
        evaluarDiagonalNegativa()
        evaluarDiagonalPositiva()
        return encontrados > 1
    else:
        print('El ADN ingresado no es válido. Recordá que tienen que ser 6 cadenas de 6 caracteres permitidos (A, T, C, G)')
        return None