class QuickSort:

    def intercambia(self, A, x, y ) :
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def Particionar(self, A,p,r):
        x=A[r]
        i=p-1
        for j in range(p,r):
            if (A[j]<=x):
                i=i+1
                intercambia(A,i,j)
        intercambia(A,i+1,r)
        return i+1

    def QuickSort(self, A,p,r):
        if ( p < r):
            q=Particionar(A,p,r)
            print(A[p:r])
            QuickSort(A,p,q-1)
            QuickSort(A,q+1,r)