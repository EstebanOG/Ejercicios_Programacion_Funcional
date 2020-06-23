#[[1,3,5,10], [6, 2, 8, 9]] -->[(10,1,11), (9,2,11)]
from functools import reduce
f = lambda a,b: a if (a > b) else b
g = lambda a,b: a if (a < b) else b
def ejercicio_tres(lista):
    if lista == []:
        return []
    return [((reduce (f, lista[0])), (reduce (g, lista[0])), ((reduce (f, lista[0])) + (reduce (g, lista[0]))))] + ejercicio_tres(lista[1:])

print(ejercicio_tres([[1,3,5,10], [6, 2, 8, 9]]))