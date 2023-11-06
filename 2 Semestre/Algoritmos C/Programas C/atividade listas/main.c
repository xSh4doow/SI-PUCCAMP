#include <stdio.h>
#include <stdlib.h>
#include "lista_cir_dup.h"

int main() {
    Lista_cir_dupla lista;
    nova_lista_cir_dupla(&lista);

    int *elemento = (int *)malloc(sizeof(int));
    *elemento = 2;
    insira_no_inicio_da_lista_cir_dupla(&lista, (Elemento_de_lista_cir_dup)elemento);

    elemento = (int *)malloc(sizeof(int));
    *elemento = 3;
    insira_no_inicio_da_lista_cir_dupla(&lista, (Elemento_de_lista_cir_dup)elemento);

    elemento = (int *)malloc(sizeof(int));
    *elemento = 5;
    insira_no_inicio_da_lista_cir_dupla(&lista, (Elemento_de_lista_cir_dup)elemento);

    Elemento_de_lista_cir_dup elemento_recuperado;
    if (recupere_elemento_do_inicio(lista, &elemento_recuperado)) {
        printf("Elemento do início: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    remova_elemento_do_inicio(&lista);

    if (recupere_elemento_do_final(lista, &elemento_recuperado)) {
        printf("Elemento do final: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    remova_elemento_do_final(&lista);

    if (lista_cir_dupla_vazia(lista)) {
        printf("A lista está vazia\n");
    } else {
        printf("A lista não está vazia\n");
    }

    free_lista_cir_dupla(&lista);

    return 0;
}
