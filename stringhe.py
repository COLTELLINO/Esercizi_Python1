s = 'Daniel'
print('Stringa: ', s)

def contaVocali(s):
    counter = 0
    for lettera in s:
        if lettera in 'aeiou':
            counter += 1
    return counter
print('Numero Vocali: ', contaVocali(s))
