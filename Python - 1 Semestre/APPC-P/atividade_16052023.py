import time


def maquina_de_escrever(texto, delay=0.3):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def listar():
    _input = input('Digite sua lista, separada por vírgula!\n').split(',')
    _lista = [int(x) for x in _input]
    return _lista


def inverter_vetor(vetor):
    return vetor[::-1]


def ordenar(lista, modo):
    n = len(lista)

    if modo == 'Crescente':
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista
    elif modo == 'Decrescente':
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista


if __name__ == '__main__':
    intro = f"Olá, {input('Olá, qual o seu nome? ').title()}! Bem vindo(a) ao programa de VETORES! Por favor, siga as instruções abaixo!"
    maquina_de_escrever(intro)

    vetor = listar()

    print(f'''
------------------------------------------
LISTA: {vetor}
------------------------------------------
LISTA INVERTIDA: {inverter_vetor(vetor)}
------------------------------------------
LISTA ORDENADA:
CRESCENTE: {ordenar(vetor, 'Crescente')}
DECRESCENTE: {ordenar(vetor, 'Decrescente')}
------------------------------------------
    ''')
