#include <stdio.h>

/*Lista de Exercícios 1*/

double toCel(float temp, char t)
{
    double celsius = 0;
    switch (t)
    {
        case 'F':
        {
            celsius = (5.0/9.0)*(temp-32.0);
            return celsius;
        };
        case 'K':
        {
            celsius = (temp-273.15);
            return celsius;
        };
        case 'R':
        {
            celsius = (temp/1.8) - 273.15;
            return celsius;
        };
    }
    return celsius;
}

double funTemp()
{
    double temp, resp;
    char t;

    printf("Digite a temperatura atual e, em seguida, sua escala.\n"
           "('C' para Celsius, 'F' para Fahrenheit,'K' para Kelvin, 'R' para Rankine):\n");

    scanf("%lf %c", &temp, &t);

    printf("Temperatura:%f%c\n", temp, t);

    /*Cálculos para Celsius*/
    resp = toCel(temp, t);

    return resp;
};

int main()
{
    double resp;
    printf("LISTA DE EXERCICIOS 1\n");
    resp = funTemp();
    printf("%lf e a temperatura convertida em C!", resp);

    return 0;
}