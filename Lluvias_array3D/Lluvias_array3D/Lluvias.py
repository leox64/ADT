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
