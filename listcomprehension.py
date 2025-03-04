l = [x**2 for x in range(1,11)]
print(l)

l1 = ['ciao', 'daniel', 'cielo', 'albero']
l2 = [x for x in l1 if x[0] == 'a']
print(l2)

dizionario = {x:x**2 for x in range(1,6)}
print(dizionario)
