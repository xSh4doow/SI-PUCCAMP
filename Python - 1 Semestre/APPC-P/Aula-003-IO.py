# coding=utf-8
# Algoritmos aula 3

import time


def cal_sb():
    sh = float(input('Qual o Salário Hora do Funcionário?\n'))
    ht = int(input('Quantas Horas o Funcionário Trabalhou? (Horas completas)\n'))
    sb = sh * ht
    return sb


def cal_dc():
    vp = float(input('Qual o valor do produto?\n'))
    pd = float(input('Qual o percentual de desconto? (sem a porcentagem - ex: 5 se 5%)\n'))
    d = vp * (pd / 100)
    return str(d)


def conv_DR():
    cot = float(input('Qual a cotação do dólar hoje? Ela pode ser encontrada em: https://dolarhoje.com/\n'))
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

    vseg = vbs * (ts / 100)
    vuser = vseg * (user / 100)
    desc = (vseg + vuser) * (ds / 100)
    seg = vseg + vuser - desc
    vparcela = seg / np

    print(f'''
    ------------------------------
    TABAJATA LTDA.
    ------------------------------
    Valor do Seguro: R${round(vseg, 2)};
    Valor Adicional por Usuário: R${round(vuser, 2)};
    Descontos: R${round(desc, 2)};
    Valor Liquido do Seguro: R${round(seg, 2)};
    Valor das Parcelas: R${round(vparcela, 2)};
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


def cal_inss(sb):
    aplica = input('Se Aplica INSS? - Teto de R$7.507,49 - S ou N\n')
    inss = 0
    if aplica.lower() == 's':
        if sb <= 1302.00:
            pf = (7.5 / 100)
            inss = sb * pf
        elif 1302 < sb <= 2571.29:
            pf = 97.65
            sf = (sb - 1302) * (9 / 100)
            inss = pf+sf
        elif 2571.29 < sb < 3856.94:
            pf = 97.65
            sf = 114.24
            tf = (sb - 2571.29) * (12 / 100)
            inss = pf + sf + tf
        elif 3856.94 < sb <= 7507.49:
            pf = 97.65
            sf = 114.24
            tf = 154.28
            qf = (sb - 3856.94) * (14 / 100)
            inss = pf + sf + tf + qf
    novo_valor = sb - inss
    return inss, novo_valor


def cal_dp():
    ndp = int(input('Quantos dependentes? 0, 1, 2...\n'))
    dps = (ndp * 189.59)
    return dps


def cal_irrf(valor):
    ded = 0
    faixa = 0
    if valor <= 1903.98:
        faixa = 1
        ded = 0
    elif 1903.98 < valor <= 2826.65:
        faixa = 2
        ded = (valor * (7.5/100)) - 142.80
    elif 2826.65 < valor <= 3751.05:
        faixa = 3
        ded = (valor * (15/100)) - 354.80
    elif 3751.05 < valor <= 4664.68:
        faixa = 4
        ded = (valor * (22.5/100)) - 636.13
    elif valor > 4664.68:
        faixa = 5
        ded = (valor * (27.5/100)) - 869.36
    return ded, faixa


def cal_sl():
    sb = cal_sb()
    print('O Valor do Salário Bruto é R$' + str(round(sb, 2)) + '\n')
    inss = cal_inss(sb)
    print('O Valor do INSS é R$' + str(round(inss[0], 2)) + ' e o Valor com o INSS já abatido é R$' + str(round(inss[1], 2)) + '\n')
    dps = cal_dp()
    print('O Valor deduzido pelos dependentes é R$' + str(round(dps, 2)) + '\n')
    v_irrf = inss[1] - dps
    irrf = cal_irrf(v_irrf)
    print(f'O Valor que foi usado no cálculo do IR é de R$ {round(v_irrf, 2)}, que se encaixa na {round(irrf[1], 2)}a faixa e portanto teve uma dedução de R${round(irrf[0], 2)}' + '\n')
    dd = float(input('Existem demais descontos no salário? Se sim, quantos R$ de desconto? Se não, digite 0'))
    sl = v_irrf - irrf[0] - dd
    print('O Valor do Salário Liquido é R$' + str(round(sl, 2)) + '\n')


def main():
    while True:
        print('''\n Bem vindo aos Algoritmos - Aula 3\n
        Qual projeto você gostaria de executar?\n
        1. Cálculo de Salário Bruto\n
        2. Cálculo de Desconto\n
        3. Conversão Dolar-Real\n
        4. Cálculo de Salário Liquido / Imposto de Renda\n
        5. Projeto Tabajata\n
        6. Sobre\n
        7. Mensagem para o Professor\n
        8. Sair\n
        ''')
        sel = int(input('Selecione a opção: '))
        if sel == 1:
            print('O cálculo do salário bruto é: R$' + str(cal_sb()) + '\n')
            continuar()
        elif sel == 2:
            print('O desconto do produto é: R$' + cal_dc() + '\n')
            continuar()
        elif sel == 3:
            print('O valor convertido é: ' + conv_DR() + '\n')
            continuar()
        elif sel == 4:
            cal_sl()
            continuar()
        elif sel == 5:
            tabajata()
            continuar()
        elif sel == 6:
            print(
                'Esse projeto foi feito por Pedro Rocha\nSe deseja ver mais, acesse: https://github.com/xSh4doow' + '\n')
            continuar()
        elif sel == 7:
            print('Fala Prof! Gostaria de te avisar que não fiz o uso de Try/Excepts no projeto. Isso se dá pelo fato que suponho que o Senhor irá utilizar o sistema de forma correta. Desde já agradeço a compreensão e o uso devido dos tipos.')
        else:
            print('Obrigado por usar meu sistema!')
            quit()


if __name__ == '__main__':
    main()
