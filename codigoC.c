// codigoC.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int soma(int a, int b) {
    return a + b;
}

float multiplica(float a, float b){
	return a*b;
}

char* obter_mensagem() {
    char* mensagem = (char*)malloc(13 * sizeof(char));
    strcpy(mensagem, "String do C!");
    return mensagem;
}

void libera_memoria(char* ponteiro) {
    free(ponteiro);
}
