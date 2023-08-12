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
        }
        case 'K':
        {
            celsius = (temp-273.15);
            return celsius;
        }
        case 'R':
        {
            celsius = (temp/1.8) - 273.15;
            return celsius;
        }
        case 'C':
            celsius = temp;
            return celsius;
    }
    return celsius;
}
double toFah(float temp, char t)
{
    double fahrenheit = 0;
    switch (t)
    {
        case 'F':
        {
            fahrenheit = temp;
            return fahrenheit;
        }
        case 'K':
        {
            fahrenheit = (temp - 32) * 5/9 + 273.15;
            return fahrenheit;
        }
        case 'R':
        {
            fahrenheit = temp + 459.67;
            return fahrenheit;
        }
        case 'C':
            fahrenheit = (temp - 32) * (5/9);
            return fahrenheit;
    }
    return fahrenheit;
}
double toKel(float temp, char t)
{
    double kelvin = 0;
    switch (t)
    {
        case 'F':
        {
            kelvin = (temp - 32.0) * 5.0/9.0 + 273.15;
            return kelvin;
        }
        case 'K':
        {
            kelvin = temp;
            return kelvin;
        }
        case 'R':
        {
            kelvin = temp / 1.8;
            return kelvin;
        }
        case 'C':
            kelvin = temp + 273.15;
            return kelvin;
    }
    return kelvin;
}
double toRan(float temp, char t)
{
    double rankine = 0;
    switch (t)
    {
        case 'F':
        {
            rankine = temp + 459.67;
            return rankine;
        }
        case 'K':
        {
            rankine = temp * 9.0/5.0;
            return rankine;
        }
        case 'R':
        {
            rankine = temp;
            return rankine;
        }
        case 'C':
            rankine = (temp + 273.15) * 9.0/5.0;
            return rankine;
    }
    return rankine;
}
char convTo()
{
    char t_t;
    printf("Para qual escala voce quer converter? Siga a mesma regra acima!\n");
    scanf(" %c", &t_t);
    printf("Convertendo para %c! Aguarde...\n", t_t);
    return t_t;
}
double funTemp()
{
    double temp, resp;
    char t, t_t;

    printf("Digite a temperatura atual e, em seguida, sua escala.\n"
           "('C' para Celsius, 'F' para Fahrenheit,'K' para Kelvin, 'R' para Rankine):\n");
    scanf("%lf %c", &temp, &t);
    printf("Temperatura:%f%c\n", temp, t);
    t_t = convTo();

    switch (t_t)
    {
        case 'C':
        {
            resp = toCel(temp, t);
        }
        case 'F':
        {
            resp = toFah(temp, t);
        }
        case 'R':
        {
            resp = toRan(temp, t);
        }
        case 'K':
        {
            resp = toKel(temp, t);
        }
    }

    return resp;
}
void temperaturas()
{
    double resp;
    resp = funTemp();
    printf("%.2lf e a temperatura convertida!", resp);
}

int main()
{
    int sel = 0;
    printf("LISTA DE EXERCICIOS 1\n");
    printf("Aperte 1 para exercícios de Temperatura\n");
    scanf(" %d", sel);
    // ARRUMAR ESSA PORRA!!!!


    return 0;
}