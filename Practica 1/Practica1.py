class Practica:
    def __init__(self):
        self.items: []

    def insertar_dato(self, datos):
        self.items.append(datos)

    def quitar_dato(self):
        try:
            return self.items.pop(0)
        except  IndexError:
            raise ValueError('La cola esta vacia')

    def cola_vacia(self):
        return self.items==[]

    def inicio_cola(self):
        return self.items[0]

    def tamanio_cola(self):
        return len(self.items)