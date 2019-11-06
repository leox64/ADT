def main():
    lista = [3,5,2,1]
    print(suma_lista(lista))

def suma_lista (l):
    if len(l) == 1:
        return l[0]
    else:
        actual = l.pop()
        return actual + suma_lista(l)

main()
