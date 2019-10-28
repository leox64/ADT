from stack import Stack
def main():
    numeros = Stack()
    numeros.push(8)
    numeros.push(10)
    numeros.push(11)
    numeros.to_string()
    print(f"La pila tiene {numeros.length()} elementos")
    print(f"El elemento en el tope es {numeros.peek() }")

    while not numeros.is_empty():
        print(numeros.pop(),',',end='')

main()
