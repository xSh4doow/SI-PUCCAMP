def celsius_to(temp):
    while True:
        try:
            graus = float(input('Qual o valor em ºC?\n'))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if temp == 'fah':
                fahrenheit = ((9 / 5) * graus) + 32
                print(graus, "ºC equivalem a ", round(fahrenheit, 2), "ºF", sep="")
                break
            elif temp == 'kel':
                kelvin = graus + 273.15
                print(graus, "ºC equivalem a ", round(kelvin, 2), "ºK", sep="")
                break
            elif temp == 'rank':
                rankine = 1.8 * (graus + 273.15)
                print(graus, "ºC equivalem a ", round(rankine, 2), " Rankine", sep="")
                break
            elif temp == 'reau':
                reau = graus * (4/5)
                print(graus, "ºC equivalem a ", round(reau, 2), "ºR", sep="")
                break


def fah_to(temp):
    while True:
        try:
            graus = float(input('Qual o valor em ºF?\n'))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if temp == 'cel':
                celsius = (graus - 32) / (9 / 5)
                print(graus, "ºF equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'kel':
                kelvin = ((graus - 32) / (9 / 5)) + 273.15
                print(graus, "ºF equivalem a ", round(kelvin, 2), "ºK", sep="")
                break
            elif temp == 'rank':
                rankine = graus + 459.67
                print(graus, "ºF equivalem a ", round(rankine, 2), " Rankine", sep="")
                break
            elif temp == 'reau':
                reau = (graus - 32)*(4/9)
                print(graus, "ºF equivalem a ", round(reau, 2), "ºR", sep="")
                break


def kel_to(temp):
    while True:
        try:
            graus = float(input('Qual o valor em K?\n'))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if temp == 'cel':
                celsius = graus - 273.15
                print(graus, "K equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'fah':
                fahrenheit = graus * (9 / 5) - 459.67
                print(graus, "K equivalem a ", round(fahrenheit, 2), "ºF", sep="")
                break
            elif temp == 'rank':
                rankine = graus * (9 / 5)
                print(graus, "K equivalem a ", round(rankine, 2), " Rankine", sep="")
                break
            elif temp == 'reau':
                reau = (graus - 273.15) * (4/5)
                print(graus, "K equivalem a ", round(reau, 2), "ºR", sep="")
                break


def rank_to(temp):
    while True:
        try:
            graus = float(input('Qual o valor em Rankine?\n'))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if temp == 'cel':
                celsius = (graus - 491.67) / (9 / 5)
                print(graus, " Rankine equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'fah':
                fahrenheit = graus - 459.67
                print(graus, " Rankine equivalem a ", round(fahrenheit, 2), "ºF", sep="")
                break
            elif temp == 'kel':
                kelvin = graus / (9 / 5)
                print(graus, " Rankine equivalem a ", round(kelvin, 2), "K", sep="")
                break
            elif temp == 'reau':
                reau = (graus - 32 - 459.67) / (9/4)
                print(graus, " Rankine equivalem a ", round(reau, 2), "ºR", sep="")
                break


def reau_to(temp):
    while True:
        try:
            graus = float(input('Qual o valor em Réaumur?\n'))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if temp == 'cel':
                celsius = graus * (5/4)
                print(graus, "ºR equivalem a ", round(celsius, 2), "ºC", sep="")
                break
            elif temp == 'fah':
                fahrenheit = (graus * (9/4)) + 32
                print(graus, "ºR equivalem a ", round(fahrenheit, 2), "ºF", sep="")
                break
            elif temp == 'kel':
                kelvin = (graus * (5/4)) + 273.15
                print(graus, "ºR equivalem a ", round(kelvin, 2), "K", sep="")
                break
            elif temp == 'rank':
                rankine = (graus * (9/4)) + 32 + 459.67
                print(graus, "ºR equivalem a ", round(rankine, 2), " Rankine", sep="")
                break


def main():
    while True:
        print('''
------------------------------------------------
    CONVERSÃO DE TEMPERATURAS
------------------------------------------------
    1. Converter Celsius-Fahrenheit
    2. Converter Celsius-Kelvin
    3. Converter Celsius-Rankine
    4. Converter Celsius-Reaumur
    5. Converter Fahrenheit-Celsius
    6. Converter Fahrenheit-Kelvin
    7. Converter Fahrenheit-Rankine
    8. Converter Fahrenheit-Reaumur
    9. Converter Kelvin-Celsius
   10. Converter Kelvin-Fahrenheit
   11. Converter Kelvin-Rankine
   12. Converter Kelvin-Reaumur
   13. Converter Rankine-Celsius
   14. Converter Rankine-Fahrenheit
   15. Converter Rankine-Kelvin
   16. Converter Rankine-Reaumur
   17. Converter Reaumur-Celsius
   18. Converter Reaumur-Fahrenheit
   19. Converter Reaumur-Kelvin
   20. Converter Reaumur-Rankine
   21. Sair
------------------------------------------------
        Escolha sua opção:''')
        try:
            opt = int(input('''    '''))
        except ValueError:
            print('Por favor, insira somente valores numéricos!')
        else:
            if opt == 1:
                celsius_to('fah')
                break
            elif opt == 2:
                celsius_to('kel')
                break
            elif opt == 3:
                celsius_to('rank')
                break
            elif opt == 4:
                celsius_to('reau')
                break
            elif opt == 5:
                fah_to('cel')
                break
            elif opt == 6:
                fah_to('kel')
                break
            elif opt == 7:
                fah_to('rank')
                break
            elif opt == 8:
                fah_to('reau')
                break
            elif opt == 9:
                kel_to('cel')
                break
            elif opt == 10:
                kel_to('fah')
                break
            elif opt == 11:
                kel_to('rank')
                break
            elif opt == 12:
                kel_to('reau')
                break
            elif opt == 13:
                rank_to('cel')
                break
            elif opt == 14:
                rank_to('fah')
                break
            elif opt == 15:
                rank_to('kel')
                break
            elif opt == 16:
                rank_to('reau')
                break
            elif opt == 17:
                reau_to('cel')
                break
            elif opt == 18:
                reau_to('fah')
                break
            elif opt == 19:
                reau_to('kel')
                break
            elif opt == 20:
                reau_to('rank')
                break
            elif opt == 21:
                break
            else:
                print('Opção Inválida!')