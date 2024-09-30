#Ejercicio 1. Escriba un programa que imprima los primeros 25 números naturales pares.

def naturales_pares(n):
    """
    naturales_pares():int->list(int)
    Dado un entero, devuelve una lista con los enteros pares de 0 a n
    """
    list=[]
    for i in range(0,n+1,2):
        list+=[i]
    return list

def test_naturales_pares():
    assert(naturales_pares(8)==[0,2,4,6,8])

#Ejercicio 3. Escriba un programa que imprima los primeros n números pares mayores que m.
#¿Puede adaptar la solución propuesta en el ejercicio anterior para que resuelva este problema?
    
def naturales_pares_entre(m,n):
    """
    naturales_pares_entre(n,m): int,int -> list(int)
    Escriba un programa que imprima los primeros n números pares mayores que m.
    """

    list=[]
    if m%2==0:
        for i in range(m,n*2+m,2):
          list+=[i]
    else:
        for i in range(m+1,n*2+m,2):
          list+=[i]
    return list

#Ejercicio 5. Escriba un programa que calcule e imprima el resultado de la suma de los prime-
#ros n números naturales usando una función recursiva

def sumatoria(n):
    """
    sumatoria():int->int
    Realiza una sumatoria de los primeros n naturales
    """
    if n==0:
        return n
    else:
        return n+sumatoria(n-1)
    
def test_sumaoria():
    assert(sumatoria(5)==15)
        
#Ejercicio 6. Escriba un programa que calcule e imprima el resultado de la suma de los núme-
#ros naturales mayores que n y menores que m usando una función recursiva.
    
def suma_entre(n,m):
    """
    suma_entre():int int ->int
    toma dos valores enteros y devuelve la suma entre ellos
    """
    if n==m:
        return n
    else:
        return n+suma_entre(n+1,m)

def test_suma_entre():
    assert(suma_entre(0,10)==55)
    assert(suma_entre(5,10)==45)

#Ejercicio 7. Escriba un programa que reciba un nombre y retorne el nombre pasado concate-
#nado 2 veces. Es decir, supongamos que la función se llama duplica, si hacemos duplica(”F ederico”)
#el resultado que deberíamos obtener sería: ”F edericoF ederico”.
    
def duplica(cadena):
    """
    duplica():str->str
    duplica una cadena
    """
    return cadena*2

#Ejercicio 9. Realice los siguientes ítems:
#a) Escriba una función suma que reciba dos números y retorne el resultado de la suma de
#ambos.
#b) Escriba una función resta que reciba dos números y retorne el resultado de la resta de
#ambos.
#c) Escriba una función multiplica que reciba dos números y retorne el resultado de la multi-
#plicación de ambos números.
#d) Escriba una función divide que reciba dos números y retorne el resultado de la división
#de ambos números.
#e) Escriba un programa que muestre un mensaje pidiendo que se elija una opción siendo
#las mismas:
#1. Suma
#2. Resta
#3. Multiplica
#4. Divide
#Luego de elegir la operación debe pedirse el ingreso de dos números y mostrar el resul-
#tado de la operación correspondiente (invocando a la función homónima).
#f) Agregue una opción que sea
#5. Salir
#de manera que, mientras no se ingrese un 5 el programa siga funcionando repitiendo la operatoria anterior

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    return x/y




#--------------------------------------------------------------------------------------------
def main():

    cadena=input("ingrese una cadena: ")
    print(duplica(cadena))

    opcion=int(input("Elija una opción\n 1.Suma\n 2.Resta\n 3.Multiplica\n 4.Divide\n 5.Salir\n "))
    
    while opcion!=5:
        
        if opcion==1:
            print("Elija dos números")
            n1=int(input("n1="))
            n2=int(input("n2="))
            print(suma(n1,n2))
        elif opcion==2:
            print("Elija dos números")
            n1=int(input("n1="))
            n2=int(input("n2="))
            print(resta(n1,n2))
        elif opcion==3:
            print("Elija dos números")
            n1=int(input("n1="))
            n2=int(input("n2="))
            print(multiplicacion(n1,n2))
        elif opcion==4:
            print("Elija dos números")
            n1=int(input("n1="))
            n2=int(input("n2="))
            print(division(n1,n2))
        opcion=int(input("Elija una opción\n 1.Suma\n 2.Resta\n 3.Multiplica\n 4.Divide\n 5.Salir\n "))
        
        


if __name__=="__main__":
    main()