#include <stdlib.h>
#include "lista_duplamente.h"

void nova_lista_dupla (Lista_dupla* ld)
{
    ld->primeiro = NULL;
    ld->ultimo = NULL;
}

static Ptr_de_no_de_lista_dupla novo_no_de_lista_dupla(Elemento_de_lista_simples i, Ptr_de_no_de_lista_dupla p, Ptr_de_no_de_lista_dupla a)
{
    Ptr_de_no_de_lista_dupla novo = (Ptr_de_no_de_lista_dupla)malloc(sizeof(Struct_do_no_de_lista_dupla));

    novo->informacao = i;
    novo->proximo = p;
    novo->anterior = a;

    return novo;
}

void insira_no_inicio_da_lista_dupla(Lista_dupla* l, Elemento_de_lista_simples i)
{
    l->primeiro = novo_no_de_lista_dupla(i, l->primeiro, NULL);
    if (l->primeiro == NULL)
    {
        l->ultimo = l->primeiro;
    }
    else
    {
        l->primeiro->proximo->anterior = l->primeiro;
    }
}

void insira_no_final_da_lista_dupla(Lista_dupla* l, Elemento_de_lista_simples i)
{
    if (l->ultimo == NULL)
    {
        insira_no_inicio_da_lista_dupla(l, i);
    }
    else
    {
        l->ultimo->proximo = novo_no_de_lista_dupla(i, NULL, l->ultimo);
        l->ultimo = l->ultimo->proximo;
    }
}

boolean remova_elemento_do_inicio_da_lista_dupla(Lista_dupla* l)
{
    if (l->primeiro == NULL)
    {
        return false;
    }

    Ptr_de_no_de_lista_dupla antigo_primeiro = l->primeiro;

    if (l->primeiro->proximo != NULL)
    {
        l->primeiro = l->primeiro->proximo;
        l->primeiro->anterior = NULL;
    }
    else
    {
        l->primeiro = l->ultimo = NULL;
    }

    free(antigo_primeiro->informacao);
    free(antigo_primeiro);

    return true;
}

boolean remova_elemento_do_final_da_lista_dupla(Lista_dupla* l)
{
    if (l->primeiro == NULL)
    {
        return false;
    }

    if (l->primeiro->proximo == NULL)
    {
        free(l->primeiro->informacao);
        free(l->primeiro);
        l->primeiro = l->ultimo = NULL;
        return true;
    }

    Ptr_de_no_de_lista_dupla penultimo = l->ultimo->anterior;

    free(l->ultimo->informacao);
    free(l->ultimo);

    penultimo->proximo = NULL;
    l->ultimo = penultimo;

    return true;
}

boolean recupere_elemento_do_inicio_da_lista_dupla(Lista_dupla l, Elemento_de_lista_simples* i)
{
    if (l.primeiro == NULL)
    {
        return false;
    }

    *i = l.primeiro->informacao;
    return true;
}

boolean recupere_elemento_do_final_da_lista_dupla(Lista_dupla l, Elemento_de_lista_simples* i)
{
    if (l.ultimo == NULL)
    {
        return false;
    }

    *i = l.ultimo->informacao;
    return true;
}

boolean lista_dupla_vazia(Lista_dupla l)
{
    return l.primeiro == NULL;
}

boolean free_lista_dupla(Lista_dupla* l)
{
    if (l->primeiro == NULL)
    {
        return false;
    }

    Ptr_de_no_de_lista_dupla atual = l->primeiro;

    while (atual != NULL)
    {
        l->primeiro = l->primeiro->proximo;
        free(atual->informacao);
        free(atual);
        atual = l->primeiro;
    }

    l->ultimo = NULL;
    return true;
}
