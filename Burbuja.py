"""
Metodo de ordenamiento de burbuja
Revisa cada elemento de la lista con el siguiente elemento, intercambiandolos de posicion
si estan en el orden equivocados.

Ejemplo
4 2 6 8 5 7

2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8

"""
lista = [4,2,6,8,5,7]

for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux
            print(lista)
