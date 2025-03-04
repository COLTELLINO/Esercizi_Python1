s = 'Daniel'
print('Stringa: ', s)

def contaVocali(s):
    counter = 0
    for lettera in s:
        if lettera in 'aeiou':
            counter += 1
    return counter
print('Numero Vocali: ', contaVocali(s))

def isPalindrome(s):
    if s == ''.join(reversed(s)):
        print('è un palindromo')
    else:
        print('non è un palindromo')
isPalindrome('ciaoaic')

stringa = input('Inserire stringa: ')
caps = int(input('digita 1 per convertire in maiuscolo, 2 per convertire in minuscolo'))

if caps == 1:
    print(stringa.upper())
elif caps == 2:
    print(stringa.lower())
else:
    print('Stringa o valore caps non valido!')
