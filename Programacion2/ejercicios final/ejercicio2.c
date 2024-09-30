#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/*
Las letras cuestan,cada una 10 pesos
Los digitos tienen un valor de 20 cada uno
Los caracteres especiales cuestan 30 y los espacios en blamco no tienen valor
*/

void limpiar_buffer(void);
int isspecial(int c);
int costo(char arr[]);
void main(void){

    int lonmensaje;
    printf("Escriba la longitud del mesaje y el mensaje: ");
    scanf("%d",&lonmensaje);
    limpiar_buffer();
    char* mensaje;
    mensaje=(char*)malloc(sizeof(char)*lonmensaje+1);
    fgets(mensaje,sizeof(char)*lonmensaje,stdin);

    int cos=costo(mensaje);
    printf("El costo del mensaje es: %d\n",cos);

    free(mensaje);
}

void limpiar_buffer(void){
    int c;
    while((c=getchar())!='\n');
}

int costo(char arr[]){
    
    int total=0;
    for(int i=0;arr[i]!='\0';i++){

        if(isspecial(arr[i])){
            total+=30;
        }
        else if(isalpha(arr[i])){
            total+=10;
        }
        else if(isdigit(arr[i])){
            total+=20;
        }
    }

    return total;
}

int isspecial(int c){
    return !isspace(c) &&!isalnum(c);
}