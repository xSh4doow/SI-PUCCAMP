#include <stdlib.h>
#include "lista_circular.h"

void nova_lista_circular(Lista_circular* lc)
{
    lc->primeiro = NULL;
}

static Ptr_de_no_de_lista_circular novo_no_de_lista_circular(Elemento_de_lista_circular i, Ptr_de_no_de_lista_circular p)
{
    Ptr_de_no_de_lista_circular novo = (Ptr_de_no_de_lista_circular)malloc(sizeof(Struct_do_no_de_lista_circular));

    novo->informacao = i;
    novo->proximo = p;

    return novo;
}

void insira_no_inicio_da_lista_circular(Lista_circular* l, Elemento_de_lista_circular i)
{
    Ptr_de_no_de_lista_circular novo = novo_no_de_lista_circular(i, l->primeiro);

    if (l->primeiro == NULL)
    {
        novo->proximo = novo;
    }
    else
    {
        Ptr_de_no_de_lista_circular atual = l->primeiro;
        while (atual->proximo != l->primeiro)
        {
            atual = atual->proximo;
        }
        atual->proximo = novo;
    }

    l->primeiro = novo;
}

void insira_no_final_da_lista_circular(Lista_circular* l, Elemento_de_lista_circular i)
{
    insira_no_inicio_da_lista_circular(l, i);
    l->primeiro = l->primeiro->proximo;
}

boolean recupere_elemento_do_final(Lista_circular l, Elemento_de_lista_circular* i)
{
    if (l.primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_circular atual = l.primeiro;
    Ptr_de_no_de_lista_circular anterior = NULL;

    while (atual->proximo != l.primeiro)
    {
        anterior = atual;
        atual = atual->proximo;
    }

    *i = atual->informacao;

    return true;
}

boolean remova_elemento_do_final(Lista_circular* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_circular atual = l->primeiro;
    Ptr_de_no_de_lista_circular anterior = NULL;

    while (atual->proximo != l->primeiro)
    {
        anterior = atual;
        atual = atual->proximo;
    }

    if (anterior == NULL)
    {
        free(atual->informacao);
        free(atual);
        l->primeiro = NULL;
    }
    else
    {
        anterior->proximo = l->primeiro;
        free(atual->informacao);
        free(atual);
    }

    return true;
}

boolean lista_circular_vazia(Lista_circular l)
{
    return l.primeiro == NULL;
}

boolean free_lista_circular(Lista_circular* l) {
    if (l->primeiro == NULL) {
        return false;
    }

    Ptr_de_no_de_lista_circular atual = l->primeiro;
    Ptr_de_no_de_lista_circular proximo = NULL;

    do {
        proximo = atual->proximo;
        free(atual->informacao);
        free(atual);
        atual = proximo;
    } while (atual != l->primeiro);

    l->primeiro = NULL;
    return true;

}