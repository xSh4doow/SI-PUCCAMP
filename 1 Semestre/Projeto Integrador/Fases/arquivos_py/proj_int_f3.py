# Criação da Fase 1 do Projeto Integrador- 09/04/2023
import time
import sql_funcs


def classificadora(ar):
    # Pegando as informações do Ar
    media = sql_funcs.get_valores(ar)
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


def continuar():
    time.sleep(1.5)
    while True:
        print('Deseja continuar no sistema?')
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


def criar_ar():
    print('''
------------------------------------------''')
    nome = input('Insira o nome desejado para o Ar: ')
    resp = sql_funcs.criar_conta(nome)
    print(resp)


def goto_mp():
    ares = sql_funcs.usuarios('ares','')
    print(ares)
    ar = input('Qual dos Ares, mostrados acima, deseja entrar: ')
    if ar not in ares:
        print('Esse ar não existe, para criá-lo, volte para o menu!')
    else:
        login = sql_funcs.login(ar)
        print(login)
        menu_principal(ar)


def menu_iniciar():
    while True:
        print(f'''
------------------------------------------
Seja bem-vindo ao SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
MENU INICIAL:
1. ENTRAR
2. CRIAR AR
3. SAIR
------------------------------------------
        ''')
        opt = int(input('Digite a opção desejada: '))
        if opt == 1:
            goto_mp()
        elif opt == 2:
            criar_ar()
            continuar()
        elif opt == 3:
            break


def inserir_amostras(nome_ar):
    print('''
-----------------------------------------
INSERÇÃO DE AMOSTRA
-----------------------------------------
DIGITE EM SEQUÊNCIA OS VALORES:
 - NOME AMOSTRA:
 - MP10:
 - MP2.5:
 - O3:
 - CO:
 - NO2:
 - SO2:
-----------------------------------------
''')
    try:
        _nome = input('NOME: ')
        _mp10 = int(input('MP10: '))
        _mp25 = int(input('MP2.5: '))
        _o3 = int(input('O3: '))
        _co = int(input('CO: '))
        _no2 = int(input('NO2: '))
        _so2 = int(input('SO2: '))
    except ValueError:
        return 'INSIRA SOMENTE VALORES CORRETOS'
    else:
        if _mp10 < 0 or _mp25 < 0 or _o3 < 0 or _co < 0 or _no2 < 0 or _so2 < 0:
            return 'INSIRA SOMENTE VALORES POSITIVOS'
        else:
            resp = sql_funcs.inserir(nome_ar, _nome, _mp10, _mp25, _o3, _co, _no2, _so2)
            return resp


def alterar_amostras(nome_ar):
    amostras = sql_funcs.usuarios('amostras', nome_ar)
    print(amostras)
    amostra = input('Qual amostra, mostradas acima, deseja alterar: ')
    if amostra not in amostras:
        return 'Essa amostra não existe.'
    else:
        atual = sql_funcs.get_amostras(nome_ar, amostra)
        print(f'''
-----------------------------------------
ALTERAÇÃO DE AMOSTRA
-----------------------------------------
VALORES ATUAIS:
 - NOME AMOSTRA: {atual.get('amostra_name')}
 - MP10: {atual.get('mp10')}
 - MP2.5: {atual.get('mp25')}
 - O3: {atual.get('o3')}
 - CO: {atual.get('co')}
 - NO2: {atual.get('no2')}
 - SO2: {atual.get('so2')}
-----------------------------------------
    ''')
        print('Digite abaixo os valores para a mudança, caso deseja manter o mesmo, favor reescrever-lo!')
        try:
            _mp10 = int(input('MP10: '))
            _mp25 = int(input('MP2.5: '))
            _o3 = int(input('O3: '))
            _co = int(input('CO: '))
            _no2 = int(input('NO2: '))
            _so2 = int(input('SO2: '))
        except ValueError:
            return 'INSIRA SOMENTE VALORES CORRETOS'
        else:
            if _mp10 < 0 or _mp25 < 0 or _o3 < 0 or _co < 0 or _no2 < 0 or _so2 < 0:
                return 'INSIRA SOMENTE VALORES POSITIVOS'
            else:
                resp = sql_funcs.alterar(atual.get('amostra_name'),_mp10, _mp25, _o3, _co, _no2, _so2)
                return resp


def excluir_amostras(nome_ar):
    amostras = sql_funcs.usuarios('amostras', nome_ar)
    print(amostras)
    amostra = input('Qual amostra, mostradas acima, deseja excluir: ')
    if amostra not in amostras:
        return 'Essa amostra não existe.'
    else:
        resp = sql_funcs.deletar(amostra)
        return resp


def menu_principal(nome_ar):
    while True:
        print(f'''
------------------------------------------
Seja bem-vindo ao SCQA - Sistema de Controle de Qualidade do Ar
------------------------------------------
MENU PRINCIPAL:
1. INSERIR AMOSTRAS
2. ALTERAR AMOSTRAS
3. EXCLUIR AMOSTRAS
4. CLASSIFICAR AMOSTRAS
5. SAIR
------------------------------------------
            ''')
        opt = int(input('Digite a opção desejada: '))
        if opt == 1:
            print(inserir_amostras(nome_ar))
            continuar()
        elif opt == 2:
            print(alterar_amostras(nome_ar))
            continuar()
        elif opt == 3:
            print(excluir_amostras(nome_ar))
            continuar()
        elif opt == 4:
            classificadora(nome_ar)
        elif opt == 5:
            break


if __name__ == '__main__':
    menu_iniciar()
