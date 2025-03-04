n = -1
def numSign(n):
    if n > 0:
        print('Il numero è positivo.')
    elif n < 0:
        print('Il numero è negativo.')
    else:
        print('il numero è zero.')
numSign(n)

x = input('Inserisci la tua età: ')

if int(x) > 10:
    print('Il prezzo del biglietto è 10 euro')
else:
    print('Il prezzo del biglietto è 5 euro')
