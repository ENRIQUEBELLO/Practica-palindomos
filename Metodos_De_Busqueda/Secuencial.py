class Secuencial:
    def busquedaLinea(self, A,n,x):
        encontrado=-1
        for k in range (n):
            if A[k] == x:
                encontrado=k
        return encontrado

    def busquedaLinealMejorada(self, A,n,x):
        encontrado=-1
        for k in range (n):
            if A[k] == x:
                encontrado=k
                break
        return encontrado

    def busquedaLinealCentinela(self, A,n,x):
        tmp=A[n]
        A[n]=x
        k=0
        while A[k] != x:
            k=k+1
            print(k)
            A[n]=tmp
            if k < n or A[n]==x:
                return k
            else:
                return -1
            return encontrado
    