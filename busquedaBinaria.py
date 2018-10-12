"""
Busqueda binaria
Buscar datos en una coleccion de datos

Ventajas:
Realiza menos comparaciones que el metodo de busqueda lineal

Requisitos antes de realizar dicho algoritmo:
Tener la lista ordenada de manera acendente (Menor A Mayor)

Algoritmo:
1- calcular el punto medio, (izquierda + derecha)/2
2- comparar el punto medio con el dato a buscar
3- si es igual el dato al punto medio, retornar indice
4- si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio + 1
5- si el dato a buscar es menor que el punto medio, derecha es igual al valor del medio - 1
6- se seguira ejecutando siempre y cuando izquierda sea menor o igual a derecha

"""

def busqueda_binaria(dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <= derecha:
        medio = (izquierda + derecha)//2
        if dato ==lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return  None

def buscar(dato):
    if busqueda_binaria(dato) == None:
        return "El dato %d no se encontro"%(dato)
    else:
        return "El dato %d se encontro en el indice: %d"%(dato,busqueda_binaria(dato))

lista = [5,12,15,30,50,65,70,87,88,96,100,125,139,143,155.167,172,189,191,200]

for i in range(len(lista)):
    print("%d  =>  %d"%(i,lista[i]))


print(buscar(100))
