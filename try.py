import timeit
from LinkedList import LinkedList as llist


lit = llist([1,1,1,3,4,4,5,2,2])
lista = [1,2,3,4,5,6]

if lit.get(0) == lit.get(len(lit)-1).next:
    print(True)
else:
    print(False)