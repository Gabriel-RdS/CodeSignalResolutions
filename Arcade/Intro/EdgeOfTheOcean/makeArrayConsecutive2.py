"""
Link: https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
"""


def makeArrayConsecutive2(statues):
    validacao = 0
    ordemCrescente = sorted(statues)

    for n in range(1, len(statues)):
        j = n - 1
        if ordemCrescente[n] - ordemCrescente[j] == 1:
            validacao += 0
        else:
            validacao += (ordemCrescente[j] - ordemCrescente[n]) + 1
    if validacao == 0:
        return validacao
    else:
        return abs(validacao)


def makeArrayConsecutive3(statues):
    return max(statues) - min(statues) - len(statues) + 1


array = [6, 2, 3, 8]
array2 = [4, 2, 7, 18]
print(makeArrayConsecutive2(array2))

