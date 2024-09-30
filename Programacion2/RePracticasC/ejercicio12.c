#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*Ejercicio 12. Cree una representación para una agenda de contactos:

e) Escriba un programa que permita:
i. Dar de alta un contacto: void alta_contacto(struct Agenda *); pide por teclado
los datos del contacto a agregar (función crear_contacto) e inserta el resultado en
la agenda.
ii. Modificar la edad de un contacto: void modificar_edad(struct Agenda *); pide
por teclado el nombre del contacto a modificar para identificarlo y luego actualiza su
edad (función actualizar_edad).
iii. Ver los datos de los contactos cargados: void imprimir_contactos(struct Agenda
*);.
f) Implemente una función double prom(struct Agenda *); que devuelva el promedio de
la edad de los contactos dentro de la agenda*/


/*a) Defina una estructura Contacto que tenga como campos: una cadena para el nombre de
una persona, una cadena para el número de teléfono y un entero sin signo para llevar la
edad de la persona.*/


typedef struct {
    char* nombre;
    char* telefono;
    unsigned int edad;
}Contacto;
/*d) Defina una estructura Agenda que almacene un arreglo de estructuras Contacto y un
entero para llevar la cantidad de estructuras completadas del arreglo.*/
typedef struct{
    Contacto contactos[100];
    int completas; //número de contactos con toda la informaciòn;
}Agenda;


//-----------------------------------------------------------//

void actualizar_edad(Contacto *c);
Contacto crear_contacto(void);
void sacar_salto(char str[]);
void alta_contacto(Agenda* p);
void modificar_edad(Agenda* agen);
void imprimir_contactos(Agenda* agenda);
void limpiar_buffer();
//----------------------------------------------------------//
void main(void){

    Agenda Amigos;
    Amigos.completas=0;

    printf("Agrega un nuevo contacto\n");
    char c='s';
    
    while(c!='n'){
        alta_contacto(&Amigos);
        printf("Quiere agregar un contacto nuevo?s/n\n");
        limpiar_buffer();
        c=getchar();
        limpiar_buffer();
        
    }
    imprimir_contactos(&Amigos);

    printf("Desea modificar la edad de algun contacto?s/n\n");

    c=getchar();
    if (c=='s')
    {   
        limpiar_buffer();
        modificar_edad(&Amigos);
        imprimir_contactos(&Amigos);
    }

    

    for(int i=0;i<Amigos.completas;i++){
        free(Amigos.contactos[i].nombre);
        free(Amigos.contactos[i].telefono);
    }




}

/*b) Implemente una función struct Contacto crear_contacto() que pida por teclado los
datos pertinentes, rellene una estructura Contacto y la devuelva.*/

/*crear_contacto: Void -> Contacto
Pide datos por teclado para crear una estructura Contacto y la devuelve*/
Contacto crear_contacto(){
    Contacto c;
    char nom[30];
    char tel[30];
    unsigned int edad;

    printf("Ingrese nombre:\n");
    fgets(nom,sizeof(char)*30,stdin);
    sacar_salto(nom);
    c.nombre=malloc(sizeof(char)*strlen(nom)+1);
    strcpy(c.nombre,nom);


    printf("Ingrese telefono:\n");
    fgets(tel,sizeof(char)*30,stdin);
    sacar_salto(tel);
    c.telefono=malloc(sizeof(char)*strlen(nom)+1);
    strcpy(c.telefono,tel);

    printf("Ingrese edad:\n");
    scanf("%d",&edad);
    c.edad=edad;

    return c;

}

void sacar_salto(char str[]){
    for(int i=0;str[i]!='\0';i++){
        if(str[i]=='\n'){
            str[i]=='\0';
        }
    }
}

/*c) Implemente una función void actualizar_edad(struct Contacto *) que, dado un pun-
tero a una estructura Contacto, pida una nueva edad por teclado y actualice la estructura.*/

/*actualizar_edad():Contacto* -> void
Dado un puntero de una estructura contacto, pide por teclado una nueve edad y la reemplaza*/
void actualizar_edad(Contacto *c){

    printf("Ingrese una nueva edad: \n");
    unsigned int e;
    scanf("%d",&e);

    c->edad=e;
}

/*i. Dar de alta un contacto: void alta_contacto(struct Agenda *); pide por teclado
los datos del contacto a agregar (función crear_contacto) e inserta el resultado en
la agenda.*/

void alta_contacto(Agenda* p){
    Contacto c;
    c=crear_contacto();
    p->contactos[p->completas]=c;
    p->completas++;
}

/*ii. Modificar la edad de un contacto: void modificar_edad(struct Agenda *); pide
por teclado el nombre del contacto a modificar para identificarlo y luego actualiza su
edad (función actualizar_edad).*/

void modificar_edad(Agenda* agen){

    char nomb[20];
    
    printf("Seleccione un Contacto para cambiar su edad\n");
    fgets(nomb,sizeof(char)*20,stdin);
    sacar_salto(nomb);




    for(int i=0;i<agen->completas;i++){
        
        if(strcmp(((agen->contactos)[i].nombre),nomb)==0){
            
            actualizar_edad(&(agen->contactos[i]));
        }
    }
}


/*iii. Ver los datos de los contactos cargados: void imprimir_contactos(struct Agenda*);.*/

void imprimir_contactos(Agenda* agenda){

    int cargados=agenda->completas;
    for(int i=0;i<cargados;i++){
        printf("%s",agenda->contactos[i].nombre);
        printf("%s",agenda->contactos[i].telefono);
        printf("%d\n\n",agenda->contactos[i].edad);
        
    }
}

void limpiar_buffer(){
    char a;
    while ((a=getchar())!='\n'); 
}

/*f) Implemente una función double prom(struct Agenda *); que devuelva el promedio de
la edad de los contactos dentro de la agenda*/

double prom(Agenda * agend){
    unsigned int suma_edades=0;
    unsigned int contactos_n=agend->completas;
    for(int i=0;i<contactos_n;i++){
        suma_edades+=agend->contactos->edad;
    }
    float promedio=suma_edades/(float)contactos_n;
    return promedio;
}