import random
from time import time

class mergeSort:
    def CrearSubArreglo(self, A, indIzq, indDer):
        return A[indIzq:indDer+1]

    def Merge(self, A, p, q, r):
        z = mergeSort()
        Izq = z.CrearSubArreglo(A, p, q)
        Der = z.CrearSubArreglo(A, q + 1, r)
        i = 0
        j = 0
        for k in range(p,r+1):
            if (j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
                A[k] = Izq[i]
                i = i + 1
            else:
                A[k] = Der[j]
                j = j + 1
        return A

    def MergeSort(self, A, p, r):
        z = mergeSort()
        if r - p > 0:
            q = int((p+r)/2)
            z.MergeSort(A, p, q)
            z.MergeSort(A, q + 1, r)
            z.Merge(A, p, q, r)
