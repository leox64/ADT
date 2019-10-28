"""
Pila: Es una estructura de ddatos lineal usada para almacenar datos con el
protocolo (last-in, first out). Lo cual signifixca que al insertar (push),se agregan
al tope de la estuctura y un elemento se saca (pop) del mismo topede la estuctura.
El ultimo elemento insertado se la llama tope (top)y el elemento totalmete opuesto se le llama
base.

"""

class Stack:
    def __init__(self):
        self.__data = []
        self.__top = 0
    def is_empty(self):
        return len(self.__data)==0

    def length (self):
        return len(self.__data)

    def pop(self):
        if self.__top != 0:
            self.__top -= 1
            return self.__data.pop()

    def peek (self):
        if self.__top != 0:
            return self.__data[self.__top-1]
        else:
            return None


    def push(self,elem):
        self.__data.append(elem)
        self.__top += 1

    def to_string(self):
        for elem in self.__data:
            print(elem)

            
        
