#include <stdio.h>
#include<stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct 
{
    char* nombre;
    int dia,mes,anio;

    
}Cumpleanio;
#define NUMCUM 3

void limpiar_buffer(void);
void busqueda_cumple(Cumpleanio cumples[], int dia,int mes);
void main(void){
    Cumpleanio c1,c2,c3,c4,c5;
    Cumpleanio cumples[5]={c1,c2,c3,c4,c5};

    /* for(int j=0;j<5;j++){
        cumples[j]=malloc(sizeof(Cumpleanio)*5);
        } */

    printf("Ingrese los cumpleaños de  personas junto con su nombre\n");
    int i=0;
    while(i<NUMCUM){
        printf("Ingrese un nombre\n");
        char nom[30];
        fgets(nom,sizeof(char)*30,stdin);
        for(int k=0;nom[k]!='\0';k++){
            if(nom[k]=='\n'){
                nom[k]='\0';
            }
        }
        cumples[i].nombre=malloc(sizeof(char)*(strlen(nom)+1));
        strcpy(cumples[i].nombre,nom);
        
        

        printf("Ingrese la fecha de nacimiento\n");
        scanf("%d %d %d",&(cumples[i].dia),&(cumples[i].mes),&(cumples[i].anio));
        
        limpiar_buffer();

        i++;
    }
    int dia,mes;
    printf("Ingrese una fecha para ver a quien pertenece: \n");
    scanf("%d %d",&dia,&mes);
    busqueda_cumple(cumples,dia,mes);
    for(int j=0;j<NUMCUM;j++){
        free(cumples[j].nombre);
    }
} 


void limpiar_buffer(void){
    char c;
    while((c=getchar())!='\n');
}
/* se entiende cada int por dia mes y anio
busqueda_cumple:Cumpleanio cumples[], int,int, int -> void
Toma una lista de cumpleaños y busca el nombre del cumpleañero, en el caso que no haya niguno lo imprimira en pantalla, 
si hay mas de uno, imprimira los nombres de los cumpleañeros*/
void busqueda_cumple(Cumpleanio cumples[], int dia,int mes){

    Cumpleanio lista_cumple[5];
    int j=0;
    for(int i=0;i<5;i++){
        if(cumples[i].dia==dia&&cumples[i].mes==mes){
            lista_cumple[j]=cumples[i];
            j++;
        } 

    }

    if(j==0){
        printf("No se encontraron cumpleaños en esta fecha\n");

    }
    else if(j==1){

        printf("%s cumple en esa fecha!!!\n",lista_cumple[0].nombre);
        
    }
    else{
        printf("Las personas que cumplen en esa fecha son: \n");
        printf("%d",j);
        for(int i=0;i<j;i++){
            printf("%s,",lista_cumple[i].nombre);
        }
        printf("\n");

    }
}