"""
Link: https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
"""


def shapeArea(n):
    valorDeLados = 0
    listaDeAreas = [1]
    for x in range(n - 1):
        valorDeLados += 4
        listaDeAreas.append(valorDeLados)
    return sum(listaDeAreas)


# Outra resolução
def shapeArea2(n):
    return n**2 + (n-1)**2


# Testes
print(shapeArea(5))
print(shapeArea(1))
print(shapeArea(8000))
