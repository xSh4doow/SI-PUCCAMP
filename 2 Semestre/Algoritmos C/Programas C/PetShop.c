//
// Created by pedro.rocha on 12/09/2023.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    unsigned int id;
    char         nome    [21];
    unsigned int idade;
    char         especie [31];
    char         raca    [31];
    char         cor     [21];
    char         tutor   [41];
}
        Pet;

unsigned int numero_natural_digitado (char pedido [], char mensagem [], unsigned int maximo)
{
    char   digitacao [1025];
    char*  erro;
    double real;

    for(;;) // forever
    {
        printf("%s",pedido);
        fgets (digitacao,1024,stdin);

        real=strtod(digitacao,&erro);

        if (*erro!=10) // foi digitado algum caractere não numérico
        {
            printf("%s",mensagem);
        }
        else if (real<0 || real>maximo)
        {
            printf("%s",mensagem);
        }
        else if (real != (unsigned int)real) // foi digitado algum número quebrado, tipo 1.5
        {
            printf("%s",mensagem);
        }
        else
            break;
    }

    return (unsigned int)real;
}

void digite_texto (char texto [], unsigned int maximo, char pedido [], char mensagem [])
{
    unsigned int errado, i;
    char digitacao [1025];

    for(;;) // forever
    {
        printf("%s",pedido);
        fgets (digitacao,maximo,stdin);
        digitacao[strlen(digitacao)-1]='\0';

        errado=0/*falso*/;
        for (i=0; digitacao[i]!='\0';i++)
            if (!(digitacao[i]==' ' || (digitacao[i]>='a' && digitacao[i]<='z') || (digitacao[i]>='A' && digitacao[i]<='Z')))
            {
                errado=1/*verdadeiro*/;
                break; // para a verificação, sem nem chegar na marca de fim, '\0', pois já achei um erro
            }

        if (errado)
        {
            printf("%s",mensagem);
        }
        else
            break; // para o forever que fica pedindo digitação e redigitação até digitar corretamente
    }

    strcpy(texto,digitacao);
}

unsigned int/*boolean*/ id_ja_cadastrado (Pet cli [], unsigned int qtd, unsigned int id)
{
    int i;
    for (i=0; i<qtd; i++)
        if (id==cli[i].id)
            return 1/*verdadeiro*/;

    return 0/*falso*/;
}

void cadastrar_pet (Pet cli [], unsigned int* qtd)
{
    if (*qtd==1000)
    {
        printf ("Não há espaço para mais pets!\n\n");
    }
    else
    {
        cli[*qtd].id = (*qtd)+1;

        digite_texto (cli[*qtd].nome,20,"Nome............: ","O nome deve conter até 20 letras e/ou espaços em branco\n");

        cli[*qtd].idade=numero_natural_digitado ("Idade (em meses): ","A Idade deve ser 1 ou 2 ou 3 ou etc, até 480; tente novamente!\n",480);

        digite_texto (cli[*qtd].especie,30,"Especie.........: ","A especie deve conter até 30 letras e/ou espaços em branco\n");
        digite_texto (cli[*qtd].raca,   30,"Raça............: ","A raça deve conter até 30 letras e/ou espaços em branco\n");
        digite_texto (cli[*qtd].cor,    20,"Cor.............: ","A cor deve conter até 20 letras e/ou espaços em branco\n");
        digite_texto (cli[*qtd].tutor,  40,"Tutor...........: ","O nome do tutor deve conter até 40 letras e/ou espaços em branco\n");

        (*qtd)++;

        printf("Cadastro realizado com sucesso!\n\n");
    }
}

void listar_pets (Pet cli [], unsigned int qtd)
{
    unsigned int i;

    if (qtd==0)
    {
        printf ("Não há pets cadastrados!\n\n");
        return;
    }

    for (i=0; i<qtd; i++)
        printf ("%u %s %u mês(es) %s %s %s %s\n", cli[i].id, cli[i].nome, cli[i].idade, cli[i].especie, cli[i].raca, cli[i].cor, cli[i].tutor);

    printf("\n");
}

void listar_pet (Pet cli [], unsigned int qtd)
{
    unsigned int i, id;

    if (qtd==0)
    {
        printf ("Não há pets cadastrados!\n\n");
        return;
    }

    id=numero_natural_digitado("Id: ","O Id deve ser 1 ou 2 ou 3 ou etc; tente novamente!\n\n",4294967295);

    for (i=0; i<qtd; i++)
        if (id==cli[i].id)
        {
            printf ("ID: %u, Nome: %s, Idade: %u Mês(es) Espécie: %s, Raça: %s, Cor: %s, Tutor: %s.\n\n", cli[i].id, cli[i].nome, cli[i].idade, cli[i].especie, cli[i].raca, cli[i].cor, cli[i].tutor);
            return;
        }

    printf ("Não existe pet cadastrado com este id!\n\n");
}

void alterar_pet(Pet cli[], unsigned int qtd, unsigned int id) {
    int i;

    for (i = 0; i < qtd; i++) {
        if (id == cli[i].id) {
            int opcao;

            do {
                printf("O que deseja alterar para o pet com ID %u?\n", id);
                printf("1) Nome\n");
                printf("2) Idade\n");
                printf("3) Espécie\n");
                printf("4) Raça\n");
                printf("5) Cor\n");
                printf("6) Tutor\n");
                printf("7) Sair\n");

                opcao = numero_natural_digitado("Opção? ", "Opções válidas estão entre 1 e 7; tente novamente!\n", 7);

                switch (opcao) {
                    case 1:
                        digite_texto(cli[i].nome, 20, "Novo nome: ", "O nome deve conter até 20 letras e/ou espaços em branco\n");
                        printf("Nome alterado com sucesso!\n\n");
                        break;

                    case 2:
                        cli[i].idade = numero_natural_digitado("Nova idade (em meses): ", "A Idade deve ser 1 ou 2 ou 3 ou etc, até 480; tente novamente!\n", 480);
                        printf("Idade alterada com sucesso!\n\n");
                        break;

                    case 3:
                        digite_texto(cli[i].especie, 30, "Nova espécie: ", "A especie deve conter até 30 letras e/ou espaços em branco\n");
                        printf("Espécie alterada com sucesso!\n\n");
                        break;

                    case 4:
                        digite_texto(cli[i].raca, 30, "Nova raça: ", "A raça deve conter até 30 letras e/ou espaços em branco\n");
                        printf("Raça alterada com sucesso!\n\n");
                        break;

                    case 5:
                        digite_texto(cli[i].cor, 20, "Nova cor: ", "A cor deve conter até 20 letras e/ou espaços em branco\n");
                        printf("Cor alterada com sucesso!\n\n");
                        break;

                    case 6:
                        digite_texto(cli[i].tutor, 40, "Novo tutor: ", "O nome do tutor deve conter até 40 letras e/ou espaços em branco\n");
                        printf("Tutor alterado com sucesso!\n\n");
                        break;

                    case 7:
                        return;  // Sair da função
                }
            } while (opcao != 7);
            return;
        }
    }

    printf("Não existe pet cadastrado com este ID!\n\n");
}


void excluir_pet (Pet cli [], unsigned int* qtd)
{
    unsigned int i, id=numero_natural_digitado("Id: ","O Id deve ser 1 ou 2 ou 3 ou etc; tente novamente!\n",4294967295);

    for (i=0; i<*qtd; i++)
        if (id==cli[i].id)
            break;

    if (i==*qtd)
    {
        printf ("Não existe pet cadastrado com este id!\n\n");
        return;
    }

    for ( ; i<*qtd-1; i++)
        cli[i] = cli[i+1];

    (*qtd)--;

    printf("Exclusão realizada com sucesso!\n\n");
}

int main() {
    Pet cliente[1000]; // tamanho 1000; posicoes de 0 a 999
    unsigned int qtd_de_pets = 0, opcao;

    printf("PROGRAMA PARA GERENCIAR PETS\n\n");

    do {
        printf("0) Cadastrar pet\n");
        printf("1) Listar    pet\n");
        printf("2) Listar    pets\n");
        printf("3) Excluir   pet\n");
        printf("4) Alterar   pet\n");
        printf("5) Sair\n");
        opcao = numero_natural_digitado("Opção? ", "Opções válidas estão entre 0 e 5; tente novamente!\n\n", 5);

        switch (opcao) {
            case 0:
                cadastrar_pet(cliente, &qtd_de_pets);
                break;

            case 1:
                listar_pet(cliente, qtd_de_pets);
                break;

            case 2:
                listar_pets(cliente, qtd_de_pets);
                break;

            case 3:
                excluir_pet(cliente, &qtd_de_pets);
                break;

            case 4:
                // Adicionar a opção para alterar informações do pet
                listar_pets(cliente, qtd_de_pets);  // Mostra os IDs dos pets disponíveis
                unsigned int id_alterar = numero_natural_digitado("Digite o ID do pet que deseja alterar: ",
                                                                  "ID inválido. Tente novamente!\n", 4294967295);
                alterar_pet(cliente, qtd_de_pets, id_alterar);
                break;

            case 5:
                break;  // Sair do loop principal

            default:
                printf("Opção inválida. Tente novamente!\n\n");
        }
    }
    while (opcao != 5);

    printf("OBRIGADO POR USAR ESTE PROGRAMA!\n\n");

    return 0;
}