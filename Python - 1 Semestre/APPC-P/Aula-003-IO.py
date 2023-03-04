# coding=utf-8
# Algoritmos aula 3

import time

def cal_sb():
    sh = float(input('Qual o Salário Hora do Funcionário?\n'))
    ht = int(input('Quantas Horas o Funcionário Trabalhou? (Horas completas)\n'))
    sb = sh * ht
    return str(sb)


def cal_dc():
    vp = float(input('Qual o valor do produto?\n'))
    pd = float(input('Qual o percentual de desconto? (sem a porcentagem - ex: 5 se 5%)\n'))
    d = vp * (pd / 100)
    return str(d)


def conv_DR():
    cot = float(input('Qual a cotação do dólar hoje? \n'))
    modo = int(input('1. Dolar pra Real ou 2. Real para Dolar?\n'))
    if modo == 1:
        valor = int(input('Qual o valor a ser convertido para Real?\n'))
        conv = valor * cot
    elif modo == 2:
        valor = int(input('Qual o valor a ser convertido para Dolar?\n'))
        conv = valor / cot
    return str(conv)

def tabajata():
    print('''
    ------------------------------
    TABAJATA LTDA.
    ------------------------------    
    Bem vindo ao SISTEMA de ASSEGURAMENTO
    Por favor, insira os dados corretamente:
    ------------------------------
        ''')

    vbs = float(input('Qual o Valor Do Bem a Ser Segurado?\n'))
    user = float(input('Qual o Numero de Usuários?\n'))
    ts = float(input('Qual a Taxa de Seguro?\n'))
    ds = float(input('Qual a Taxa de Desconto?\n'))
    np = float(input('Qual o Numero de Parcelas?\n'))

    vseg = vbs*(ts/100)
    vuser = vseg*(user/100)
    desc = (vseg+vuser)*(ds/100)
    seg = vseg+vuser-desc
    vparcela = seg/np

    print(f'''
    ------------------------------
    TABAJATA LTDA.
    ------------------------------
    Valor do Seguro: R${vseg};
    Valor Adicional por Usuário: R${vuser};
    Descontos: R${desc};
    Valor Liquido do Seguro: R${seg};
    Valor das Parcelas: R${vparcela};
    ------------------------------
    '''.format())

def continuar():
    time.sleep(1.5)
    print('Deseja continuar navegando nos projetos?')
    resp = input('Sim ou Não?\n')
    if resp.lower() == 'sim':
        print('Ok, redirecionando para o menu principal!')
        time.sleep(1.5)
    elif resp.lower() == 'nao':
        print('Tudo bem, obrigado por usar meu sistema!')
        time.sleep(1)
        quit()
    else:
        print('resposta inválida')


def main():
    while True:
        print('''\n Bem vindo aos Algoritmos - Aula 3\n
        Qual projeto você gostaria de executar?\n
        1. Cálculo de Salário Bruto\n
        2. Cálculo de Desconto\n
        3. Conversão Dolar-Real\n
        4. Projeto Tabajata\n
        5. Sobre\n
        6. Sair\n
        ''')
        sel = int(input('Selecione a opção: '))
        if sel == 1:
            print('O cálculo do salário bruto é: R$' + cal_sb()+'\n')
            continuar()
        elif sel == 2:
            print('O desconto do produto é: R$' + cal_dc()+'\n')
            continuar()
        elif sel == 3:
            print('O valor convertido é: ' + conv_DR()+'\n')
            continuar()
        elif sel == 4:
            tabajata()
            continuar()
        elif sel == 5:
            print('Esse projeto foi feito por Pedro Rocha'+'\n')
            continuar()
        else:
            print('Obrigado por usar meu sistema!')
            quit()


if __name__ == '__main__':
    main()
