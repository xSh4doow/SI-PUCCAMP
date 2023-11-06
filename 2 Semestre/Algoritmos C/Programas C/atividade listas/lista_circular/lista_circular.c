#include <stdlib.h>
#include "lista_circular.h"

void nova_lista_cir(Lista_cir* lc)
{
    lc->primeiro = NULL;
}

static Ptr_de_no_de_lista_cir novo_no_de_lista_cir(Elemento_de_lista_cir i, Ptr_de_no_de_lista_cir p)
{
    Ptr_de_no_de_lista_cir novo = (Ptr_de_no_de_lista_cir)malloc(sizeof(Struct_do_no_de_lista_cir));
    novo->informacao = i;
    novo->proximo = p;
    return novo;
}

void insira_no_inicio_da_lista_cir(Lista_cir* l, Elemento_de_lista_cir i)
{
    if (l->primeiro == NULL)
    {
        l->primeiro = novo_no_de_lista_cir(i, NULL);
        l->primeiro->proximo = l->primeiro; // Faz a lista apontar para si mesma.
    }
    else
    {
        Ptr_de_no_de_lista_cir novo = novo_no_de_lista_cir(i, l->primeiro);
        Ptr_de_no_de_lista_cir ultimo = l->primeiro;
        while (ultimo->proximo != l->primeiro)
        {
            ultimo = ultimo->proximo;
        }
        ultimo->proximo = novo;
        l->primeiro = novo;
    }
}

void insira_no_final_da_lista_cir(Lista_cir* l, Elemento_de_lista_cir i)
{
    if (l->primeiro == NULL)
    {
        insira_no_inicio_da_lista_cir(l, i);
    }
    else
    {
        Ptr_de_no_de_lista_cir novo = novo_no_de_lista_cir(i, l->primeiro);
        Ptr_de_no_de_lista_cir ultimo = l->primeiro;
        while (ultimo->proximo != l->primeiro)
        {
            ultimo = ultimo->proximo;
        }
        ultimo->proximo = novo;
    }
}

boolean recupere_elemento_do_inicio(Lista_cir l, Elemento_de_lista_cir* i)
{
    if (l.primeiro == NULL)
        return false;

    *i = l.primeiro->informacao;
    return true;
}

boolean recupere_elemento_do_final(Lista_cir l, Elemento_de_lista_cir* i)
{
    if (l.primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir ultimo = l.primeiro;
    while (ultimo->proximo != l.primeiro)
    {
        ultimo = ultimo->proximo;
    }
    *i = ultimo->informacao;
    return true;
}

boolean remova_elemento_do_inicio(Lista_cir* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir antigo_primeiro = l->primeiro;
    Ptr_de_no_de_lista_cir ultimo = l->primeiro;
    while (ultimo->proximo != l->primeiro)
    {
        ultimo = ultimo->proximo;
    }
    l->primeiro = l->primeiro->proximo;
    ultimo->proximo = l->primeiro;

    free(antigo_primeiro->informacao);
    free(antigo_primeiro);

    if (l->primeiro == antigo_primeiro)
    {
        // Único nó restante na lista
        free(l->primeiro);
        l->primeiro = NULL;
    }

    return true;
}

boolean remova_elemento_do_final(Lista_cir* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir antigo_ultimo = l->primeiro;
    Ptr_de_no_de_lista_cir ultimo = l->primeiro;
    Ptr_de_no_de_lista_cir penultimo = NULL;
    while (ultimo->proximo != l->primeiro)
    {
        penultimo = ultimo;
        ultimo = ultimo->proximo;
    }
    if (penultimo == NULL)
    {
        // Único nó na lista
        free(l->primeiro->informacao);
        free(l->primeiro);
        l->primeiro = NULL;
    }
    else
    {
        penultimo->proximo = l->primeiro;
        free(ultimo->informacao);
        free(ultimo);
    }

    return true;
}

boolean lista_cir_vazia(Lista_cir l)
{
    return l.primeiro == NULL;
}

boolean free_lista_cir(Lista_cir* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir atual = l->primeiro;
    Ptr_de_no_de_lista_cir proximo = l->primeiro->proximo;

    while (proximo != l->primeiro)
    {
        free(atual->informacao);
        free(atual);
        atual = proximo;
        proximo = proximo->proximo;
    }

    free(atual->informacao);
    free(atual);
    l->primeiro = NULL;

    return true;
}
