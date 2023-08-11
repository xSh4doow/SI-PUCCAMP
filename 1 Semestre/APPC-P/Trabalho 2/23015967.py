# Inicio do Código - Importando as Libs
import time

from fase1_dataset import dataset, habilidades


# Printa as Habilidades
def show_Habilidades():
    for hab in habilidades:
        print('\033[32m' + hab + '\033[0;0m')


# Pega as Habilidades do Usuário
def get_Habilidades(datas):
    while True:
        user_hab = input('Selecione as habilidades que você mais se relaciona! Separe por vírgulas \n').split(', ')
        if not any(hab not in datas for hab in user_hab):
            return user_hab
        else:
            print('\033[31m' + 'A(s) habilidade(s) escrita(s) não está(ão) no nosso DataSet, tente novamente!' + '\033[0;0m')


# Calcula a Probabilidade
def calc_prob(ds, profissao, habilidade):
    for prof in ds:
        if prof['PROFISSÃO'] == profissao:
            vals = prof['HABILIDADES'].values()
            hab = prof['HABILIDADES'].get(habilidade)
            calc = round((hab / sum(vals)) * 100, 1)
            return calc


# Pegar as Habilidades do Usuário e Encontrar a Profissão
def match_Habilidades(u_input, ds):
    dic = {}
    for prof in ds:
        for hab in u_input:
            if hab in prof['HABILIDADES']:
                val = calc_prob(ds, prof['PROFISSÃO'], hab)
                if prof['PROFISSÃO'] not in dic:
                    dic.update({prof['PROFISSÃO']: val})
                else:
                    _val = dic.get(prof['PROFISSÃO'])
                    _nval = val + _val
                    dic.update({prof['PROFISSÃO']: _nval})

    return dict(sorted(dic.items(), key=(lambda item: item[1]), reverse=True))


# Formata a resposta final
def format_print(dic):
    print('De acordo com o que você inseriu, calculamos que:')
    for prof in dic:
        print('Você tem ' + "\033[36m" + str(dic.get(prof)) + "\033[0;0m" + '% de chance de se dar bem como: ' + "\033[35m" + prof + "\033[0;0m")
    print('-----------------------------------------------------------')


# Função para Continuar no Sistema
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


# Função Main
def main():
    print('\033[34m''''
-----------------------------------------------------------
Olá! Seja bem vindo(a) ao Sistema Seletor de Carreira!
Para continuar-mos, selecione as habilidades com as quais
você mais se relaciona:
-----------------------------------------------------------
HABILIDADES:''' + '\033[0;0m')
    show_Habilidades()
    u = get_Habilidades(habilidades)
    d = match_Habilidades(u, dataset)
    format_print(d)
    continuar()


if __name__ == '__main__':
    main()
