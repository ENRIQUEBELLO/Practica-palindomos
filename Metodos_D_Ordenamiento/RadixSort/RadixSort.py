class RadixSort:

    def SeparaCadena(self, cad):
        A2=[]
        for j in cad:
            A2.append(j)
        return A2

    def CreaLista2(self, k):
        L=[]
        for i in range(k+1):
            L.append([0]*2)
        return L

    def CreaLista(self, k):
        L=[]
        for i in range(k+1):
            L.append(0)
        return L

    def obtenerElemSinClaves(self, E):
        Elem=[]
        Elem.append("000000")
        for i in range(1,len(E)):
            Elem.append(E[i][0])
        return Elem

    def CountingSort2(self, A,k):
        C=CreaLista(k)
        B=CreaLista2(len(A)-1)
        for j in range(1,len(A)-1):
            C[A[j][1]]=C[A[j][1]]+1
        for i in range (1,k+1):
            C[i]=C[i]+C[i-1]
        for j in range (len(A)-1,0,-1):
            B[ C[A[j][1]] ][1]=A[j][1]
            B[ C[A[j][1]] ][0]=A[j][0]
            C[A[j][1]]=C[A[j][1]] -1
        return B

    def radixSort(self, A):
        numCar=len(A[1])
        for i in range (numCar,0,-1):
            cc=FormaArregloConClaves(A,i)
            print (cc)
            ordenado=CountingSort2(cc, 122)
            A=obtenerElemSinClaves(ordenado)
        return A