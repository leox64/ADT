"""
listas doblemante ligadas ADT
ListaDoblementeEnlazada()
get_size() -> Regresa el numero de elementos que hay en la cola
insert(value) -> inserta al final 
find_from_head(value)
find_from_tail(value)
remove_from_head(value)
remove_from_tail(value) ->
insert_between(value,predecesor,sucesor) -> Inserta entre dos nodos
trasversal() -> Inserta los nodods desde head hasta tail
reverse_trasversal() -> Imprime los nodos desde tail hasta head 
"""
class NodoDoble:
    def __init__ (self,value,siguiente, previo):
        self.data = value
        self.next = siguiente
        self.prev = previo

class ListaDoblementeEnlazada:
    def __init__ (self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head 
        self.__size = 0 

    def get_size(self):
        return self.__size

    def is_empty(self)

    def insert (self,value):

        if self.__size == 0:
            nuevo = NodoDoble (value,self.__tail,self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1

    def transversal(self):
        curr_Node = self.__head
        while curr_Node.next != None:
            print(curr_Node.data,"->",end="")
            curr_Node = curr_Node.next
        print("")

    def reverse_transversal(self):
        curr_Node = self.__tail
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end="")
            curr_Node = curr_Node.prev
        print("")


