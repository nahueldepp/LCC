#include <stdio.h>

/*Ejercicio 9. Escriba un programa que muestre los números enteros del 1 al 100.*/

int main1(){
    int i=0;
    while(i<=100){
        printf("%d\n",i);
        i++;
    }
    return 0;
}

/*jercicio 10. Escriba un programa que muestre los números impares del 1 al 100*/

int main2(){
    int i=1;
    while(i<=100){
        printf("%d\n",i);
        i+=2;
    }
    return 0;
}

/*Ejercicio 11. Escriba un programa que pida dos números y muestre todos los números que
van desde el primero al segundo. Se debe controlar que los valores son correctos, es decir, que
el primero es menor que el segundo.*/
void entre_ayb(int a, int b){
    if(a<b){
        while(a<=b){
        a++;
        printf("%d\n",a);
    }
    }
    else{
        printf("a debe ser menor a b\n");
    }
    
}

void main3(){
    int a,b;
    printf("Escriba dos números, el primero menor que el segundo: ");

    scanf("%d""%d",&a,&b);

    entre_ayb(a,b);
    
}

/*Ejercicio 12. Escriba un programa que dado un número ingresado determine si el mismo es
primo o no.*/

void es_primo(int n){
    int i=2;
    int con=0;
    while (i<n && con<1){
        if((n%i)==0){
            con++;
        }
        i++;
    }
    if (con>0){
        printf("No es primo\n");
    }
    else{
        printf("El número es primo\n");
    }
}
void main(){

    int p;
    printf("Ingrese un número para ver si es primo: ");
    scanf("%d",&p);
    
    es_primo(p);
}

