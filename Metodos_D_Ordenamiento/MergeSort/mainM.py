import random
from time import time
from MergeSort import mergeSort

a = []
b = mergeSort()

for i in range(0, 100):
     a.append(random.randint(0,1000))

print (a)

inicio = time()
c = b.MergeSort(a)
t_final = time() - inicio
print (c)
print (t_final)