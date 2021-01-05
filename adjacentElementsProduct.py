"""
https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

--EXPLICAÇÃO--
Adjacente é o elemento que está ao lado, ou seja, no caso do teste 1 [3, 6, -2, -5, 7, 3] o 7 e o 3 geram o maior
produto (multiplicação) dentre (3*6), (6*-2), (-2*-5),(-5*7),(7*3).
--EXPLICAÇÃO--
"""


def adjacentElementsProduct(inputArray):
    array2 = []
    for x, y in zip(inputArray[0::], inputArray[1::]):
        array2.append(y * x)
    return max(array2)


# Testes

teste1 = [3, 6, -2, -5, 7, 3]
teste2 = [-1, -2]
teste3 = [5, 1, 2, 3, 1, 4]
teste4 = [1, 2, 3, 0]
teste5 = [9, 5, 10, 2, 24, -1, -48]

print(adjacentElementsProduct(teste1))
print(adjacentElementsProduct(teste2))
print(adjacentElementsProduct(teste3))
print(adjacentElementsProduct(teste4))
print(adjacentElementsProduct(teste5))
