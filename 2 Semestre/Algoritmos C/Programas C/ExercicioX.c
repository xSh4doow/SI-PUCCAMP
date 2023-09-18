//
// Created by pedro.rocha on 22/08/2023.
//

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

char DtoI(double N)
{
    if (N != (int)N)
    {
        return 0;
    }

    return 1;
}

int getN()
{
    char N[513];
    char ver;
    char *erro;
    double tamanho;
    int size;

    do
    {
        printf("Digite o tamanho do X que você quer criar: \n");
        fflush(stdin);
        fgets(N, 512, stdin);
        tamanho = strtod(N, &erro);
        ver = DtoI(tamanho);


        if (tamanho <=2 || *erro !=10 || ver == 0)
        {
            printf("Tamanho incorreto!\n");
        }

    } while (tamanho <=2 || *erro !=10 || ver == 0);

    size = (int)tamanho;

    return size;

}

void buildX(int tam)
{
    int i, j;
    for (i = 1; i <= tam; i++) {
        for (j = 1; j <= tam; j++) {
            if (i == j || j == tam - i + 1) {
                printf("O");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

void X()
{
    int Num;
    Num = getN();
    buildX(Num);
}

int main()
{
    setlocale(LC_ALL, "portuguese");
    X();
    return 0;
}


