#ifndef LISTA_CIR_DUPLA
#define LISTA_CIR_DUPLA

typedef enum {
    false,
    true
} boolean;

typedef void* Elemento_de_lista_cir_dup;

typedef struct Struct_do_no_de_lista_cir_dup {
    Elemento_de_lista_cir_dup informacao;
    struct Struct_do_no_de_lista_cir_dup* proximo;
    struct Struct_do_no_de_lista_cir_dup* anterior;
} Struct_do_no_de_lista_cir_dup;

typedef Struct_do_no_de_lista_cir_dup* Ptr_de_no_de_lista_cir_dup;

typedef struct
{
    Ptr_de_no_de_lista_cir_dup primeiro;
    Ptr_de_no_de_lista_cir_dup ultimo;
} Lista_cir_dupla;

void nova_lista_cir_dupla(Lista_cir_dupla* lc);
void insira_no_inicio_da_lista_cir_dupla(Lista_cir_dupla* l, Elemento_de_lista_cir_dup i);
void insira_no_final_da_lista_cir_dupla(Lista_cir_dupla* l, Elemento_de_lista_cir_dup i);
boolean recupere_elemento_do_inicio(Lista_cir_dupla l, Elemento_de_lista_cir_dup* i);
boolean recupere_elemento_do_final(Lista_cir_dupla l, Elemento_de_lista_cir_dup* i);
boolean remova_elemento_do_inicio(Lista_cir_dupla* l);
boolean remova_elemento_do_final(Lista_cir_dupla* l);
boolean lista_cir_dupla_vazia(Lista_cir_dupla l);
boolean free_lista_cir_dupla(Lista_cir_dupla* l);

#endif
