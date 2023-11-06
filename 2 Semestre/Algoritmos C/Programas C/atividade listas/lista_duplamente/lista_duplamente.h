#ifndef LISTA_DUPLA
#define LISTA_DUPLA

typedef enum {
    false,
    true
} boolean;

typedef void* Elemento_de_lista_dupla;

typedef struct Struct_do_no_de_lista_dupla {
    Elemento_de_lista_dupla informacao;
    struct Struct_do_no_de_lista_dupla* proximo;
    struct Struct_do_no_de_lista_dupla* anterior;
} Struct_do_no_de_lista_dupla;

typedef Struct_do_no_de_lista_dupla* Ptr_de_no_de_lista_dupla;

typedef struct
{
    Ptr_de_no_de_lista_dupla primeiro;
    Ptr_de_no_de_lista_dupla ultimo;
} Lista_duplamente_ligada;

void nova_lista_dupla(Lista_duplamente_ligada* lc);
void insira_no_inicio_da_lista_dupla(Lista_duplamente_ligada* l, Elemento_de_lista_dupla i);
void insira_no_final_da_lista_dupla(Lista_duplamente_ligada* l, Elemento_de_lista_dupla i);
boolean recupere_elemento_do_inicio(Lista_duplamente_ligada l, Elemento_de_lista_dupla* i);
boolean recupere_elemento_do_final(Lista_duplamente_ligada l, Elemento_de_lista_dupla* i);
boolean remova_elemento_do_inicio(Lista_duplamente_ligada* l);
boolean remova_elemento_do_final(Lista_duplamente_ligada* l);
boolean lista_dupla_vazia(Lista_duplamente_ligada l);
boolean free_lista_dupla(Lista_duplamente_ligada* l);

#endif
