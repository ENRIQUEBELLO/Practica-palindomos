import math
class Binaria:
    def BusquedaBinIter(self, A,x,izquierda,derecha):

        while izquierda <= derecha:
            medio = math.floor((izquierda+derecha)/2)
            if A[medio] == x:
                return medio
            elif A[medio] < x:
                izquierda = medio+1
            else:
                derecha = medio-1
        return -1

    def BusquedaBinRecursiva(self, A,x,izquierda,derecha):
        if izquierda > derecha:
             return -1
        medio = math.floor((izquierda+derecha)/2)
        print(medio)

        if A[medio] ==x:
                return medio

        elif A[medio] < x:

            return BusquedaBinRecursiva(A,x,medio+1,derecha)
        else:
            return BusquedaBinRecursiva(A,x,izquierda,medio-1)