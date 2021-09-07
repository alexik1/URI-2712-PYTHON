n = int(input())
while n:
    n -= 1
    placa = input().split('-')
    if (len(placa) == 2) and (len(placa[0]) == 3) and (len(placa[1]) == 4) and (placa[0] == placa[0].upper()) and (placa[0].isalpha()): #isalpha to check if 1st lenght of placas is letters only.
        try:
            check = int(placa[1])
            r = int(placa[1][3])
            if r > 8 or r == 0:
                print('SEXTA')
            elif r > 6:
                print('QUINTA')
            elif r > 4:
                print('QUARTA')
            elif r > 2:
                print('TERCA')
            else:
                print('SEGUNDA')
        except:
            print('FALHA')
    else:
        print('FALHA')
