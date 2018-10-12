_autor_ = 'Enrique Bello'
numeros = [6, 8, 9, 12, 23, 19, 65, 33, 78, 89, 26, 45, 31]
print (numeros)
a = int(len(numeros) / 2)

print(a)
c = 0
for i in range(int(len(numeros) / 2)):
    c = c - 1
    x = numeros[i]
    numeros[i] = numeros[c]
    numeros[c] = x
print (numeros)

longitud = int(len(numeros)) - 1

a = int(0)

while((longitud - a) > a):
    aux = numeros[a]
    numeros[a] = numeros[longitud - a]
    numeros[longitud - a] = aux
    a = + 1
print(numeros)

while(a <= (longitud - a)):
    aux = numeros[a]
    numeros[a] = numeros[longitud - a]
    numeros[longitud - a] = aux
    a = a + 1

def invertirArreglo(lista, i, f):
    while(i <= f):
        aux = lista[f]
        lista[f] = lista[i]
        lista[i] = aux
        return invertirArreglo(lista, i, f)
