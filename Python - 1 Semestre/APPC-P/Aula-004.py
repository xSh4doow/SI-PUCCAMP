# coding=utf-8
# Algoritmos - Aula 4
import datetime
import aula004ex7 as a47
import random


# Senha
def senha():
    s_senha = 10092004
    while True:
        try:
            u_input = int(input('Bem vindo ao Sistema! Por favor, insira sua senha para prosseguir:\n'))
        except ValueError:
            print('INSIRA SOMENTE NÚMEROS!')
        else:
            if u_input != s_senha:
                print('ACESSO NEGADO - TENTE NOVAMENTE')
            elif u_input == s_senha:
                print('ACESSO PERMITIDO')
                break


# Triângulos
def lados_tri():
    while True:
        try:
            lados = list(input('Insira os lados do triângulo: (separados por vírgulas)\n').split(','))
        except ValueError:
            print('Insira somente valores numéricos!')
        else:
            if lados[0] == lados[1] == lados[2]:
                print('Triângulo Equilátero')
                break
            elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
                print('Triângulo Isóceles')
                break
            else:
                print('Triângulo Escaleno')
                break


# Par ou Impar
def p_i():
    while True:
        try:
            numero = int(input('Insira o número que deseja saber se é par ou impar: \n'))
        except ValueError:
            print('SOMENTE NÚMEROS!')
        else:
            if numero % 2 == 0:
                print('Par')
                break
            else:
                print('Impar')
                break


# Divisivel
def div():
    while True:
        try:
            numero = list(input('Insira os números da divisão, separados por vírgula: \n').split(','))
        except ValueError:
            print('SOMENTE NÚMEROS!')
        else:
            if int(numero[0]) % int(numero[1]) == 0:
                print(f'O Número {numero[0]} É divisivel por {numero[1]}!')
                break
            else:
                print(f'O Número {numero[0]} NÃO é divisivel por {numero[1]}!')
                break


# Media
def irc():
    while True:
        try:
            pe1 = int(input('Insira o Peso da Prova 1: '))
            pr1 = int(input('Insira a Nota da Prova 1: '))
            pe2 = int(input('Insira o Peso da Prova 2: '))
            pr2 = int(input('Insira a Nota da Prova 2: '))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS!')
        else:
            media = ((pe1 * pr1) + (pe2 * pr2)) / (pe1 + pe2)
            print(f'''
--------------------------
BOLETIM IRC
--------------------------
PROVA 1 = {pe1 * pr1}
PROVA 2 = {pe2 * pr2}
--------------------------
MEDIA FINAL = {media}          
--------------------------            
''')
            if media < 5:
                print('REPROVADO')
                break
            elif media >= 9:
                print('PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR')
                break
            elif media >= 8:
                print('PARABÉNS O DESEMPENHO FOI MUITO BOM')
                break
            elif media >= 5:
                print('APROVADO')
                break


# Graus
def to_cel():
    while True:
        try:
            graus = float(input('Insira a temperatura a ser convertida: '))
            temp = input('Escolha de qual escala será convertida: fah(fahrenheit), kel(kelvin), rank(rankine) ou reau(reaumur)\n')
        except ValueError:
            print('INSIRA CORRETAMENTE OS VALORES!')
        else:
            if temp == 'rank':
                celsius = (graus - 491.67) / (9 / 5)
                print(graus, " Rankine equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'kel':
                celsius = graus - 273.15
                print(graus, "K equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'fah':
                celsius = (graus - 32) / (9 / 5)
                print(graus, "ºF equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'reau':
                celsius = graus * (4 / 5)
                print(graus, "ºR equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            else:
                print('Escala Incorreta')


# IPTU
def iptu():
    while True:
        try:
            ano_imovel = int(input('''
-----------------------------
PREFEITURA DE RAPIDÓPOLIS
-----------------------------
SISTEMA DE DESCONTO IPTU
-----------------------------
POR FAVOR, INSIRA O ANO DA CONSTRUÇÃO DO IMÓVEL:\n'''))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            ano_atual = int(datetime.date.today().strftime('%Y'))
            idade = ano_atual - ano_imovel
            pct = 0
            if idade < 5:
                pct = 0
            elif 5 <= idade < 20:
                pct = 15
            elif 20 <= idade < 40:
                pct = 25
            elif idade >= 40:
                pct = 30
            print(f'''
-----------------------------
PREFEITURA DE RAPIDÓPOLIS
-----------------------------
SISTEMA DE DESCONTO IPTU
-----------------------------
ANO ATUAL: {ano_atual}
ANO DE CONSTRUÇÃO DO IMÓVEL: {ano_imovel}
-----------------------------
O IMÓVEL TEM {idade} ANOS, PORTANTO RECEBE UM DESCONTO DE {pct}%
-----------------------------
            ''')
            break


# IMC
def imc():
    while True:
        print('BEM VINDO AO SISTEMA DE CÁLCULO DE IMC')
        try:
            peso = float(input('DIGITE AQUI O SEU PESO (ex 65):\n'))
            altura = float(input('DIGITE AQUI A SUA ALTURA (ex 1.70):\n'))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            c_imc = round((peso / (altura ** 2)), 2)
            classific = None
            if c_imc < 18.5:
                classific = 'Abaixo do Peso'
            elif 18.5 <= c_imc < 24.99:
                classific = 'Normal'
            elif 25 <= c_imc < 29.99:
                classific = 'Sobrepeso'
            elif c_imc >= 30:
                classific = 'Obesidade'
            print(f'SISTEMA DE CÁLCULO DE IMC\nSEU IMC É: {c_imc}\nSUA CLASSIFICAÇÃO É: {classific}')
            break


# Ordem Crescente
def ord_cresc():
    while True:
        try:
            numeros = list(input('QUAIS NÚMEROS VOCÊ DESEJA SABER SE ESTÁ EM ORDEM CRESCENTE? (SEPARADOS POR VÍRGULA)\n').split(', '))
            lista_numeros = []
            for i in numeros:
                lista_numeros.append(int(i))
        except ValueError:
            print('INSIRA SOMENTE VALORES NUMÉRICOS')
        else:
            ordem = lista_numeros.copy()
            ordem.sort(reverse=False)
            if lista_numeros == ordem:
                print('OS NÚMEROS ESTÃO EM ORDEM CRESCENTE', numeros, '=', ordem)
                break
            else:
                print('OS NÚMEROS NÃO ESTÃO EM ORDEM CRESCENTE', numeros, '!=', ordem)
                break


# Presença
def presenca():
    alunos = ['Heri Poter', 'Ermione Grenger', 'Roni Uislei', 'Voudemorti']
    q_a = random.randint(0, 3)
    while True:
        try:
            pr1 = float(input('Insira a Nota da Prova 1: '))
            pr2 = float(input('Insira a Nota da Prova 2: '))
            freq = float(input('Insira a Frequência do Aluno (sem %): '))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            ma = (pr1 + pr2) / 2
            status = None
            if freq <= 75:
                status = 'REPROVADO POR FALTA'
            else:
                if ma < 4:
                    status = 'REPROVADO POR NOTA'
                elif 4 <= ma < 6:
                    status = 'TERÁ DE PASSAR NO EXAME'
                elif 6 <= ma <= 10:
                    status = 'APROVADO'

            print(f'''
---------------------------------------
UNIVERSIDADE HOGWARTS DE RAPIDÓPOLIS         
---------------------------------------
ALUNO:{alunos[q_a]}
---------------------------------------
BOLETIM:
FREQUÊNCIA: {freq}%
NOTA PROVA DE FEITIÇOS: {pr1}
NOTA PROVA DE POÇÕES: {pr2}
MÉDIA FINAL: {ma}
---------------------------------------
RESULTADO: {status}
---------------------------------------
            ''')
            break


# Função F(x)
def funcx():
    while True:
        try:
            x = int(input('Insira o valor desejado de "X"\n'))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            try:
                y = (4 * (x ** 2) - (3 * x) + 9) / x
            except ZeroDivisionError:
                print('X não pode ser 0')
            else:
                print(f'NA EXPRESSÃO: y = (4 * (x ** 2) - (3 * x) + 9) / x, SE SUBSTITUIRMOS X POR {x}, Y = {y}!')
                break


# Menuzinho
def menu():
    while True:
        print('''
---------------------------------
CODIGOS - ESTRUTURAS DE DECISÃO - EXERCÍCIOS
---------------------------------
 1. Exercício 1 - Senha
 2. Exercício 2 - Triângulo
 3. Exercício 3 - Par ou Ímpar
 4. Exercício 4 - Divisível
 5. Exercício 5 - Instituto Rapodopolense de Computação
 6. Exercício 6 - Conversão para Celsius
 7. Exercício 7 - Para executar esse Exercício, o arquivo 'aula004ex7.py' deve estar no mesmo diretório
 8. Exercício 8 - IPTU
 9. Exercício 9 - IMC
10. Exercício 10 - Ordem Crescente
11. Exercício 11 - Presença em Hogwarts
12. Exercício 12 - Função F(x)
13. Sair
---------------------------------''')
        try:
            opt = int(input('SELECIONE SUA OPÇÃO:\n'))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            if opt == 1:
                senha()
                break
            elif opt == 2:
                lados_tri()
                break
            elif opt == 3:
                p_i()
                break
            elif opt == 4:
                div()
                break
            elif opt == 5:
                irc()
                break
            elif opt == 6:
                to_cel()
                break
            elif opt == 7:
                a47.main()
                break
            elif opt == 8:
                iptu()
                break
            elif opt == 9:
                imc()
                break
            elif opt == 10:
                ord_cresc()
                break
            elif opt == 11:
                presenca()
                break
            elif opt == 12:
                funcx()
                break
            else:
                quit()


if __name__ == '__main__':
    menu()
