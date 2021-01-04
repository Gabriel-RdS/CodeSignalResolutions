def addTwoDigits(n):
    s = 0
    while n:
        s += n % 10  # Soma `s` ao ultimo numeral de `n`
        n //= 10  # Remove o ultimo numero de `n`
    return s


print(addTwoDigits(2209))
