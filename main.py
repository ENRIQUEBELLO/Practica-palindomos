from Pila import Pila

pila = Pila(6)

pila.push(45)
pila.push(90)
pila.push(100)
pila.push(115)
pila.push(123)
pila.push(129)
pila.push(132)

#pila.pop()


pila.show()

print("Size: %d"%(pila.Size()))
print("Estado:",pila.empty())
print("Top: %d"%(pila.Top()))
