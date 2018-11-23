import random
from time import time
from BubleSort1 import bubbleSort

a = []
b = bubbleSort()

for i in range(0, 100):
     a.append(random.randint(0,1000))

print (a)

inicio = time()
c = b.bubbleSort(a)
t_final = time() - inicio
print (c)
print (t_final)