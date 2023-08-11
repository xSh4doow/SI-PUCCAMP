# Criação da Fase 2 do Projeto Integrador- 31/03/2023
import time
import sql_funcs


# Classificar o Ar
def classificadora():
    # Pegando as informações do Ar
    media = sql_funcs.get_valores('Campinas 2')
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
            print('Tudo bem, obrigado por usar nosso sistema!')
            time.sleep(1)
            quit()
        else:
            print('Resposta Inválida, Tente Novamente!')


# Inicialização do Sistema
def main():
    while True:
        # Print da Introdução
        print(f'''


------------------------------------------
Seja bem-vindo ao SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
''')

        # Cálculo e Classificação - cálculo já incorporado na função classificadora
        classificadora()

        # Retorno ou Saída
        continuar()


# Play
if __name__ == '__main__':
    main()
