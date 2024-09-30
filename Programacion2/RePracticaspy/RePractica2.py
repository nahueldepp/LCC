
from random import *
#Ejercicio 2. Escriba un programa que imprima por pantalla todas las fichas del dominó, una
#por línea y sin repetir.

def domino():
    """
    domino():none->list(tuple)
    Devuelve una lista con tuplas de tamaño dos, representando las fichas de domino
    """
    lista=[]
    for i in range(0,7):
        for j in range(i,7):
            ficha=(i,j)
            lista+=[ficha]
    return lista

#Ejercicio 3. Modifique el programa anterior para que pueda generar fichas de un juego que
#puede tener números de 0 a n.

def domino_n(n):
    """
    domino_n():int->list(tuple)
    Dado un entero, me permite representar las fichas de un domino de n números
    """
    lista=[]
    for i in range(0,n+1):
        for j in range(i,n+1):
            ficha=(i,j)
            lista+=[ficha]
    return lista

#Ejercicio 4. Escriba una función que tome una cantidad m de valores que serán ingresados
#por el usuario y, a medida que se ingresa cada número, muestre el factorial del mismo. El valor
#de m es ingresado inicialmente por el usuario.

def factorial(n):
    """
    factorial(): int-->int

    """
    factor=1
    if n==0:
        return factor
    else:
        for i in range(1,n+1):
            factor=factor*i
        return factor
    
def factoriales():
    """
    factoriales():none-->none

    """

    valor=int(input("Elija un valor para calcular su factorial y -1 para terminar: "))

    while valor!=-1:
        print(factorial(valor))

        valor=int(input("Elija un valor para calcular su factorial y -1 para terminar: "))


#Ejercicio 9. Escriba un programa que pida dos números enteros. El programa pedirá de nuevo
#el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo
#los dos números.
        
def mayor_de_dos(n,m):

    while m<n:
        m=int(input("El segundo valor es menor que el primero, ingrese uno mayor: "))
    
    return (n,m)


""" Ejercicio 10. Escriba una función que reciba dos números como parámetros y devuelva cuán-
tos múltiplos del primero hay que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea
mayor que el segundo.
c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operacio-
nes? """

#a)
def cant_multiplos_for(n,m):
    """
    cant_multiplos_for():int int-->int
    recibe dos números n<m, y devuelove la cantidad de multiplos de n hasta m

    """
    contador=0
    for i in range(n,m):
        if i%n==0:
            contador+=1
    return contador

def test_cant_multiplos_for():
    assert cant_multiplos_for(1,10)==9
    assert cant_multiplos_for(5,25)==4


#b)
def cant_multiplos_while(n,m):
    """
    cant_multiplos_while(): int int--> int
    toma dos números n<m, multiplica a n hasta que n*a>=m, y devuelve la cantidad de multiplos (a)
    """
    contador=0
    
    while contador*n<m:
        contador+=1
    return contador-1

def test_cant_multiplos_while():
    assert cant_multiplos_while(1,5)==4
    assert cant_multiplos_while(2,5)==2


"""Ejercicio 11. Manejo de contraseñas
a) Escriba un programa que contenga una contraseña inventada. El programa debe pre-
guntarle al usuario la contraseña y no permitirle continuar hasta que la haya ingresado
correctamente.
b) Modifique el programa anterior para que solamente permita como máximo una cantidad
fija de intentos.
c) Modifique el programa anterior para que sea una función que devuelva si el usuario in-
gresó la contraseña correctamente o no, mediante un valor booleano (True o False)."""


def ingresar_contraseña():
    """
    Contraseña= Pipo123
    """ 
    contraseñaI=input("Ingrese la contraseña: ")
    contador=3
    while contraseñaI!="Pipo123" and contador>1:
        contador-=1
        print("Contraseña incorrecta, le quedan",contador,"intentos.")
        contraseñaI=input("Vuelva a ingrsear la contraseña: ")
    if contraseñaI=="Pipo123":
        return True
    else:
        return False


"""Ejercicio 12. Escriba una función que reciba un número natural e imprima todos los números
primos que hay menores o iguales que ese número. Para esto se pide que:
a) Defina una función es_primo que toma un número natural y verifica si es un número primo.
b) Resuelva el problema usando la función definida en el punto anterior."""


def es_primo(n):
    """
    es_primo(n): int->Bool
    dado un número n, devuelve true si en es primo
    """
    contador=0
    for i in range(1,n):
        if n%i==0:
            contador+=1
    if contador==1:
        return True
    return False

def test_es_primo():
    assert es_primo(5)==True
    assert es_primo(7)==True
    assert es_primo(8)==False

def imprimir_primos(n):
    for i in range(n+1):
        if es_primo(i):
            print(i)

"""
Ejercicio 13. Potencias de dos
a) Escriba una función es_potencia_de_dos que reciba como parámetro un número natural
y devuelva True si el número es una potencia de 2 y False en caso contrario.
b) Escriba una función que, dados dos números naturales pasados como parámetros, de-
vuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
(0 si no hay ninguna potencia de 2 entre los dos). Utilice la función es_potencia_de_dos
descripta en el punto anterior.
"""

#a)

def es_potencia_de_dos(m):
    """
    es_poteencia_de_dos(m): int->bool
    recibe un entero y si es potencia de dos devuelve True, caso contraria false

    """
    n=m
    while n%2==0 and n>2:
       n=n/2 
    if n==2:
        return True
    return False

def suma_de_potencias_dos(n,m):
    """
    suma_de_potencias_dos(n,m): int int--> int
    Dado dos números, devuelve la suma de las potencias de dos en [n,m)
    """
    suma=0
    for i in range(n,m):
        if es_potencia_de_dos(i):
            suma+=i
    return suma

"""1) Simule lanzamientos de un dado. Muestre el resultado en cada intento y finalice cuando
salga el número 6. También añada cuantas veces se lanzó el dado."""

def lanzamiento_dado():
    valor=randint(1,6)
    contador=0
    while valor!=6:
        valor=randint(1,6)
        contador+=1
        print("Valor: ",valor,"Intento Nº:",contador)
    return valor

"""
2) Simule n lanzamientos de dos dados, donde n es un valor que se debe pedir que se
ingrese por teclado. Muestre cuántas veces los dados tuvieron el mismo resultado."""

"""
3) Simule n lanzamientos de un dado en un juego con las siguientes reglas: si sale 6 gana
4 pesos; si sale 3 gana 1 dólar; si sale 1 sigue jugando y si sale 2, 4 o 5 pierde 2 pesos.
Muestre los valores que salen y el resultado final del juego.
"""
def juego_dado(n):
    contador=0
    sumavalor=0
    while contador<=n:
        valor=randint(1,6)
        print(valor)
        if valor==6:
            sumavalor+=4
        elif valor==3:
            valor+=1
        elif valor==1:
            sumavalor
        else:
            sumavalor-=2
        contador+=1
    return sumavalor


#---------------------------------------------------------------------------------------------
def main():
    print(domino())
   # n=int(input("Ingrese un entero: "))
    #print(domino_n(n))

    #factoriales()



if __name__=="__main__":
    main()