from nodo import Nodo

class ListaEncadeada:

    def __init__(self):
        self.head = None
        self._size = 0

    def inseriraofinal(self,valor):
        if self.head:
                inicio=self.head
                while (inicio.proximo):
                        inicio= inicio.proximo
                inicio.proximo = Nodo (valor)
        else:
                self.head = Nodo(valor)

        self._size=self._size + 1

    def __len__(self):
        return self._size

    def get (self, index):
        pass

    def set (self, index,valor):
        pass

    def __getitem__(self, index):
        inicio= self.head
        for i in range (index):
            if inicio:
                inicio= inicio.proximo
            else:
                raise IndexError("Erro")
        if inicio:
            return inicio.dado
        else:
            raise IndexError("Erro")

    def __setitem__(self, index, valor):
        inicio = self.head
        for i in range(index):
            if inicio:
                inicio = inicio.proximo
            else:
                raise IndexError("Erro")
        if inicio:
            inicio.dado = valor
        else:
            raise IndexError("Erro")

    def buscar(self,valor):
        inicio=self.head
        i=0
        while(inicio):
            if inicio.data == valor:
                return i
            inicio = inicio.proximo
            i=i+1
        raise ValueError("{} valor não esta na lista. ".format(valor))

    def insert (self, index,valor):
        if index==0:
            nodo=Nodo(valor)
            nodo.proximo=self.head
            self.head = nodo
        else:
            inicio = self.head
            for i in range (index):
                if inicio:
                    inicio = inicio.proximo
                else:
                    raise IndexError ("Não existe este valor na lista")


lista=ListaEncadeada()