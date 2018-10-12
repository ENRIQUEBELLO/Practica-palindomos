lista = [21,45,69,58,20]

lista = lista + [15] + [50]

print(lista)
for i in range(len(lista)):
    print("index[%d] => %d"%(i, lista[i]))
print(lista[::-1])
