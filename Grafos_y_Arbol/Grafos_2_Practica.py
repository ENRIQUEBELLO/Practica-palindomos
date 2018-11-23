class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()


class Grafo:
    vertices = {}

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice  "+key +" Susvecinos son:"+ str(self.vertices[key].vecinos))


g = Grafo()
a = Vertice('A')
g.agregarVertice(a)

for i in range(ord('A'), ord('I')):
    g.agregarVertice(Vertice(chr(i)))

edges = ['AB', 'AC', 'AD', 'AE', 'AF', 'AH', 'BD', 'BA', 'BE', 'BG', 'CH', 'CA', 'CF', 'DB', 'DA', 'DH', 'EG',
         'EB', 'EA', 'EF', 'FE', 'FA', 'FC', 'GB', 'GA', 'GE', 'HD', 'HA', 'HC']

for edge in edges:
    g.agregarArista(edge[:1], edge[1:])

g.imprimeGrafo()