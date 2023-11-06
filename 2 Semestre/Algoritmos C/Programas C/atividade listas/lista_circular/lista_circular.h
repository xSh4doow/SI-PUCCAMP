#ifndef LISTA_CIR
#define LISTA_CIR

typedef enum {
    false,
    true
} boolean;

typedef void* Elemento_de_lista_cir;

typedef struct Struct_do_no_de_lista_cir {
    Elemento_de_lista_cir informacao;
    struct Struct_do_no_de_lista_cir* proximo;
} Struct_do_no_de_lista_cir;

typedef Struct_do_no_de_lista_cir* Ptr_de_no_de_lista_cir;

typedef struct
{
    Ptr_de_no_de_lista_cir primeiro;
} Lista_cir;

void nova_lista_cir(Lista_cir* lc);
void insira_no_inicio_da_lista_cir(Lista_cir* l, Elemento_de_lista_cir i);
void insira_no_final_da_lista_cir(Lista_cir* l, Elemento_de_lista_cir i);
boolean recupere_elemento_do_inicio(Lista_cir l, Elemento_de_lista_cir* i);
boolean recupere_elemento_do_final(Lista_cir l, Elemento_de_lista_cir* i);
boolean remova_elemento_do_inicio(Lista_cir* l);
boolean remova_elemento_do_final(Lista_cir* l);
boolean lista_cir_vazia(Lista_cir l);
boolean free_lista_cir(Lista_cir* l);

#endif
