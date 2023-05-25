# Inicio do Código
from fase1_dataset import dataset, habilidades
from time import sleep


def maquina_de_escrever(texto, delay=0.3):
    for char in texto:
        print(char, end='', flush=True)
        sleep(delay)
    print()


# Sistema de Escolha de Carreira
for i in dataset:
    p = i.get('PROFISSÃO')
    h = i.get('HABILIDADES')


# Demonstrar as Habilidades
def mostrar_habilidades():
    for habilidade in habilidades:
        print(habilidade)


def calcular_prob(habs):
    pass


if __name__ == '__main__':
    print('Bem vindo ao Sistema de Profissão')
    print('De acordo com as categorias abaixo, com quais você mais se conecta?')
    mostrar_habilidades()
    selecoes = input('digite as que voce interessa - separe com ,\n').split(',')
    print(selecoes)
