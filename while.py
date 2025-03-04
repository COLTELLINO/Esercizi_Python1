def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact = i * fact
        i += 1
    return fact
print('Fattoriale: ', factorial(5))

i = 0
while i <= 98:
    i += 2
    print(i)
