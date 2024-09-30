#include <stdio.h>
int main1()
{
    float celsius;
    int fahr=0;
    int salto=20;
    int maximo=300;
   
    while (fahr<=maximo){
        celsius=(5.0/9.0)*(fahr-32.0);
        printf("%3d\t%6.1f\n",fahr,celsius);
        fahr=fahr+salto;
    }

    
    printf("Hola,mundo\n"); 
    return 0;
}

int main2()
{
    int a, b, c, d=6, e;
    a = b = 3;
    c = a*b+d;
    e = (c + 5) / 4-3;
    e+=5;
    printf("Los resultados son %d y %d ", c, e);
    return 0;
}

/*Ejercicio 4. Determinar en qué estado está el agua en función de su temperatura: si es ne-
gativa el estado será sólido, si es menor que 100 será líquido y si es mayor que 100 será gas.
El valor de la temperatura deberá ingresarse.*/

char* estadoagua(float temperatura){
    char* estado;
    if(temperatura<0){
        estado = "solido";
    }
    else if(temperatura<100){
        estado = "liquido";
    }
    else{
        estado= "gaseoso";
    }

    return estado;
}

int main3 ()
{
    float x;
    printf("Introduzca la temperatura del agua: \n");
    scanf ("%f", &x);
    char* estado= estadoagua(x);
    printf("El estado del agua es: %s \n",estado);
    
    return 0;
}


/*Ejercicio 6. Construir un programa que calcule y presente por pantalla el signo del zodiaco
a partir de la introducción por teclado del día y mes de nacimiento como números enteros*/
void signos(int dia,int mes){

    if((dia>=22 && mes==12)||(dia<=20 && mes==1)){
        printf("Usted es Capricornio\n");
    }
    else if((dia>=21 && mes==1)||(dia<=19 && mes==2)){
        printf("Usted es Acuario\n");
    }
    else if((dia>=20 && mes==2)||(dia<=20 && mes==3)){
        printf("Usted es Piscis\n");
    }
    else if((dia>=21 && mes==3)||(dia<=19 && mes==4)){
        printf("Usted es Aries\n");
    }
    else if((dia>=20 && mes==4)||(dia<=20 && mes==5)){
        printf("Usted es Tauro\n");
    }
    else if((dia>=21 && mes==5)||(dia<=21 && mes==6)){
        printf("Usted es Géminis\n");
    }
    else if((dia>=22 && mes==6)||(dia<=21 && mes==7)){
        printf("Usted es Cáncer\n");
    }
    else if((dia>=22 && mes==7)||(dia<=21 && mes==8)){
        printf("Usted es Leo\n");
    }
    else if((dia>=22 && mes==8)||(dia<=22 && mes==9)){
        printf("Usted es Virgo\n");
    }
    else if((dia>=23 && mes==10)||(dia<=22 && mes==10)){
        printf("Usted es Libra\n");
    }
    else if((dia>=23 && mes==10)||(dia<=21 && mes==11)){
        printf("Usted es Escorpio\n");
    }
    else{
        printf("Usted es Sagitario\n");
    }
}   
int main(){
    int dia,mes;
    printf("Ingrese el dia y mes de su nacimiento: ");
    /*Recibe el dato de entra, dia y mes, dd/mm*/
    scanf("%d""/""%d",&dia,&mes);
    signos(dia,mes);

}

/*Ejercicio 9. Escriba un programa que muestre los números enteros del 1 al 100.*/

