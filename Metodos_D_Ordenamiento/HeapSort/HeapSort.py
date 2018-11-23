class HeapSort:

    import math

    def hIzq(self, i):
        return 2*i

    def hDer(self, i):
        return 2*i+1

    def intercambia(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def MaxHeapify(self, A,i,tamanoHeap):
        L=hIzq(i)
        R=hDer(i)
        if ( L <= tamanoHeap and A[L]>A[i]):
            posMax=L
        else:
            poxMax=i
        if (R <= tamanoHeap and A[R]>A[poxMax]):
            posMax=R
        if (posMax != i):
            intercambia(A,i,posMax)
            MaxHeapify(A,posMax,tamanoHeap)

    def construirHeapMaxIni(self, A,tamanoHeap):
        for i in range(math.ceil(tamanoHeap/2) - 1, 0, -1):
            MaxHeappify(A,i,tamanoHeap)

    def OrdenacioHeapSort(self, A,tamanoHeap):
        construirHeapMaxIni(A,tamanoHeap)
        for i in range(len(A[1:]), 1, -1):
            intercambia(A,1,i)
            tamanoHeap=tamanoHeap-1
            MaxHeapify(A,1,tamanoHeap)