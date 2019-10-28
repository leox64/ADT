from stack import Stack

def eval_posfija(expresion):
    pila = Stack()
    print("posfija:",expresion)
    for elem in expresion:
        if elem.isdigit(): #NOTA.-solo funciona para operandos de un digito
            pila.push(elem)
        else:
            o1=pila.pop()
            o2=pila.pop()
            pila.push(str(eval(o2+elem.replace('^','**')+o1)))
    return pila.pop()

def main():
    #3+2
    exp='32+'
    print (eval_posfija(exp))
    #4+2-3
    exp='42+3-'
    print (eval_posfija(exp))
    #3+2*3-(8/4)
    exp='323*84/-+'
    print (eval_posfija(exp))
    #(9/3)-(5+2+3-4*2)*5
    exp='93/52+3+42*-5*-'
    print (eval_posfija(exp))
    exp = '32+53+-'
    print (eval_posfija(exp))
    exp = '52+52+2^/'
    print (eval_posfija(exp))
    exp='63/5+523*-+'
    print (eval_posfija(exp))
main()
