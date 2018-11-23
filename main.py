_autor_ = 'Enrique Bello'
from Pila import Pila

pila = Pila(6)

pila.push(20)
pila.push(49)
pila.push(110)
pila.push(159)
pila.push(196)
pila.push(200)
pila.push(284)

#pila.pop()


pila.show()

print("Size: %d"%(pila.Size()))
print("Estado:",pila.empty())
print("Top: %d"%(pila.Top()))
