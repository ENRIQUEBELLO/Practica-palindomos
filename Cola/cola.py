__autor__='ENRIQUE BELLO'
class Cola():

    def __init__(self):
        self.cola = []
        self.size = 0

    def empty(self):
        return len(self.cola) ==0

    def push(self,dato):
        self.cola += [dato]
        #self.cola = self.cola + [dato]
        self.size += 1

    def pop(self):
        if self.empty():
            print("la cola esta vacia")
        else:
            self.cola = [self.cola[i] for i in range(1,self.size)]
            self.size -= 1

    def show(self):
        n = self.size - 1
        while n > -1:
            print("[%d]  =>  %d"%(n,self.cola[n]))
            n -= 1

    def front(self):
        if self.empty():
            print("Cola vacia")
        else:
            print("Primer dato: %d"%(self.cola[0]))