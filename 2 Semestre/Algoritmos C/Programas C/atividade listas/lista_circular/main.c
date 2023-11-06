#include <stdio.h>
#include <stdlib.h>
#include "lista_circular.h"

int main() {
    Lista_cir lista;
    nova_lista_cir(&lista);

    int *elemento = (int *)malloc(sizeof(int));
    *elemento = 2;
    insira_no_inicio_da_lista_cir(&lista, (Elemento_de_lista_cir)elemento);

    elemento = (int *)malloc(sizeof(int));
    *elemento = 3;
    insira_no_inicio_da_lista_cir(&lista, (Elemento_de_lista_cir)elemento);

    elemento = (int *)malloc(sizeof(int));
    *elemento = 5;
    insira_no_inicio_da_lista_cir(&lista, (Elemento_de_lista_cir)elemento);

    elemento = (int *)malloc(sizeof(int));
    *elemento = 7;
    insira_no_final_da_lista_cir(&lista, (Elemento_de_lista_cir)elemento);

    Elemento_de_lista_cir elemento_recuperado;
    if (recupere_elemento_do_inicio(lista, &elemento_recuperado)) {
        printf("Elemento do início: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    remova_elemento_do_inicio(&lista);

    if (recupere_elemento_do_inicio(lista, &elemento_recuperado)) {
        printf("Elemento do início: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    if (recupere_elemento_do_final(lista, &elemento_recuperado)) {
        printf("Elemento do final: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    remova_elemento_do_final(&lista);

    if (recupere_elemento_do_final(lista, &elemento_recuperado)) {
        printf("Elemento do final: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    elemento = (int *)malloc(sizeof(int));
    *elemento = 11;
    insira_no_final_da_lista_cir(&lista, (Elemento_de_lista_cir)elemento);

    if (recupere_elemento_do_final(lista, &elemento_recuperado)) {
        printf("Elemento do final: %d\n", *((int *)elemento_recuperado));
    } else {
        printf("Lista vazia\n");
    }

    if (lista_cir_vazia(lista)) {
        printf("A lista está vazia\n");
    } else {
        printf("A lista não está vazia\n");
    }

    free_lista_cir(&lista);

    return 0;
}