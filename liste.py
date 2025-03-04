list = [1,2,3,4,5]
print('Lista: ', list)

def evenOnly(list):
    l = list.copy()
    for x in l:
        if (x%2)==1:
            l.remove(x)
    return l
print('Numeri Pari: ', evenOnly(list))

def invertList(list):
    i = -1
    l = []
    while i >= len(list)*-1:
        l.append(list[i])
        i -= 1
    return l
print('Lista Invertita: ', invertList(list)) 

def minandmax(list):
    max = list[0]
    min = list[0]
    for x in list:
        if x > max: 
            max = x
        elif x < min: 
            min = x
    print('Min = ', min)
    print('Max = ', max)
minandmax(list)
