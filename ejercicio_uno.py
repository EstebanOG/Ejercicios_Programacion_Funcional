#[123,234,678] --> 348
def f(x):
    return list(map(int, str(x)))

def obtener_digito(lista):
    if lista == []:
        return ""
    return "{}{}".format(f(lista[0])[-1] , obtener_digito(lista[1:]))

print(obtener_digito([123,234,678]))