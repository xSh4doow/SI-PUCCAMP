//
// Created by xsh4d on 18/09/2023.
//
#include <stdio.h>

typedef struct Filme
{
    unsigned int codigo;
    unsigned int duracao;
};

typedef struct Atuacao
{
    unsigned int codFilme;
    unsigned int codAtor;
};


unsigned int contadorAtuacao(struct Atuacao atuacao[], unsigned int numeroAtuacoes, unsigned int codFilme)
{
    unsigned int numAtores = 0;

    for (int i = 0; i < numeroAtuacoes; i++)
    {
        if (atuacao[i].codFilme == codFilme)
        {
            numAtores++;
        }
    }

    return numAtores;
}

unsigned int tempoTrabalhado (struct Filme filme[], unsigned int numeroFilmes, struct Atuacao atuacao[], unsigned int numeroAtuacao, unsigned int codAtor)
{
    unsigned int horas_trabalhadas = 0;

    for(int i = 0; i < numeroAtuacao; i++)
    {
        if (atuacao[i].codAtor == codAtor)
        {
            unsigned int codFilmeAt = atuacao[i].codFilme;

            for (int j = 0; j < numeroFilmes; j++)
            {
                if (filme[j].codigo == codFilmeAt)
                {
                    horas_trabalhadas += filme[j].duracao;
                }
            }
        }
    }

    return horas_trabalhadas;
}


int main() {
    struct Filme filmes[] = {
            {1, 120},
            {2, 90},
            {3, 150},
    };
    int numFilmes = sizeof(filmes) / sizeof(filmes[0]);

    struct Atuacao atuacoes[] = {
            {1, 101},
            {2, 101},
            {3, 102},
            {2, 103},
    };
    int numAtuacoes = sizeof(atuacoes) / sizeof(atuacoes[0]);

    unsigned int codigoAtor = 101;

    unsigned int tempoTotalAtuado = tempoTrabalhado(filmes, numFilmes, atuacoes, numAtuacoes, codigoAtor);

    printf("O ator com código %u atuou por %d minutos em todos os filmes.\n", codigoAtor, tempoTotalAtuado);

    return 0;
}