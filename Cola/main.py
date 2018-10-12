"""
Cola:
Es una estructura de datos, caracterizada por ser una secuencia de elementos en
la que la operacion de insercion (push) se realiza por un extremo y la operacion de
extraccion (pop) por el otro. Tambien se le llama estructura FIFO (del ingles Firs In First Out),
debido a que el primer elemento en entrar sera tambien el primero en salir.

Operaciones:
1: insertar
2: eliminar
3: buscar
4: estado de la cola (vacia o con elementos)
5: retornar elemento frontal
6: retornar el tamaño de la cola
7: Etc.

"""

#from os import system
#system("cls")

from cola import Cola
#el error que marca en la cola no afecta al proyecto al ejecutarlo
cola = Cola()

cola.push(12)
cola.push(23)
cola.push(56)
cola.push(78)
cola.push(89)
cola.push(100)
cola.push(47)

cola.pop()
cola.pop()
cola.pop()

cola.show()

cola.front()