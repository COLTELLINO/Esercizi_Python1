for x in range(10): 
    print (x + 1)

list = [1,2,3,4,5]
print('Lista: ', list)
def sum(list):
    sum = 0
    for x in list:
       sum += x
    return sum
print('Somma: ', sum(list))

for x in range(10):
    output = []
    for y in range(10):
        output.append((x+1)*(y+1))
    print(output)
