"""
Ordenamiento  Por Seleccion

es un algoritmo que consiste en ordenar los elementos de manera acendente o descendente

Funcionamiento
-Buscar el dato mas pequeño de la lista
-Intercambiarlo por el actual
-Seguir buscando el dato mas pequeño de la lista
-Esto se repetira sucecivamente

"""
lista = [4,2,6,8,5,7,0]

for i in range(len(lista)-1):
    minimo = i
    for x in range(i,len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux
    #print(lista)
print(lista)