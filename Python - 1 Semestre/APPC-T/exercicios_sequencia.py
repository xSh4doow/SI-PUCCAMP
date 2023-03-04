import time as t


def celsius_to(temp):
    try:
        graus = float(input('Qual o valor em ºC?\n'))
        if temp == 'fah':
            fahrenheit = (9 / 5 * graus) + 32
            print(graus, "ºC equivalem a ", fahrenheit, "ºF", sep="")
        elif temp == 'kel':
            kelvin = graus + 273.15
            print(graus, "ºC equivalem a ", kelvin, "ºK", sep="")
        elif temp == 'rank':
            rankine = 1.8 * (graus + 273.15)
            print(graus, "ºC equivalem a ", rankine, "ºR", sep="")
    except:
        print('Por favor, insira somente valores numéricos!')


def fah_to(temp):
    try:
        graus = float(input('Qual o valor em ºF?\n'))
        if temp == 'cel':
            celsius = (graus - 32) / (9 / 5)
            print(graus, "ºF equivalem a ", celsius, "ºC", sep="")
        elif temp == 'kel':
            kelvin = ((graus - 32) / (9 / 5)) + 273.15
            print(graus, "ºF equivalem a ", kelvin, "ºK", sep="")
        elif temp == 'rank':
            rankine = graus + 459.67
            print(graus, "ºF equivalem a ", rankine, "ºR", sep="")
    except:
        print('Por favor, insira somente valores numéricos!')


def kel_to(temp):
    try:
        graus = float(input('Qual o valor em K?\n'))
        if temp == 'cel':
            celsius = graus - 273.15
            print(graus, "K equivalem a ", celsius, "ºC", sep="")
        elif temp == 'fah':
            fahrenheit = graus * 9 / 5 - 459.67
            print(graus, "K equivalem a ", fahrenheit, "ºF", sep="")
        elif temp == 'rank':
            rankine = graus * 9 / 5
            print(graus, "K equivalem a ", rankine, "ºR", sep="")
    except:
        print('Por favor, insira somente valores numéricos!')


def rank_to(temp):
    try:
        graus = float(input('Qual o valor em ºR?\n'))
        if temp == 'cel':
            celsius = (graus - 491.67) / 9 / 5
            print(graus, "ºRK equivalem a ", celsius, "ºC", sep="")
        elif temp == 'fah':
            fahrenheit = graus - 459.67
            print(graus, "ºR equivalem a ", fahrenheit, "ºF", sep="")
        elif temp == 'kel':
            kelvin = graus / (9 / 5)
            print(graus, "ºR equivalem a ", kelvin, "K", sep="")
    except:
        print('Por favor, insira somente valores numéricos!')


def main():
    while True:
        print('''
    ------------------------------------------------
        Lista de Exercícios de Sequência
    ------------------------------------------------
        1. Converter Celsius-Fahrenheit;
        2. Converter Fahrenheit-Celsius;
        3. Converter Celsius-Kelvin;
        4. Converter Kelvin-Celsius;
        5. Converter Celsius-Rankine;
        6. Converter Rankine-Celsius;
        7. Converter Fahrenheit-Kelvin;
        8. Converter Kelvin-Fahrenheit;
        9. Converter Fahrenheit-Rankine;
        10. Converter Rankine-Fahrenheit;
        11. Converter Kelvin-Rankine;
        12. Converter Rankine-Kelvin;
        13. Sair
    ------------------------------------------------
        Escolha sua opção:''')

        opt = int(input('''    '''))

        if opt == 1:
            celsius_to('fah')
        elif opt == 2:
            fah_to('cel')
        elif opt == 3:
            celsius_to('kel')
        elif opt == 4:
            kel_to('cel')
        elif opt == 5:
            celsius_to('rank')
        elif opt == 6:
            rank_to('cel')
        elif opt == 7:
            fah_to('kel')
        elif opt == 8:
            kel_to('fah')
        elif opt == 9:
            fah_to('rank')
        elif opt == 10:
            rank_to('fah')
        elif opt == 11:
            kel_to('rank')
        elif opt == 12:
            rank_to('kel')
        elif opt == 13:
            quit()
        else:
            print('Opção Inválida!')


if __name__ == '__main__':
    main()
