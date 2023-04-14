# Insersão do Valor e Definição das Variáveis
numero = float(input('Digite o número que você quer escrito por extenso: '))
negativo = ''
if numero < 0:
    negativo = 'Menos'
    numero = numero * -1
unidade = int(numero // 1)
decimal = (round(numero - unidade, 2) * 10)
decimal_d = int(decimal // 1)
decimal_u = int((decimal - decimal_d) * 10 + 0.001)

txt_unidade = ''
txt_decimald = ''
txt_decimalu = ''
txt_ext = ''

Moeda = 'Reais'
Quebrado = 'Centavos'

# Começo da Lógica - Transformando cada dígito em seu correspondente extenso
if unidade == 0:
    txt_unidade = 'Zero'
if unidade == 1:
    txt_unidade = 'Um'
if unidade == 2:
    txt_unidade = 'Dois'
if unidade == 3:
    txt_unidade = 'Três'
if unidade == 4:
    txt_unidade = 'Quatro'
if unidade == 5:
    txt_unidade = 'Cinco'
if unidade == 6:
    txt_unidade = 'Seis'
if unidade == 7:
    txt_unidade = 'Sete'
if unidade == 8:
    txt_unidade = 'Oito'
if unidade == 9:
    txt_unidade = 'Nove'

if decimal_d == 1:
    if decimal_u == 0:
        txt_decimald = 'Dez'
    if decimal_u == 1:
        txt_decimald = 'Onze'
    if decimal_u == 2:
        txt_decimald = 'Doze'
    if decimal_u == 3:
        txt_decimald = 'Treze'
    if decimal_u == 4:
        txt_decimald = 'Quatorze'
    if decimal_u == 5:
        txt_decimald = 'Quinze'
    if decimal_u == 6:
        txt_decimald = 'Dezesseis'
    if decimal_u == 7:
        txt_decimald = 'Dezessete'
    if decimal_u == 8:
        txt_decimald = 'Dezoito'
    if decimal_u == 9:
        txt_decimald = 'Dezenove'
if decimal_d == 2:
    txt_decimald = 'Vinte'
if decimal_d == 3:
    txt_decimald = 'Trinta'
if decimal_d == 4:
    txt_decimald = 'Quarenta'
if decimal_d == 5:
    txt_decimald = 'Cinquenta'
if decimal_d == 6:
    txt_decimald = 'Sessenta'
if decimal_d == 7:
    txt_decimald = 'Setenta'
if decimal_d == 8:
    txt_decimald = 'Oitenta'
if decimal_d == 9:
    txt_decimald = 'Noventa'

if decimal_d != 1:
    if decimal_u == 1:
        txt_decimalu = 'Um'
    if decimal_u == 2:
        txt_decimalu = 'Dois'
    if decimal_u == 3:
        txt_decimalu = 'Três'
    if decimal_u == 4:
        txt_decimalu = 'Quatro'
    if decimal_u == 5:
        txt_decimalu = 'Cinco'
    if decimal_u == 6:
        txt_decimalu = 'Seis'
    if decimal_u == 7:
        txt_decimalu = 'Sete'
    if decimal_u == 8:
        txt_decimalu = 'Oito'
    if decimal_u == 9:
        txt_decimalu = 'Nove'


# Criação das Strings Finais
if txt_unidade == 'Um':
    Moeda = 'Real'
if txt_decimalu == 'Um' and not txt_decimald:
    Quebrado = 'Centavo'

if not txt_decimald and not txt_decimalu:
    txt_ext = f'{negativo} {txt_unidade} {Moeda}'
else:
    if decimal_d == 0:
        txt_ext = f'{negativo} {txt_unidade} {Moeda} e {txt_decimalu} {Quebrado}'
    else:
        if decimal_d == 1:
            txt_ext = f'{negativo} {txt_unidade} {Moeda} e {txt_decimald} {Quebrado}'
        if decimal_d >= 2:
            if decimal_u == 0:
                txt_ext = f'{negativo} {txt_unidade} {Moeda} e {txt_decimald} {Quebrado}'
            else:
                txt_ext = f'{negativo} {txt_unidade} {Moeda} e {txt_decimald} e {txt_decimalu} {Quebrado}'


# Retorno ao Usuário
print(f'O Valor R$: {numero} por extenso é:{txt_ext}!')
