#ejercicios de la practica 3, listas y tuplas. 

"""Ejercicio 1. Escriba una función posicionesMultiplo que tome una lista y un número y re-
torne la lista formada por los elementos que están en las posiciones múltiplos de ese número.
Por ejemplo: posicionesMultiplo([1,2,3,4,5,6,7],2) retorna [1,3,5,7] y
posicionesMultiplo([1,2,3,4,5,6,7],3) da como resultado [1,4,7]."""


def posiciones_multiplo(lis,n):
    """
    posiciones_multiplo(): list(int) int -> list(int)
    Toma una lista y un número y devuelve una lista formada por los elementos de la lista previa que 
    estaban en las posiciones multiplos de n.
    Creando una lista nueva.
    """
    lisv=[]
    k=len(lis)
    for i in range(k) :
        if n*i<k:
            lisv[i:i]=[lis[n*i]]
    return lisv

def test_posiciones_multiplo():
    assert(posiciones_multiplo([11,12,17,14,5],2)==[11,17,5])
    assert(posiciones_multiplo([11,12,6,7,9,5],3)==[11,7])

"""Ejercicio 2. Escriba una función que tome una lista de números y devuelva la suma acumu-
lada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es
la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el
siguient"""

def suma_acumulada(lista):
    """
    suma_acumulada(): list(int)->list(int)
    dada una lista de números, devuelve una lista con las suma acumulada.
    """      
    lis_sum=[]
    sum=0
    for i in lista:
        sum=sum+i
        lis_sum+=[sum]
    return lis_sum

def test_suma_acumulada():
    assert(suma_acumulada([1,2,3,4,5])==[1,3,6,10,15])
    assert(suma_acumulada([2,3,5,8])==[2,5,10,18])

"""Ejercicio 3. Escriba una función llamada elimina que tome una lista y elimine el primer y
último elemento de la lista. La función debe devolver una nueva lista con los elementos que no
fueron eliminados."""

def elimina(lista):

    """
    elimina(): list -> list
    """
    k=len(lista) 
    lista[(k-1):k]=[]
    lista[0:1]=[]
    return lista

def test_elimina():
    assert(elimina([1,2,3,4])==[2,3])
    assert(elimina([5,8,6,4,3,1,15])==[8,6,4,3,1])

"""
Ejercicio 4. Escriba una función ordenada que tome una lista como parámetro y devuelva
T rue si la lista está ordenada en orden ascendente y F alse en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna T rue y ordenada(["b", "a"]) retorna F alse.
"""

def ordenada(lista):
    """
    ordenada(): int->boolean
    Dada una lista de elementos comparables, devuelve True si estan ordenados
    """

    orden=True
    i=0
    k=len(lista) #4
    while i<k-1 : #3
        if (lista[i]<lista[i+1])==False:
            
            orden=False
        
        i+=1
    return orden 

"""Ejercicio 5. Escriba una función llamada duplicado que tome una lista y devuelva T rue si
tiene algún elemento duplicado. La función no debe modificar la lista."""

def duplicado(lista):
    """
    duplicado():list -> Bool
    Dado una lista, si tiene un elemento duplicado devuelve True, sino, false
    Ejemplo:
    duplicado([1,2,2,3])==True
    duplicado([1,2,3])==False

    """
    dupli=False
    k=len(lista)
    for i in range(k):
        if lista[i] in (lista[0:i]and lista[i+1:]) :
            dupli=True 
    return dupli

def test_duplicado():
    assert(duplicado([1,2,3,4,5])==False)
    assert(duplicado([1,2,3,4,5,3])==True)


"""Ejercicio 6. Escriba una función llamada eliminaDuplicados que tome una lista y devuelva
una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo
orden. Ayuda: puede utilizar la función sort."""

def eliminar_duplicado(lista):
    """
    eliminar_duplicado(): list -> list
    Toma una lista, y devuelve una sin los elemnetos duplicados de la anterior
    """
    lista.sort()
    i=0
    while duplicado(lista)==True:
        if lista[i] in lista[i+1:]:
            lista[i:i+1]=[]
        i+=1
    
    return lista

def test_eliminar_duplicados():
    assert(eliminar_duplicado([2,3,7,6,5,4,7,8,9,9,])==[2,3,4,5,6,7,8,9])
    assert(eliminar_duplicado([1,2,2,3,3])==[1,2,3])


"""
Ejercicio 8 Implemente la función busquedaDicotomica que toma una lista de palabras ordenadas alfabé-
ticamente y una palabra a buscar y retorna si la palabra está en la lista o no.
"""

def busquedaDicotomica(lista,palabra):

    k=len(lista)
    izq=0
    med=der+izq//2
    der=k-1

    while izq<=der :
        med=der+izq//2
        if lista[izq]<=palabra<=lista[med]:
            der=med
        
            

