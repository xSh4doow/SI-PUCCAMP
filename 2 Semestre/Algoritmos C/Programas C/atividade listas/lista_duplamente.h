#ifndef LISTA_DUPLAMENTE
#define LISTA_DUPLAMENTE

typedef enum {
    false,
    true
} boolean;

typedef void* Elemento_de_lista_simples;

typedef struct Struct_do_no_de_lista_dupla {
    Elemento_de_lista_simples informacao;
    struct Struct_do_no_de_lista_dupla* proximo;
    struct Struct_do_no_de_lista_dupla* anterior;
} Struct_do_no_de_lista_dupla;

typedef Struct_do_no_de_lista_dupla* Ptr_de_no_de_lista_dupla;

typedef struct
{
    Ptr_de_no_de_lista_dupla primeiro, ultimo;
} Lista_dupla;

void nova_lista_dupla(Lista_dupla* ld);
void insira_no_inicio_da_lista_dupla(Lista_dupla* l, Elemento_de_lista_simples i);
void insira_no_final_da_lista_dupla(Lista_dupla* l, Elemento_de_lista_simples i);
boolean remova_elemento_do_inicio_da_lista_dupla(Lista_dupla* l);
boolean remova_elemento_do_final_da_lista_dupla(Lista_dupla* l);
boolean recupere_elemento_do_inicio_da_lista_dupla(Lista_dupla l, Elemento_de_lista_simples* i);
boolean recupere_elemento_do_final_da_lista_dupla(Lista_dupla l, Elemento_de_lista_simples* i);
boolean lista_dupla_vazia(Lista_dupla l);
boolean free_lista_dupla(Lista_dupla* l);

#endif
