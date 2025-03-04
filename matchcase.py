x = int(input('Inserisci un numero tra 0 e 5: '))

if (x <= 5 and x >= 0):
    match x:
        case '0':
            print('zero')
        case '1':
            print('uno')
        case '2':
            print('due')
        case '3':
            print('tre')
        case '4':
            print('quattro')
        case '5':
            print('cinque')
else:
    print('numero non valido!')
