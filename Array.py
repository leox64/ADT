#array
class Array:
    def __init__(self,n):
        self.data=[]
        for i in range(n):
            self.__data.append(None)

    def get_length(self):
        return len(self.__data)

    def set_item(self,index,value):
        if index >= 0 and index < len(self.__data):
            self.__data[index] = value
        else:
            print("Fuera de rango")

    def get_item (self,index):
        if index >= 0 and index < len(self.__data):
            return self.__data[index] 
        else:
            print("Fuera de rango")

    def clearing (self,valor):
        for index in range(len(self.__data)):
            self.__data[index] = valor

    def to_string(self):
        print(self.__data)

#main
def main():
    arreglo = Array(10)
    arreglo.to_string()
    print(f"El tamaño es de {arreglo.get_length()}")
    arreglo.set_item(1,10)
    arreglo.to_string()
    arreglo.set_item(12,10)
    print (f"El elemento 1 es {arreglo.get_item(1)}")
    arreglo.get_item(20)
    arreglo.clearing(5)
    arreglo.to_string()
main()
