//
// Created by pedro.rocha on 16/08/2023.
//

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

double pegarLado(int qual)
{
    char digitacao[513];
    char* erro;
    double lado;

    do
    {
        printf("Digite a medida (em CM) do %i lado: \n", qual);
        fflush(stdin);
        fgets(digitacao, 512, stdin);
        lado = strtod(digitacao, &erro);

        if (lado <=0 || *erro !=10)
        {
            printf("Tamanho incorreto!\n");
        }

    } while (lado <= 0|| *erro !=10);

    return lado;
}

int validarTri(double lado1, double lado2, double lado3)
{
    if (lado1 >= lado2 + lado3 || lado2 >= lado1 + lado3 || lado3  >= lado1 + lado2)
    {
        return 0;
    } else
    {
        return 1;
    }
}

char* classificacao(double lado1, double lado2, double lado3)
{
    if (lado1 == lado2 && lado2 == lado3)
    {
        return "Equilatero";
    }
    else if (lado1 == lado2 || lado2 == lado3 || lado1 == lado3)
    {
        return "Isoceles";
    }
    else
    {
        return "Escaleno";
    }
}

void triangulo()
{
    double l1, l2, l3;
    int valid;
    char* resp;

    l1 = pegarLado(1);
    l2 = pegarLado(2);
    l3 = pegarLado(3);

    printf("%.2lf, %.2lf, %.2lf\n", l1, l2, l3);
    valid = validarTri(l1, l2, l3);

    if (valid == 0)
    {
        wprintf(L"Esse triangulo não existe...\n");
        return;
    }
    else
    {
        resp = classificacao(l1, l2, l3);
        wprintf(L"O triangulo: %.2lf, %.2lf, %.2lf é: %s\n", l1, l2, l3, resp);
        return;
    }
}

int main()
{
    setlocale(LC_ALL, "");
    char cont;
    do
    {
        triangulo();
        wprintf(L"Deseja continuar? Se sim, digite S - Se não, digite qualquer outra coisa\n");
        scanf(" %c", &cont);
    } while (cont == 'S' || cont == 's');
    wprintf(L"Ok, até mais!\n");
    return 0;
}