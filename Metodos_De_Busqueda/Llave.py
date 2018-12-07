class Llave:
    def formaArreglo(self, tamanio):
        Arr=[None]*tamanio
        return Arr

    def obtenerLlaveNumerica(self, llave):
        hash=0
        for char in  str(llave):
            hash+=ord(char)
        return hash

    def H(self, llaveN):
        return llaveN%5

    def agregar(self, llave,valor,map,tamanio):

        llave_hash=H(obtenerLlaveNumerica(llave))

        ParllevarValor=[llave,valor]

        if  map[llave_hash] is  None:
            map[llave_hash]=list([ParllevarValor])
            return True
        else:

            for par in map[llave_hash]:
                if par [0]==llave:
                    par[1]=valor
                    return True

            for j in range(tamanio):
                llaveh=(llave_hash+j)%13
                if(llaveh==len(map)):
                    print("Tabla llena",llave_hash)
                    break
                else:

                    if  map[llaveh] is None:
                        map[llaveh]=list([ParllevarValor])
                        return True

    def buscar(self, llave,tamanio):

        llave_hash=H(obtenerLlaveNumerica(llave))

        if map(llave_hash) is not None:

            for par in map[llave_hash]:

                if par[0] == llave:
                    return par[1]
                else:
                    for j in range(tamanio):
                        llaveh=(llave_hash+j)%13
                        if(llaveh==len(map)):
                            break

                        for par1 in map[llaveh]:

                            if par1[0]== llave:
                                return par1[1]
        return None