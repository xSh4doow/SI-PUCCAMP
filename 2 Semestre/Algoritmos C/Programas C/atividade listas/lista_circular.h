#ifndef LISTA_CIRCULAR
#define LISTA_CIRCULAR

typedef enum {
    false,
    true
} boolean;

typedef void* Elemento_de_lista_circular;

typedef struct Struct_do_no_de_lista_circular {
    Elemento_de_lista_circular informacao;
    struct Struct_do_no_de_lista_circular* proximo;
} Struct_do_no_de_lista_circular;

typedef Struct_do_no_de_lista_circular* Ptr_de_no_de_lista_circular;

typedef struct
{
    Ptr_de_no_de_lista_circular primeiro;
} Lista_circular;

void nova_lista_circular(Lista_circular* lc);
void insira_no_inicio_da_lista_circular(Lista_circular* l, Elemento_de_lista_circular i);
void insira_no_final_da_lista_circular(Lista_circular* l, Elemento_de_lista_circular i);
boolean recupere_elemento_do_final(Lista_circular l, Elemento_de_lista_circular* i);
boolean remova_elemento_do_final(Lista_circular* l);
boolean lista_circular_vazia(Lista_circular l);
boolean free_lista_circular(Lista_circular* l);

#endif
