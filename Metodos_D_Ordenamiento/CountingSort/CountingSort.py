class CountingSor:

    def CreaLista(self, k):
        L=[]
        for i in range(k+1):
            L.append(0)
        return L

    def CountingSort(self, A,k):
        C=CreaLista (k)
        B=Crealista(len(A)-1)
        for j in range(l,len(A)):
            C[A[j]]=C[A[j]]+1
        for i in range (1,k+1):
            C[i]=C[i]+C[i-1]
        for j in range (len(A)-1,0,-1):
            B[C[A[j]]]=A[j]
            C[A[j]]=C[A[j]]-1
        return B