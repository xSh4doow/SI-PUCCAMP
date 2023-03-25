# Criação da Fase 1 do Projeto Integrador (para análise de Requisitos)- 11/03/2023
import time


# Criando um novo objeto 'Ar' - Capacidade de Cadastrar vários 'Ares'
class Ar:
    # Inicializando cada instância do Objeto Ar
    def __init__(self, mp10, mp25, o3, co, no2, so2):
        # Criando as Variáveis/Características desse Ar
        self.mp10 = mp10
        self.mp25 = mp25
        self.o3 = o3
        self.co = co
        self.no2 = no2
        self.so2 = so2

    def mostrar(self):
        print(f'''
----------------------------
MP10: {self.mp10}
MP2.5: {self.mp25}
03 - Ozônio: {self.o3}
CO - Monóxido de Carbono: {self.co}
NO2 - Dióxido de Nitrogênio: {self.no2}
SO2 - Dióxido de Enxofre: {self.so2}
----------------------------
        '''.format())


# Gerar a média dos parâmetros, independente de seus tamanhos
def gerar_media(l1, l2, l3, l4, l5, l6):
    # Atribuição de variáveis
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    mp10, mp25, o3, co, no2, so2 = 0, 0, 0, 0, 0, 0

    # Cálculo das médias
    while a != len(l1):
        mp10 = int(l1[a]) + mp10
        a += 1

    while b != len(l2):
        mp25 = int(l2[b]) + mp25
        b += 1

    while c != len(l3):
        o3 = int(l3[c]) + o3
        c += 1

    while d != len(l4):
        co = int(l4[d]) + co
        d += 1

    while e != len(l5):
        no2 = int(l5[e]) + no2
        e += 1

    while f != len(l6):
        so2 = int(l6[f]) + so2
        f += 1

    mp10 = mp10 / len(l1)
    mp25 = mp25 / len(l2)
    o3 = o3 / len(l3)
    co = co / len(l4)
    no2 = no2 / len(l5)
    so2 = so2 / len(l6)

    # Retornar como uma Tupla os valores
    return mp10, mp25, o3, co, no2, so2


# Classificar o Ar
def classificadora(objeto):
    # Pegando as informações do Ar
    media = gerar_media(objeto.mp10, objeto.mp25, objeto.o3, objeto.co, objeto.no2, objeto.so2)
    mp10 = media[0]
    mp25 = media[1]
    o3 = media[2]
    co = media[3]
    no2 = media[4]
    so2 = media[5]

    # Criando uma variável auxiliar
    n = 0

    # Classificando
    if (0 <= mp10 <= 50) and (0 <= mp25 <= 25) and (0 <= o3 <= 100) and (0 <= co <= 9) and (0 <= no2 <= 200) and (0 <= so2 <= 20):
        n = 1
    if (50 < mp10 <= 100) or (25 < mp25 <= 50) or (100 < o3 <= 130) or (9 < co <= 11) or (200 < no2 <= 240) or (20 < so2 <= 40):
        n = 2
    if (100 < mp10 <= 150) or (50 < mp25 <= 75) or (130 < o3 <= 160) or (11 < co <= 13) or (240 < no2 <= 320) or (40 < so2 <= 365):
        n = 3
    if (150 < mp10 <= 250) or (75 < mp25 <= 125) or (160 < o3 <= 200) or (13 < co <= 15) or (320 < no2 <= 1130) or (365 < so2 <= 800):
        n = 4
    if (mp10 > 250) or (mp25 > 125) or (o3 > 200) or (co > 15) or (no2 > 1130) or (so2 > 800):
        n = 5
    if mp10 < 0 or mp25 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
        n = 0
        print('INSIRA SOMENTE VALORES INTEIROS POSITIVOS')

    # Retornando Informações ao Usuário
    if n == 1:
        print(f'''
------------------------------------------
SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
------------------------------------------
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}
------------------------------------------
Nessas condições, seu ar é Bom!
Nenhum efeito ruim é causado!
------------------------------------------''')
    elif n == 2:
        print(f'''
------------------------------------------
SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
------------------------------------------
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}
------------------------------------------
Nessas condições, seu ar é Moderado!
------------------------------------------
Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como:
- Tosse Seca
- Cansaço
A população, em geral, não é afetada!
-----------------------------------------''')
    elif n == 3:
        print(f'''
------------------------------------------
SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
------------------------------------------
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}
------------------------------------------
Nessas condições, seu ar é Ruim!
------------------------------------------
Toda a população pode apresentar sintomas como:
- Tosse Seca
- Cansaço
- Ardor nos Olhos, Nariz e Garganta
Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas mais sérios na saúde!
-----------------------------------------''')
    elif n == 4:
        print(f'''
------------------------------------------
SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
------------------------------------------
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}
------------------------------------------
Nessas condições, seu ar é Muito Ruim!
------------------------------------------
Toda a população pode apresentar agravamento dos sintomas como:
- Tosse Seca
- Cansaço
- Ardor nos Olhos, Nariz e Garganta
- Falta de ar
- Respiração Ofegante
Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas ainda mais sérios à saúde!
-----------------------------------------''')
    elif n == 5:
        print(f'''
------------------------------------------
SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
------------------------------------------
MP10: {mp10}
MP2.5: {mp25}
O3: {o3}
CO: {co}
NO2: {no2}
SO2: {so2}
------------------------------------------
Nessas condições, seu ar é Péssimo!
------------------------------------------
Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares.
Aumento da morte prematura em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)
-----------------------------------------''')


# Função pra deixar o código mais bonitinho
def continuar():
    time.sleep(1.5)
    while True:
        print('Deseja continuar navegando nos projetos?')
        resp = input('Sim ou Não?\n')
        if resp.lower() == 'sim':
            print('Ok, redirecionando para o menu principal!')
            time.sleep(1.5)
            break
        elif resp.lower() == 'nao':
            print('Tudo bem, obrigado por usar meu sistema!')
            time.sleep(1)
            quit()
        else:
            print('Resposta Inválida, Tente Novamente!')


# Inicialização do Sistema
def main():
    # Print da Introdução
    print(f'''
------------------------------------------
Seja bem-vindo ao SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
Por favor, insira corretamente os valores:
    ''')

    # Coleta de Dados
    mp10 = list(input('MP10: ').split(','))
    mp25 = list(input('MP2.5: ').split(','))
    o3 = list(input('03 - Ozônio: ').split(','))
    co = list(input('CO - Monóxido de Carbono: ').split(','))
    no2 = list(input('NO2 - Dióxido de Nitrogênio: ').split(','))
    so2 = list(input('SO2 - Dióxido de Enxofre: ').split(','))

    # Inialização de um Objeto Ar e atribuição das características
    a1 = Ar(mp10, mp25, o3, co, no2, so2)

    # Cálculo e Classificação - cálculo já incorporado na função classificadora
    classificadora(a1)

    # Retorno ou Saída
    continuar()


# Play
if __name__ == '__main__':
    main()
