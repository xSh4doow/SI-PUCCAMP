#include <stdlib.h>
#include "lista_duplamente.h"

void nova_lista_dupla(Lista_duplamente_ligada* lc)
{
    lc->primeiro = NULL;
    lc->ultimo = NULL;
}

static Ptr_de_no_de_lista_dupla novo_no_de_lista_dupla(Elemento_de_lista_dupla i, Ptr_de_no_de_lista_dupla p, Ptr_de_no_de_lista_dupla a)
{
    Ptr_de_no_de_lista_dupla novo = (Ptr_de_no_de_lista_dupla)malloc(sizeof(Struct_do_no_de_lista_dupla));

    novo->informacao = i;
    novo->proximo = p;
    novo->anterior = a;

    return novo;
}

void insira_no_inicio_da_lista_dupla(Lista_duplamente_ligada* l, Elemento_de_lista_dupla i)
{
    if (l->primeiro == NULL) // Lista vazia
    {
        l->primeiro = novo_no_de_lista_dupla(i, NULL, NULL);
        l->ultimo = l->primeiro;
    }
    else
    {
        Ptr_de_no_de_lista_dupla novo = novo_no_de_lista_dupla(i, l->primeiro, NULL);
        l->primeiro->anterior = novo;
        l->primeiro = novo;
    }
}

void insira_no_final_da_lista_dupla(Lista_duplamente_ligada* l, Elemento_de_lista_dupla i)
{
    if (l->primeiro == NULL) // Lista vazia
    {
        insira_no_inicio_da_lista_dupla(l, i);
    }
    else
    {
        Ptr_de_no_de_lista_dupla novo = novo_no_de_lista_dupla(i, NULL, l->ultimo);
        l->ultimo->proximo = novo;
        l->ultimo = novo;
    }
}

boolean recupere_elemento_do_inicio(Lista_duplamente_ligada l, Elemento_de_lista_dupla* i)
{
    if (l.primeiro == NULL)
        return false;

    *i = l.primeiro->informacao;
    return true;
}

boolean recupere_elemento_do_final(Lista_duplamente_ligada l, Elemento_de_lista_dupla* i)
{
    if (l.ultimo == NULL)
        return false;

    *i = l.ultimo->informacao;
    return true;
}

boolean remova_elemento_do_inicio(Lista_duplamente_ligada* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_dupla antigo_primeiro = l->primeiro;
    l->primeiro = l->primeiro->proximo;

    if (l->primeiro != NULL)
        l->primeiro->anterior = NULL;
    else
        l->ultimo = NULL;

    free(antigo_primeiro->informacao);
    free(antigo_primeiro);

    return true;
}

boolean remova_elemento_do_final(Lista_duplamente_ligada* l)
{
    if (l->ultimo == NULL)
        return false;

    Ptr_de_no_de_lista_dupla antigo_ultimo = l->ultimo;
    l->ultimo = l->ultimo->anterior;

    if (l->ultimo != NULL)
        l->ultimo->proximo = NULL;
    else
        l->primeiro = NULL;

    free(antigo_ultimo->informacao);
    free(antigo_ultimo);

    return true;
}

boolean lista_dupla_vazia(Lista_duplamente_ligada l)
{
    return l.primeiro == NULL;
}

boolean free_lista_dupla(Lista_duplamente_ligada* l)
{
    if (l->primeiro == NULL)
        return false;

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
