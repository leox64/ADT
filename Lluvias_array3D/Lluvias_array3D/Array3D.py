import xlrd


class Array3D:
    def __init__(self, rows, cols, depth):
        self.__cuadro = []
        self.__row = rows
        self.__col = cols
        self.__depth = depth

        for depth in range(depth):
            tmp = []
            for row in range(rows):
                tmp2 = []
                for col in range(cols):
                    tmp2.append(None)
                tmp.append(tmp2)
            self.__cuadro.append(tmp)

    def to_string(self):
        print(self.__cuadro)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):
        return self.__col

    def get_num_rebanadas(self):
        return self.__depth

    def set_item(self, r, c, d, valor):
        if (r >= 0 and r < self.__row) and (c >= 0 and c < self.__col) and (d >= 0 and c < self.__depth):
            self.__cuadro[d][r][c] = valor

    def set_num_cols(self, r, c, d):
        return self.__cuadro[d][r][c]

    def clearing(self, valor):
        for rebanada in range(self.__depth):
            for fila in range(self.__row):
                for columna in range(self.__col):
                    self.__cuadro[rebanada][fila][columna] = valor

    def funcion(self, depth, row, col):
        data = []
        for anio in range(1985, 2019):
            anio_lista = []
            archivo = xlrd.open_workbook(filename="./Precipitacion/" + str(anio) + 'Precip.xls')
            hoja = archivo.sheet_by_index(0)
            for estado in range(2, 3, 4):
                mes_lista = []
                for mes in range(1, 13):
                    mes_lista.append("%.2f" % hoja.cell_value(estado, mes))
                anio_lista.append(mes_lista)
            data.append(anio_lista)
        print(data)
