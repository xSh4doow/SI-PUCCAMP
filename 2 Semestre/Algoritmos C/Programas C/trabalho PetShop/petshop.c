#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define file "arquivo.dat"

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

unsigned int quantidadeDePets (FILE* arq)
{
    fseek(arq,0,SEEK_END);
    return ftell(arq)/sizeof(Pet);
}

unsigned int proximo_id (FILE* arq)
{
    if (quantidadeDePets(arq)==0) return 1;

    Pet ultimo;
    fseek(arq,-sizeof(Pet),SEEK_END);
    fread(&ultimo,1,sizeof(Pet),arq);
    return ultimo.id+1;
}

void cadastrar_pet (FILE* arq)
{
    Pet p;

    p.id = proximo_id(arq);

    digite_texto (p.nome,20,"Nome............: ","O nome deve conter até 20 letras e/ou espaços em branco\n");

    p.idade=numero_natural_digitado ("Idade (em meses): ","A Idade deve ser 1 ou 2 ou 3 ou etc, até 480; tente novamente!\n",480);

    digite_texto (p.especie,30,"Especie.........: ","A especie deve conter até 30 letras e/ou espaços em branco\n");
    digite_texto (p.raca,   30,"Raça............: ","A raça deve conter até 30 letras e/ou espaços em branco\n");
    digite_texto (p.cor,    20,"Cor.............: ","A cor deve conter até 20 letras e/ou espaços em branco\n");
    digite_texto (p.tutor,  40,"Tutor...........: ","O nome do tutor deve conter até 40 letras e/ou espaços em branco\n");

    // SEEK_END: pto de referencia = fim; SEEK_SET: pto de referencia = inicio; SEEK_CUR: pto de referencia = posicao corrento ou atual, o que da no mesmo
    fseek(arq,0,SEEK_END); // posiciono a 0 bytes do fim
    fwrite(&p,sizeof(Pet),1,arq); // grava no arq 1 struct do tamanho sizeof(Pet) e a struct sera p

    printf("Cadastro realizado com sucesso!\n\n");
}

void listar_pets(FILE* arq) {
    fseek(arq, 0, SEEK_SET); // Move a posição do arquivo para o início (seek do in)
    Pet p;
    while (fread(&p, sizeof(Pet), 1, arq) == 1) { // Lê uma estrutura Pet do arquivo
        printf("%u %s %u mês(es) %s %s %s %s\n", p.id, p.nome, p.idade, p.especie, p.raca, p.cor, p.tutor); // Exibe os detalhes do pet
    }
    printf("\n"); // Adiciona uma linha em branco após listar todos os pets
}

void listar_pet(FILE* arq) {
    unsigned int id = numero_natural_digitado("Id: ", "O Id deve ser 1 ou 2 ou 3 ou etc; tente novamente!\n\n", 4294967295); // Solicita o ID do pet que deseja listar
    Pet p;
    fseek(arq, 0, SEEK_SET); // Move a posição do arquivo para o início (seek do in)
    while (fread(&p, sizeof(Pet), 1, arq) == 1) { // Lê uma estrutura Pet do arquivo
        if (id == p.id) { // Compara o ID do pet com o ID fornecido
            printf("%u %s %u mês(es) %s %s %s %s\n\n", p.id, p.nome, p.idade, p.especie, p.raca, p.cor, p.tutor); // Exibe os detalhes do pet se o ID corresponder
            return; // Retorna para encerrar a função após encontrar o pet desejado
        }
    }
    printf("Não existe pet cadastrado com este ID!\n\n"); // Exibe uma mensagem se o pet não for encontrado
}

void atualizar_pet(FILE* arq) {
    unsigned int id = numero_natural_digitado("Id: ", "O Id deve ser 1 ou 2 ou 3 ou etc; tente novamente!\n", 4294967295);
    Pet p;
    int encontrado = 0;

    fseek(arq, 0, SEEK_SET);
    while (fread(&p, sizeof(Pet), 1, arq) == 1) {
        if (id == p.id) {
            encontrado = 1;
            break;
        }
    }

    if (!encontrado) {
        printf("Não existe pet cadastrado com este ID!\n\n");
        return;
    }

    unsigned int subopcao;
    char atualizou=0/*falso*/;
    do {
        printf("0) Atualizar nome\n");
        printf("1) Atualizar idade\n");
        printf("2) Atualizar especie\n");
        printf("3) Atualizar raça\n");
        printf("4) Atualizar cor\n");
        printf("5) Atualizar tutor\n");
        printf("6) Encerrar Atualizações\n");
        subopcao=numero_natural_digitado ("Opção? ","Opções válidas estão entre 0 e 6; tente novamente!\n\n",6);

        if (subopcao == 0) {
            digite_texto(p.nome, 20, "Nome............: ", "O nome deve conter até 20 letras e/ou espaços em branco\n");
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        } else if (subopcao == 1) {
            p.idade = numero_natural_digitado("Idade (em meses): ", "A Idade deve ser 1 ou 2 ou 3 ou etc, até 480; tente novamente!\n", 480);
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        } else if (subopcao == 2) {
            digite_texto(p.especie, 30, "Especie.........: ", "A especie deve conter até 30 letras e/ou espaços em branco\n");
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        } else if (subopcao == 3) {
            digite_texto(p.raca, 30, "Raça............: ", "A raça deve conter até 30 letras e/ou espaços em branco\n");
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        } else if (subopcao == 4) {
            digite_texto(p.cor, 20, "Cor.............: ", "A cor deve conter até 20 letras e/ou espaços em branco\n");
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        } else if (subopcao == 5) {
            digite_texto(p.tutor, 40, "Tutor...........: ", "O nome do tutor deve conter até 40 letras e/ou espaços em branco\n");
            getc(stdin);
            atualizou=1/*verdadeiro*/;
        }
    } while (subopcao != 6);

    if (atualizou) {
        fseek(arq, -sizeof(Pet), SEEK_CUR);
        fwrite(&p, sizeof(Pet), 1, arq);
        printf("Alterações realizadas com sucesso!\n\n");
    }
}

void excluir_pet(FILE* arq, char loc [1025]) {
    unsigned int id = numero_natural_digitado("ID do pet a ser excluído: ", "O ID deve ser 1 ou 2 ou 3 ou etc; tente novamente!\n", 4294967295);
    Pet p;
    FILE* tempFile = fopen("temp.dat", "wb"); // Arquivo temporário para escrever pets não excluídos
    int excluido = 0; // Indica se o pet foi excluído

    fseek(arq, 0, SEEK_SET);
    unsigned int novoId = 1; // Novo ID a ser atribuído aos pets

    while (fread(&p, sizeof(Pet), 1, arq) == 1) {
        if (id == p.id) {
            excluido = 1; // Marca como excluído
        } else {
            p.id = novoId++; // Atribui um novo ID ao pet e incrementa o ID para o próximo pet
            fwrite(&p, sizeof(Pet), 1, tempFile); // Escreve o pet no arquivo temporário
        }
    }

    fclose(arq);
    fclose(tempFile);

    if (excluido) {
        remove(loc); // Remove o arquivo original
        rename("temp.dat", loc); // Renomeia o arquivo temporário para o original
        printf("Pet excluído com sucesso!\n\n");
    } else {
        remove("temp.dat"); // Se não foi excluído, remove o arquivo temporário
        printf("Não existe pet cadastrado com este ID!\n\n");
    }

    arq = fopen(file, "rb+"); // Abre o arquivo original novamente
}

int main()
{
    FILE* arquivo;
    char localizacaoDoArquivo [1025]; // dispositivo(c: ou d: etc)+caminho(\sistemas\petshop\dados\)+nome(bichinhos.dat)
    unsigned opcao;

    printf("PROGRAMA PARA GERENCIAR PETS\n\n");

    do
    {
        printf("Digite a loc do arquivo: ");
        fgets(localizacaoDoArquivo, 1024, stdin);
        localizacaoDoArquivo[strlen(localizacaoDoArquivo)-1]='\0';
        arquivo=fopen(localizacaoDoArquivo,"rb+");
        if (arquivo==NULL) // nao deu certo para abrir o arquivo para usar
        {
            arquivo=fopen(localizacaoDoArquivo,"wb+");
            if (arquivo==NULL) // nao deu certo para criar o arquivo
                printf("Foi impossível abrir o arquivo indicado! Tente novamente...\n");
            else
            {
                fclose(arquivo);
                arquivo=fopen(localizacaoDoArquivo,"rb+");
            }
        }
    }
    while (arquivo==NULL);

    do
    {
        printf("\n");
        printf("0) Cadastrar pet\n");
        printf("1) Listar    pet\n");
        printf("2) Listar    pets\n");
        printf("3) Atualizar pet\n");
        printf("4) Excluir   pet\n");
        printf("5) Sair\n");
        opcao=numero_natural_digitado ("Opção? ","Opções válidas estão entre 0 e 5; tente novamente!\n\n",5);

        switch (opcao)
        {
            case 0:
                cadastrar_pet(arquivo);
                break;

            case 1:
                listar_pet(arquivo);
                break;

            case 2:
                listar_pets(arquivo);
                break;

            case 3:
                atualizar_pet(arquivo);
                break;

            case 4:
                excluir_pet(arquivo, localizacaoDoArquivo);
                arquivo=fopen(localizacaoDoArquivo,"rb+");
                break;
        }
    }
    while (opcao!=5);

    fclose(arquivo);
    printf("OBRIGADO POR USAR ESTE PROGRAMA!\n\n");

    return 0;
}