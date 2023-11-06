#include <stdlib.h>
#include "lista_cir_dup.h"

void nova_lista_cir_dupla(Lista_cir_dupla* lc)
{
    lc->primeiro = NULL;
    lc->ultimo = NULL;
}

static Ptr_de_no_de_lista_cir_dup novo_no_de_lista_cir_dup(Elemento_de_lista_cir_dup i, Ptr_de_no_de_lista_cir_dup p, Ptr_de_no_de_lista_cir_dup a)
{
    Ptr_de_no_de_lista_cir_dup novo = (Ptr_de_no_de_lista_cir_dup)malloc(sizeof(Struct_do_no_de_lista_cir_dup));

    novo->informacao = i;
    novo->proximo = p;
    novo->anterior = a;

    return novo;
}

void insira_no_inicio_da_lista_cir_dupla(Lista_cir_dupla* l, Elemento_de_lista_cir_dup i)
{
    if (l->primeiro == NULL) // Lista vazia
    {
        l->primeiro = novo_no_de_lista_cir_dup(i, NULL, NULL);
        l->primeiro->proximo = l->primeiro;
        l->primeiro->anterior = l->primeiro;
        l->ultimo = l->primeiro;
    }
    else
    {
        Ptr_de_no_de_lista_cir_dup novo = novo_no_de_lista_cir_dup(i, l->primeiro, l->ultimo);
        l->primeiro->anterior = novo;
        l->ultimo->proximo = novo;
        l->primeiro = novo;
    }
}

void insira_no_final_da_lista_cir_dupla(Lista_cir_dupla* l, Elemento_de_lista_cir_dup i)
{
    if (l->primeiro == NULL) // Lista vazia
    {
        insira_no_inicio_da_lista_cir_dupla(l, i);
    }
    else
    {
        Ptr_de_no_de_lista_cir_dup novo = novo_no_de_lista_cir_dup(i, l->primeiro, l->ultimo);
        l->primeiro->anterior = novo;
        l->ultimo->proximo = novo;
        l->ultimo = novo;
    }
}

boolean recupere_elemento_do_inicio(Lista_cir_dupla l, Elemento_de_lista_cir_dup* i)
{
    if (l.primeiro == NULL)
        return false;

    *i = l.primeiro->informacao;
    return true;
}

boolean recupere_elemento_do_final(Lista_cir_dupla l, Elemento_de_lista_cir_dup* i)
{
    if (l.ultimo == NULL)
        return false;

    *i = l.ultimo->informacao;
    return true;
}

boolean remova_elemento_do_inicio(Lista_cir_dupla* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir_dup antigo_primeiro = l->primeiro;
    l->primeiro = l->primeiro->proximo;
    l->primeiro->anterior = l->ultimo;
    l->ultimo->proximo = l->primeiro;

    free(antigo_primeiro->informacao);
    free(antigo_primeiro);

    if (l->primeiro == l->ultimo)
    {
        // Único nó restante na lista
        free(l->primeiro);
        l->primeiro = l->ultimo = NULL;
    }

    return true;
}

boolean remova_elemento_do_final(Lista_cir_dupla* l)
{
    if (l->primeiro == NULL)
        return false;

    if (l->primeiro->proximo == l->primeiro)
    {
        // Único nó na lista
        free(l->primeiro->informacao);
        free(l->primeiro);
        l->primeiro = l->ultimo = NULL;
        return true;
    }

    Ptr_de_no_de_lista_cir_dup antigo_ultimo = l->ultimo;
    l->ultimo = l->ultimo->anterior;
    l->ultimo->proximo = l->primeiro;
    l->primeiro->anterior = l->ultimo;

    free(antigo_ultimo->informacao);
    free(antigo_ultimo);

    return true;
}

boolean lista_cir_dupla_vazia(Lista_cir_dupla l)
{
    return l.primeiro == NULL;
}

boolean free_lista_cir_dupla(Lista_cir_dupla* l)
{
    if (l->primeiro == NULL)
        return false;

    Ptr_de_no_de_lista_cir_dup atual = l->primeiro;

    while (atual != l->ultimo)
    {
        l->primeiro = l->primeiro->proximo;
        free(atual->informacao);
        free(atual);
        atual = l->primeiro;
    }

    free(l->primeiro->informacao);
    free(l->primeiro);
    l->ultimo = NULL;
    return true;
}
