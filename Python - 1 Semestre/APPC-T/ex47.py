def extenso():
    while True:
        try:
            numero = float(input('''
---------------------------------
BANCO DE RAPIDÓPOLIS CORP
---------------------------------
DIGITE O NÚMERO:\n'''))
        except ValueError:
            print('SOMENTE VALORES NUMÉRICOS')
        else:
            numeros = list(str(numero))
            dic = {'0': 'Zero', '1': 'Um', '2': 'Dois', '3': 'Três', '4': 'Quatro', '5': 'Cinco', '6': 'Seis', '7': 'Sete', '8': 'Oito', '9': 'Nove',
                   '.': 'Vírgula', '-': 'Menos'}
            i = 0
            l_ext = []
            for num in numeros:
                num = numeros[i]
                extens = dic.get(num)
                l_ext.append(extens)
                i += 1

            if numero > 0:
                positivo = True
            elif numero < 0:
                positivo = False

            def unidade():
                retorno = str(l_ext).removesuffix("', 'Vírgula', 'Zero']").removeprefix("['").replace("'", '').replace(',', '')
                return retorno

            def dezena(d):
                if l_ext[d] == 'Um':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Dez'
                    elif l_ext[d + 1] == 'Um':
                        retorno = 'Onze'
                    elif l_ext[d + 1] == 'Dois':
                        retorno = 'Doze'
                    elif l_ext[d + 1] == 'Três':
                        retorno = 'Treze'
                    elif l_ext[d + 1] == 'Quatro':
                        retorno = 'Quatorze'
                    elif l_ext[d + 1] == 'Cinco':
                        retorno = 'Quinze'
                    elif l_ext[d + 1] == 'Seis':
                        retorno = 'Dezesseis'
                    elif l_ext[d + 1] == 'Sete':
                        retorno = 'Dezessete'
                    elif l_ext[d + 1] == 'Oito':
                        retorno = 'Dezoito'
                    elif l_ext[d + 1] == 'Nove':
                        retorno = 'Dezenove'
                elif l_ext[d] == 'Dois':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Vinte'
                    else:
                        retorno = f'Vinte e {l_ext[d + 1]}'
                elif l_ext[d] == 'Três':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Trinta'
                    else:
                        retorno = f'Trinta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Quatro':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Quarenta'
                    else:
                        retorno = f'Quarenta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Cinco':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Cinquenta'
                    else:
                        retorno = f'Cinquenta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Seis':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Sessenta'
                    else:
                        retorno = f'Sessenta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Sete':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Setenta'
                    else:
                        retorno = f'Setenta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Oito':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Oitenta'
                    else:
                        retorno = f'Oitenta e {l_ext[d + 1]}'
                elif l_ext[d] == 'Nove':
                    if l_ext[d + 1] == 'Zero':
                        retorno = 'Noventa'
                    else:
                        retorno = f'Noventa e {l_ext[d + 1]}'
                return retorno

            def dezena_centena(c,d):
                cent = str(c)
                if l_ext[d + 1] == 'Um':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Dez'
                    elif l_ext[d + 2] == 'Um':
                        retorno = f'{cent} e Onze'
                    elif l_ext[d + 2] == 'Dois':
                        retorno = f'{cent} e Doze'
                    elif l_ext[d + 2] == 'Três':
                        retorno = f'{cent} e Treze'
                    elif l_ext[d + 2] == 'Quatro':
                        retorno = f'{cent} e Quatorze'
                    elif l_ext[d + 2] == 'Cinco':
                        retorno = f'{cent} e Quinze'
                    elif l_ext[d + 2] == 'Seis':
                        retorno = f'{cent} e Dezesseis'
                    elif l_ext[d + 2] == 'Sete':
                        retorno = f'{cent} e Dezessete'
                    elif l_ext[d + 2] == 'Oito':
                        retorno = f'{cent} e Dezoito'
                    elif l_ext[d + 2] == 'Nove':
                        retorno = f'{cent} e Dezenove'
                elif l_ext[d + 1] == 'Dois':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Vinte'
                    else:
                        retorno = f'{cent} e Vinte e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Três':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Trinta'
                    else:
                        retorno = f'{cent} e Trinta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Quatro':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Quarenta'
                    else:
                        retorno = f'{cent} e Quarenta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Cinco':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Cinquenta'
                    else:
                        retorno = f'{cent} e Cinquenta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Seis':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Sessenta'
                    else:
                        retorno = f'{cent} e Sessenta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Sete':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Setenta'
                    else:
                        retorno = f'{cent} e Setenta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Oito':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Oitenta'
                    else:
                        retorno = f'{cent} e Oitenta e {l_ext[d + 2]}'
                elif l_ext[d + 1] == 'Nove':
                    if l_ext[d + 2] == 'Zero':
                        retorno = f'{cent} e Noventa'
                    else:
                        retorno = f'{cent} e Noventa e {l_ext[d + 2]}'
                return retorno

            def centena(d,c):
                retorno = ''
                if l_ext[d] == 'Um':
                    cent = 'Cento'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Cem'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Dois':
                    cent = 'Duzentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Duzentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Três':
                    cent = 'Trezentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Trezentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Quatro':
                    cent = 'Quatrocentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Quatrocentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Cinco':
                    cent = 'Quinhentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Quinhentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Seis':
                    cent = 'Seiscentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Seiscentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Sete':
                    cent = 'Setecentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Setecentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Oito':
                    cent = 'Oitocentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Oitocentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'
                elif l_ext[d] == 'Nove':
                    cent = 'Novecentos'
                    if l_ext[d + 1] == 'Zero' and l_ext[d + 2] == 'Zero':
                        retorno = 'Novecentos'
                    elif l_ext[d + 1] != 'Zero':
                        retorno = dezena_centena(cent,c)
                    elif l_ext[d + 1] == 'Zero':
                        retorno = f'{cent} e {l_ext[d + 2]}'

                return retorno

            def decimal():
                l_ext_i = l_ext.copy()[:-2]
                if positivo:
                    if len(l_ext_i) == 2:
                        retorno1 = unidade()
                    elif len(l_ext_i) == 3:
                        retorno1 = dezena(0)
                    elif len(l_ext_i) == 4:
                        retorno1 = centena(0,0)
                    if l_ext[-2] == 'Zero':
                        retorno2 = str(l_ext[-1]).removesuffix("']").removeprefix("['")
                    else:
                        retorno2 = dezena(4)
                    return retorno1, retorno2
                elif not positivo:
                    if len(l_ext_i) == 3:
                        retorno1 = unidade()
                    elif len(l_ext_i) == 4:
                        retorno1 = dezena(0)
                    elif len(l_ext_i) == 5:
                        retorno1 = centena(1,1)
                    if l_ext[-2] == 'Zero':
                        retorno2 = str(l_ext[-1]).removesuffix("']").removeprefix("['")
                    else:
                        retorno2 = dezena(4)
                    return retorno1, retorno2

            if positivo:
                if len(l_ext) == 3:
                    print(f'---------------------------------\nO número {numero} em extenso é', unidade(), '\n---------------------------------')
                    break
                elif len(l_ext) == 4:
                    print(f'---------------------------------\nO número {numero} em extenso é', dezena(0), '\n---------------------------------')
                    break
                elif len(l_ext) == 5:
                    print(f'---------------------------------\nO número {numero} em extenso é', centena(0, 0), '\n---------------------------------')
                    break
                elif len(l_ext) > 5:
                    print(
                        f'---------------------------------\nO número {numero} em extenso é {decimal()[0]} vírgula {decimal()[1]}\n---------------------------------')
                    break
            elif not positivo:
                if len(l_ext) == 4:
                    print(f'---------------------------------\nO número {numero} em extenso é ', unidade(), '\n---------------------------------')
                    break
                elif len(l_ext) == 5:
                    print(f'---------------------------------\nO número {numero} em extenso é menos', dezena(1),
                          '\n---------------------------------')
                    break
                elif len(l_ext) == 6:
                    print(f'---------------------------------\nO número {numero} em extenso é menos', centena(1, 1),
                          '\n---------------------------------')
                    break
                elif len(l_ext) > 6:
                    print(
                        f'---------------------------------\nO número {numero} em extenso é {decimal()[0]} vírgula {decimal()[1]}\n---------------------------------')
                    break


extenso()
