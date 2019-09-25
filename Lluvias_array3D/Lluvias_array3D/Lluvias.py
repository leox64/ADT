from xlrd import sheet
from Array3D import Array3D
import xlrd


# num_rows=sheet.nrows
# num_col=sheet.ncols
# lecture = xlrd.sheet.lecture(2, 1)
# print(lecture.value)
def main():
    estado = int(input("que estado(1-32):"))
    anio = int(input("año(1985-2019):"))
    mes = int(input("mes(1-12):"))
    array = Array3D(anio, mes, estado)
    array.funcion(anio,mes,estado)


main()
'''
odernamiento:
es el proceso de cambiar la posicion de un grupo de datos con el objetivo de obtenerlos en un orden
ascendente o descendente. Los datos puden ser simples como int float, o tipos complejos como un ADT.


En programacion el ordenamiento es uno de los temas mas estudiados en ciencias de la computacion, 
dando como rsultado diferentes algortimos de ordenamiento:

1. Metetodo de la burbuja
Consta en iterar multiples veces sobre el arreglo causando que el elemntos mas grande (pesado) vaya
al fondo o al final del arreglo, alfinal de cada iteracion, provocando que los elemntos menores, 
(ligeros) se muevan al principio del arreglo (flotar).

Ejemplo:

8,5,9,3          5 8 3 9
                 

5 8 9 3

5 8 9 3

5 8 3 9 

'''
