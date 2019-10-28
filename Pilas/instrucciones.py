"""
Aplicaciones de las pilas en ciencias dela computación.

-Verificar balanceo de expresiones aritmeticas.
-Adminstración de llamadas a funciones en lengujes de progracion.
-Recorrer arboles y grafos (ADT'S).
-Conversión de notación aritmetica: infija,posfija y prefija.
-Evaluar expresiones aritmeticas:posfija y prefija.
-Manejo de memoria an elos sistemas operativos.
-Backtracking (inteligencia artificial).


Algoritmo para cambiar de infija a posfija.
dada una cadena que representa una expresión aritmetica:
    Paso 1.- Crea una pila y agrega al inicio un parentesis de apertura y a la cadena
agregale un parentesis de cierre al final.
    Paso 2.- Recorre la cadena de izquierda a derecha y repite los pasos de l tres al seis
para cada elemento de la cadena hasta que la pila esté vacía.
    Paso 3.- Si se encuentra un operando agregalo a la salida
    Paso 4.- si se encuantra un parentesis de apertura agregal o a la pila.
    Paso 5 .- Si se encuentra un opreador entonces:
Paso 5.1.- Haz un "pop" repetidamente spobre lapila y agraga el valor obtenido del "pop"
a la salida,  y cada opreador en el tope de la pila que tiene la misma priorida o mayor que el
operador encontrado.
Paso 5.2.- Agrega el operador a la pila.
    Paso 6.- Si se encuantra un parentesis de cierre:
Paso 6.1.- Repetidamente haz un "pop" sobre la pila y agrega el valor sacado a la salida
hasta que un parentesis de apertura sea encontrado (en el top de la pila).
Paso 6.2.- Elimina el parentesis de apertura de la pila.

"""

"""
Algoritmo para evaluar una expresion matemática en notación posfija.
Considere una cadena de entrada en notación posfija:
Paso 1.- Pra cada elemento (de izquierda aderecha) realizar lo siguiente.
Paso 2.- Si el elemento es un operando hacerle "push" a la pila de lo contrario declarar la
variable O1 y hacerla igual a un "pop" sobre la pila, hacer "pop" y asignarlo a la variable O2
y haces un "push(eval(O2+elem+O1))"

"""
