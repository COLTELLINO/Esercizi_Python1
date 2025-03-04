dizionario = {'albero':'tree','faccia':'face','pavimento':'floor','sedia':'chair'}
x = input('Inserisci parola da tradurre')
if x in dizionario:
    print('Traduzione = ', dizionario.get(x))
else:
    print('Parola sconosciuta')

def controlloParola(dizionario, key):
    if key in dizionario:
        return True
    else:
        return False
controlloParola(dizionario, 'albero')
