"""
Link: https://app.codesignal.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr
"""


def maxMultiple(divisor, bound):
    multiplicador = 2
    resultado = 0
    while resultado < bound:
        resultado = divisor * multiplicador
        multiplicador += 1
        if resultado > bound:
            return resultado - divisor
    return resultado


def maxMultiple2(divisor, bound):
    return bound - (bound % divisor)

# Teste
print(maxMultiple(7, 20))
