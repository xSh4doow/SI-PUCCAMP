#include <stdio.h>

/*Lista de Exercícios 1*/

/*EXERCÍCIOS DE TEMPERATURA*/
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
    double temp;
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
            return toCel(temp, t);
        }
        case 'F':
        {
            return toFah(temp, t);
        }
        case 'R':
        {
            return toRan(temp, t);
        }
        case 'K':
        {
            return toKel(temp, t);
        }
    }
}
void temperaturas()
{
    double resp;
    resp = funTemp();
    printf("%.2lf e a temperatura convertida!", resp);
}

/*EXERCÍCIOS DE PERÍMETRO*/
double p_circulo()
{
    double A;
    printf("Digite a medida do raio da circunferencia: \n");
    scanf("%lf", &A);

    return (2*3.1415*A);
}
double p_polireg()
{
    double A, B;
    printf("Digite quantos lados o Poligono tem e em seguida a medida do lado: \n");
    scanf("%lf %lf", &A, &B);

    return (A*B);
}
double p_trapezio()
{
    double A, B, C;
    printf("Digite as medidas da Altura, da Base e da Diagonal do Trapezio: \n");
    scanf("%lf %lf %lf", &A, &B, &C);

    return (A+B+2*C);
}
double p_retangulo()
{
    double A, B;
    printf("Digite as medidas da Altura e da Base do Retangulo: \n");
    scanf("%lf %lf", &A, &B);

    return (A*2+B*2);
}
double p_quadrado()
{
    double A;
    printf("Digite a medida de um lado do Quadrado: \n");
    scanf("%lf", &A);

    return (A*4);
}
double p_triangulo()
{
    double A,B,C;
    printf("Digite as medidas dos lados: A, B e C do Triangulo: \n");
    scanf("%lf %lf %lf", &A, &B, &C);

    return A+B+C;
}
void perimetro()
{
    char sel;
    double resp;
    printf("Qual figura voce quer calcular o perimetro? (TODOS OS VALORES SAO EM CM!)\n");
    printf("T - Triangulo, Q - Quadrado/Losango, R - Retangulo/Paralelogramo, Z - Trapezio,"
           " P - Poligono Regular, C - Circulo:\n");
    scanf(" %c", &sel);
    printf("Foi selecionado: %c\n", sel);

    switch (sel)
    {
        case 'T':
        {
            resp = p_triangulo();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        case 'Q':
        {
            resp = p_quadrado();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        case 'R':
        {
            resp = p_retangulo();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        case 'Z':
        {
            resp = p_trapezio();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        case 'P':
        {
            resp = p_polireg();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        case 'C':
        {
            resp = p_circulo();
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
        }
        default:
            resp = 0.0;
            printf("O Perimetro e de: %.2lfcm!", resp);
            return;
    }

}

/*EXERCÍCIOS DE ÁREA*/
double a_circulo()
{
    double A;
    printf("Digite a medida do raio da circunferencia: \n");
    scanf("%lf", &A);

    return (3.1415*A*A);
}
double a_polireg()
{
    double A, B, C;
    printf("Digite quantos lados o Poligono tem, a medida da Base e seu Apotema: \n");
    printf("*Apotema e a linha imaginaria que une o centro ao meio da base* \n");
    scanf("%lf %lf", &A, &B, &C);

    return ((A*B*C)/2);
}
double a_trapezio()
{
    double A, B, C;
    printf("Digite as medidas da Base Maior, da Base Menor e da Altura do Trapezio: \n");
    scanf("%lf %lf %lf", &A, &B, &C);

    return (((A+B)*C)/2);
}
double a_losango()
{
    double A, B;
    printf("Digite as medidas da Diagonal Maior e Menor do Losango/Paralelogramo: \n");
    scanf("%lf %lf", &A, &B);

    return ((A*B)/2);
}
double a_retangulo()
{
    double A, B;
    printf("Digite as medidas da Altura e da Base do Retangulo: \n");
    scanf("%lf %lf", &A, &B);

    return (A*B);
}
double a_quadrado()
{
    double A;
    printf("Digite a medida de um lado do Quadrado: \n");
    scanf("%lf", &A);

    return (A*A);
}
double a_triangulo()
{
    double A,B;
    printf("Digite as medidas da Altura e Base do Triangulo: \n");
    scanf("%lf %lf", &A, &B);

    return ((A*B)/2);
}
void area()
{
    char sel;
    double resp;
    printf("Qual figura voce quer calcular a Area? (TODOS OS VALORES SAO EM CM!)\n");
    printf("T - Triangulo, Q - Quadrado, R - Retangulo, Z - Trapezio, L - Losango/Paralelogramo,"
           " P - Poligono Regular, C - Circulo:\n");
    scanf(" %c", &sel);
    printf("Foi selecionado: %c\n", sel);

    switch (sel)
    {
        case 'T':
        {
            resp = a_triangulo();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'Q':
        {
            resp = a_quadrado();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'R':
        {
            resp = a_retangulo();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'Z':
        {
            resp = a_trapezio();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'L':
        {
            resp = a_losango();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'P':
        {
            resp = a_polireg();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        case 'C':
        {
            resp = a_circulo();
            printf("A Area e de: %.2lfcm2!", resp);
            return;
        }
        default:
            resp = 0.0;
            printf("A Area e de: %.2lfcm2!", resp);
            return;
    }

}

/*OUTROS CALCULOS*/
void imc()
{
    double imc, peso, altura;
    printf("CALCULO DE IMC!\n Digite seu Peso e sua Altura (PESO EM KG - ALTURA EM M):\n");
    scanf("%lf %lf", &peso, &altura);

    imc = (peso/(altura*altura));

    printf("SEU IMC E DE: %.2lf!", imc);

}
void funcao()
{
    double resp, a, b;
    printf("SISTEMA DE RESOLUCAO DE EQUACAO - FUNCAO DO FORMATO: AX+B=0\n");
    printf("Digite os coeficientes A e B:\n");
    scanf("%lf %lf", &a, &b);

    resp = (-(b)/a);

    printf("A resposta da equacao e: %.2lf!", resp);

}
void calculos()
{
    char sel;
    printf("Voce quer calcular Area, Perimetro, IMC ou Funcao 1 Grau\n");
    printf("(A - Area, P - Perimetro, I - IMC, F - Funcao):\n");
    scanf(" %c", &sel);

    switch (sel)
    {
        case 'P':
        {
            perimetro();
            return;
        }
        case 'A':
        {
            area();
            return;
        }
        case 'I':
        {
            imc();
            return;
        }
        case 'F':
        {
            funcao();
            return;
        }
    }
}



int main()
{
    int sel = 0;
    printf("LISTA DE EXERCICIOS 1\n");
    printf("Aperte 1 para Exercicios de Temperatura ou 2 para Exercicios de Calculo\n");
    scanf(" %i", &sel);

    switch (sel)
    {
        case 1:
        {
            temperaturas();
            return 0;
        }
        case 2:
        {
            calculos();
            return 0;
        }
        default:
        {
            printf("Você inseriu uma opção inválida, tente novamente!");
        }
    }

    return 0;
}