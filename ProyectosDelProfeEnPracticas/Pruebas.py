from Pila import Pila
from Colas import Cola

colita=Cola()
print(colita.cola_vacia())


colita.insertar_dato(4)
print(colita.cola_vacia())

colita.insertar_dato(2)
colita.insertar_dato(7)
colita.insertar_dato(3)
colita.insertar_dato(6)
colita.insertar_dato(8)
print(colita.cola_vacia())

print(colita.inicio_cola())
extraer = colita.quitar_dato()
print(colita.inicio_cola())