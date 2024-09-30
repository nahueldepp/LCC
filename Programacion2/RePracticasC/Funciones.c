#include <stdio.h>

/*Ejercicio 15. Escribir una función maximo que tome como parámetro dos enteros y devuelva
el máximo entre ellos. Utilizar esa función para calcular el máximo entre 4 enteros que se le
soliciten al usuario*/

int maximo(int m, int n){
    if(m<n){
        return n;
    }
    else{
        return m;
    }
}
int main1(){

    int a,b,c,d;
    printf("Ingrese 4 enteros para saber su maximo: ");
    scanf("%d %d %d %d",&a,&b,&c,&d);
    int max;
    max=maximo(maximo(a,b),maximo(c,d));
    printf("El maximo es: %d \n",max);
    
    return 0;


}

int fibo(int n){
    
    if (n==0){
        return 0;
    }
    else if (n==1){
        return 1;
    }
    else{
        return fibo(n-1)+fibo(n-2);
    }
}

int main(){
    int n;
    printf("Seleccione un núemro\n");
    scanf("%d",&n);
    printf("Su número de fibonachi es: %d \n", fibo(n));


}