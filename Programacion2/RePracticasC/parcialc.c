#include <stdio.h>
#include <assert.h>


/*Ejercicio 1: Definir Usando la Receta
En esta oportunidad los hermanos, Ricardo y Rebeca Losrapidos, necesitan que los ayu-
demos a programar las siguiente funciones para una matriz entera de dimensión 3 × 4:
suma_fila: esta función recibe una matriz, las dimensiones correspondientes a las can-
tidad de filas y columnas, y la fila específica que se desea sumar. La función devuelve la
suma de los elementos de la fila señalada.
suma_columna: esta función recibe una matriz, las dimensiones correspondientes a las
cantidad de filas y columnas, y la columna señalada que se desea sumar. La función
devuelve la suma de los elementos de la columna especificada.
matriz_impar: esta función recibe una matriz, las dimensiones correspondientes a la
cantidad de filas y columnas, y determina si todos sus elementos son impares, en tal caso,
retornará 1 y en caso contrario 0
La receta de cada función sólo deberá incluir:
Signatura de la función.
Declaración de propósito.
Ejemplos.*/

int suma_fila(int filas,int columnas,int matriz[filas][columnas],int fila_selec);
void test_suma_fila(void);
int suma_columnas(int filas, int columnas, int matriz[filas][columnas],int colomna_selc);
void test_suma_columnas(void);
int matriz_impar(int filas, int columnas ,int matriz[filas][columnas]);
void test_matriz_impar(void);

void main(void){

   int matriz [3][4]={
    {1,2,3,4},
    {2,5,4,7},
    {3,7,5,3},
   };
   void test_suma_fila(void);
   void test_suma_columnas(void);
   void test_matriz_impar(void);
}



/*suma_fila: int int int[][] int->int
 esta función recibe una matriz, las dimensiones correspondientes a las can-
tidad de filas y columnas, y la fila específica que se desea sumar. La función devuelve la
suma de los elementos de la fila señalada.*/

int suma_fila(int filas,int columnas,int matriz[filas][columnas],int fila_selec){

    int suma_tot=0;

    for(int i=0;i<columnas;i++){
        suma_tot+= matriz[fila_selec][i];
    }

    return suma_tot;
}

void test_suma_fila(void){
    int matriz_a[2][2]={
        {1,3},
        {4,3}
    };
    assert(suma_fila(2,2,matriz_a,2)==7);
    assert(suma_fila(2,2,matriz_a,1)==4);

}

/*suma_columna: int int int[][] int ->int
esta función recibe una matriz, las dimensiones correspondientes a las
cantidad de filas y columnas, y la columna señalada que se desea sumar. La función
devuelve la suma de los elementos de la columna especificada.*/
int suma_columnas(int filas, int columnas, int matriz[filas][columnas],int colomna_selc){
    int suma_tot=0;

    for(int i=0;i<filas;i++){
        suma_tot+=matriz[i][colomna_selc];
    }
    return suma_tot;
}

void test_suma_columnas(void){
    int matriz_a[2][2]={
        {1,3},
        {4,3}
    };
    assert(suma_columnas(2,2,matriz_a,2)==6);
    assert(suma_columnas(2,2,matriz_a,1)==5);

}


/*matriz_impar: int int int[][]->int 
esta función recibe una matriz, las dimensiones correspondientes a la
cantidad de filas y columnas, y determina si todos sus elementos son impares, en tal caso,
retornará 1 y en caso contrario 0*/


int matriz_impar(int filas, int columnas ,int matriz[filas][columnas]){

    for(int i=0; i<filas;i++){
        for(int j=0;j<columnas;j++){
            if((matriz[i][j]%2)==0){
                return 0;
            }
        }
    }
    return 1;
}

void test_matriz_impar(void){
    int matriz_a[2][2]={
        {1,3},
        {4,3}
    };
    int matriz_b[3][2]={
        {1,5},
        {7,3},
        {1,3}
    };
    assert(matriz_impar(2,2,matriz_a)==0);
    assert(matriz_impar(3,2,matriz_b)==1);

}