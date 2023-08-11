# 1

def print_range():
    a = int(input('Qual será o primeiro número? '))
    b = int(input('Qual será o segundo número? '))
    for i in range(a, b):
        print(i)


def calc_med():
    n = input('Quais serão os números para fazer a mediana?\n').split(',')
    med = len(n) // 2
    print(n[med])


def calc_all():
    n = [eval(num) for num in input('Quais serão os números para a análise?\n').split(',')]
    med = len(n) // 2
    print(f'A médiana é: {n[med]}')
    print(f'O maior é: {max(n)}')
    print(f'O menor é: {min(n)}')


def fatorial():
    n = int(input('Qual o valor para calcular sua fatorial? '))
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    print(fat)


def tabuada():
    n = int(input('Qual o valor para calcular sua tabuada? '))
    for i in range(0, 11):
        print(f'{n}x{i} = {n * i}')


def bohrgogna():
    d = int(input('Qual dia do mês quer calcular a Temperatura? '))
    t = 0.011 * (d ** 3) - 0.3 * (d ** 2) + 0.004 * d
    print(f'A temperatura é: {t}°Celsius')


def adv_n():
    while True:
        import random
        nComp = random.randint(0, 100)

        print('''
SEJA BEM-VINDO AO JOGO:
ADIVINHE O NÚMERO!
    ''')
        nJ = -1
        tent = 0
        print(nComp)
        print('Se quiser jogar, digite um número, se quiser sair e iniciar uma nova, digite #.')
        while nJ != nComp:
            nJ = input()
            if nJ == '#':
                break
            else:
                nJ = int(nJ)
            tent += 1
            if nJ > nComp:
                print('Seu numero é MAIOR que o do computador')
            if nJ < nComp:
                print('Seu numero é MENOR que o do computador')
            if nJ == nComp:
                print(f'Parabéns, você ganhou em {tent} tentativas!')
        opt = input('Deseja jogar novamente? S/N: ')
        if opt in ['n', 'N']:
            print('Ok, até mais!')
            break
        elif opt in ['s', 'S']:
            print('Reinicializando o jogo!')
        else:
            print('Opção Inválida!')
            break


def div():
    a = int(input('Digite o primeiro número do intervalo: '))
    b = int(input('Digite o segundo número do intervalo: '))
    c = int(input('Digite o número para indicar a divisibilidade: '))
    resp = []
    for i in range(a, b + 1):
        if i % c == 0:
            resp.append(i)
    print(f'Os valores divisíveis por {c} são: {resp}.')


def lista():
    lista_times = ["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO",
                   "SANTOS", "FERROVIÁRIA", "JUVENTUS", "GOIÁS",
                   "ÍBIS", "SINOP"]
    ind = 0
    while ind != len(lista_times):
        print(f'{ind} - {lista_times[ind]}')
        ind += 1


def jokenpo():
    import random

    while True:

        p_user = 0
        p_comp = 0

        rounds = int(input('Quantas rodadas quer jogar? '))

        for i in range(0, rounds):
            print(f'''
    -------------------------------------
    Vamos jogar JOKENPO!
    -------------------------------------
    PLACAR: Você:{p_user}x{p_comp}
    -------------------------------------
    Digite Pedra, Papel ou Tesoura:    
        ''')
            computador = random.randint(1, 3)
            user = input().title()

            int_user = 0
            if user == 'Pedra':
                int_user = 1
            elif user == 'Papel':
                int_user = 2
            elif user == 'Tesoura':
                int_user = 3

            if int_user == computador:
                print('Vocês empataram')
            # pedraxpapel
            elif int_user == 1 and computador == 2:
                print('Você perdeu, a maquina fez 1 ponto')
                p_comp += 1
            # pedraxtesoura
            elif int_user == 1 and computador == 3:
                print('Você venceu, você fez 1 ponto')
                p_user += 1
            # papelxpedra
            elif int_user == 2 and computador == 1:
                print('Você venceu, você fez 1 ponto')
                p_user += 1
            # papelxtesoura
            elif int_user == 2 and computador == 3:
                print('Você perdeu, a maquina fez 1 ponto')
                p_comp += 1
            # tesouraxpedra
            elif int_user == 3 and computador == 1:
                print('Você perdeu, a maquina fez 1 ponto')
                p_comp += 1
            # tesouraxpapel
            elif int_user == 3 and computador == 2:
                print('Você venceu, você fez 1 ponto')
                p_user += 1

        if p_user < p_comp:
            print(f'O jogo terminou, a maquina venceu de: {p_comp} x {p_user}')
        elif p_comp < p_user:
            print(f'O jogo terminou, você venceu de: {p_user} x {p_comp}')
        elif p_comp == p_user:
            print(f'O jogo terminou, vocês empararam em: {p_user} x {p_comp}')

        opt = input('Deseja jogar novamente? S/N: ')
        if opt in ['n', 'N']:
            print('Ok, até mais!')
            break
        elif opt in ['s', 'S']:
            print('Reinicializando o jogo!')
        else:
            print('Opção Inválida!')
            break



jokenpo()
