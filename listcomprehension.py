l = [x**2 for x in range(1,11)]
print(l)

dizionario = {x:x**2 for x in range(1,6)}
print(dizionario)

n = -1
def numSign(n):
    if n > 0:
        print('Il numero è positivo.')
    elif n < 0:
        print('Il numero è negativo.')
    else:
        print('il numero è zero.')
numSign(n)
