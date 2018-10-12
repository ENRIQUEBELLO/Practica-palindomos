class Pila:
   def __init__(self):
       self.items = []

   def push(self, dato):
       self.items.append(dato)

   def pop(self):
       try:
           return self.items.pop()
       except IndexError:
           raise ValueError('La pilsa esta vacia')

   def es_vacia(self):
       return self.items == []

   def limpiar_pila(self):
       self.clear()

   def cima_pila(self):
        return self.items[-1]

   def tamanio_pila(self):
       return len(self.items)