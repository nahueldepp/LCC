#include<stdio.h>

#define LARGO 12 // largo de la lista de alturas
double aAlturas[]={1.95,1.89,1.88,1.86,1.86,2.0,2.0,2.0,2.0,2.07,2.09,2.12};


//1-Promedio aritmetico e la altura del parana
//2-¿Cual es la altura maxima registrada?
//3-Calculo de la moda: El conjunto de datos puede tener una sola moda,ser ultimodal o no tener moda

double altmax(double arr[]);
double promedioA(double arr[]);
double enlista(double n,double arr[]);
void filtrarl(double or[],double sr[] );
void moda(double arr[]);
void main(void){
    double k=promedioA(aAlturas);
    printf("El pormedio aritmetico es de las alturas del rio parana sera: %f\n",k );
    double amax=altmax(aAlturas);
    printf("La altura maxima es: %0.2f\n",amax);
    moda(aAlturas);
}

/*promedioA: double[]->double
Dado una lista de nùmeros flotantes(alturas), devuelve el promedio aritmetico
*/
double promedioA(double arr[]){
    
    double n;
    for(int i=0;i<LARGO; i++){
        n+=arr[i];
    }

    n=n/LARGO;

    return n;
}

/*altmax:double[]->double
Dado una lista de alturas, devuelve la altura maxima*/
double altmax(double arr[]){
    double z=arr[0];
    for(int i=0;i<LARGO;i++){
        if(z<arr[i]){
            z=arr[i];
        }
    }
    return z;
}


/*enlista:double double[]->int
Dado un número y una lista, determina si el número esta dentro de esta, si es asi, devuelve 1,
0 en caso contrario*/

double enlista(double n,double arr[]){
    for(int i=0;i<LARGO;i++){
        if(n==arr[i]){
            return 1;
        }
    }
    return 0;
}
/*filtrarl:->double[] double[]->void
Dada dos listas de alturas, una con alturas repetidas y otra vacia, 
copia los elementos de la primera sin repetir en la segunda*/

void filtrarl(double or[],double sr[] ){

    int i=0;
    int j=0;
    for(i,j;i<LARGO;i++){

        if(enlista(or[i],sr)==0){
            sr[j]=or[i];
            j++;
        }
    }
    
    sr[i++]=-1;

}
/*modas:double[]->double
Dado una lista de alturas, devuelve la/s altura/s que mas se repiten*/

void moda(double arr[]){
    
    double lissinrep[LARGO+1];
    filtrarl(arr,lissinrep);
    
    int max,max2;
    max=0;
    int mi,mi2;//indices de los valores que mas se repiten 
    mi=0;
    for(int i=0;lissinrep[i]!=-1;i++){
        int k=0;
        for(int j=0;j<LARGO;j++){
            
            if(lissinrep[i]==arr[j]){
                k++;
            }
        }
        if(max<k){
            mi2=mi;
            max2=max;
            mi=i;
            max=k;
        }
    }
    if (max==1){
        printf("Es conjunto de datos es amodal\n");
    }
    else if(max2==max){
        printf("El conjunto es multimodal\n");
        printf("Los valores que mas se repiten son: %f y %f, %d veces\n",lissinrep[mi],lissinrep[mi2],max);
    }
    else{
        printf("El conjunto solo tiene una moda\n");
        printf("El valor que mas se repite es: %.2f, %d veces\n",lissinrep[mi],max);
    }
    

}