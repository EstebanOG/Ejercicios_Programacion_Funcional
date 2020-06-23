class Nodo():
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha
def f(x):
    return list(map(int, str(x)))

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [f(arbol.valor)] + en_orden(arbol.derecha)

arbol = Nodo(15,Nodo(10,None,Nodo(12)),Nodo(25))
print(en_orden(arbol))