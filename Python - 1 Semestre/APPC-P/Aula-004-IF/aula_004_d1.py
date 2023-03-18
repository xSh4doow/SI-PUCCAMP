# Ano Bissexto
def bissexto():
    while True:
        try:
            ano = int(input('INSIRA O ANO QUE DESEJA VERIFICAR: '))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            if ((ano % 4) == 0) and ((ano % 100) != 0):
                print(f'O ANO {ano} É UM ANO BISSEXTO!')
                break
            else:
                print(f'O ANO {ano} NÃO É UM ANO BISSEXTO!')
                break


# Verificar Ano
def verify_ano():
    while True:
        try:
            dia = int(input('DIGITE O DIA: '))
            mes = int(input('DIGITE O MÊS: '))
            ano = int(input('DIGITE O ANO: '))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            if dia <= 0:
                print('DIA INVÁLIDO, NÃO EXISTE DIA 0')
            elif dia > 31:
                print('DIA INVÁLIDO, NÃO EXISTE MAIOR QUE 31')
            elif dia > 28 and mes == 2 and ((ano % 4) != 0):
                print('DIA INVÁLIDO, NESSE ANO NÃO HÁ DIA 29 DE FEVEREIRO')
            elif dia > 29 and mes == 2 and ((ano % 4) == 0):
                print('DIA INVÁLIDO, NÃO EXISTE DIA MAIOR QUE 29 DE FEVEREIRO')
            elif (mes in [4, 6, 9, 11]) and dia > 30:
                print('DIA INVÁLIDO, NESSE MÊS NÃO TEM DIA 31')
            elif mes == 0 or mes >= 13:
                print('NÃO EXISTE MÊS 0 OU MAIOR QUE 12')
            elif ano == 0:
                print('NÃO EXISTE ANO 0')
            else:
                print('A DATA INSERIDA É VÁLIDA E...')
                if ((ano % 4) == 0) and ((ano % 100) != 0):
                    print('O ANO INSERIDO É UM ANO BISSEXTO!')
                    break
                else:
                    print('O ANO INSERIDO NÃO É UM ANO BISSEXTO!')
                    break


# Menuzinho
def menu():
    while True:
        print('''
---------------------------------
DESAFIO I - ESTRUTURAS DE DECISÃO
---------------------------------
1. Exercício 13
2. Exercício 14
3. Sair
---------------------------------''')
        try:
            opt = int(input('SELECIONE SUA OPÇÃO:\n'))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            if opt == 1:
                bissexto()
                break
            elif opt == 2:
                verify_ano()
                break
            else:
                quit()


if __name__ == '__main__':
    menu()