#[123, 456] --> [[3, 6, 9], [12, 15. 18]]
def f(x):
    return list(map(int, str(x)))

def obtener_multiplos(lista):
    if lista == []:
        return []
    return [list(map(lambda x: x*3, f(lista[0])))] + obtener_multiplos(lista[1:])

print(obtener_multiplos([123,456]))

