from random import sample

moje_liczby = [7, 11, 23, 33, 39,45]

Totek_liczby = range(1, 50)

wylosowane_liczby = []
counter = 0
#print(counter)

while wylosowane_liczby != moje_liczby:
    wylosowane_liczby = sample(Totek_liczby, 3)
    counter += 1

#print(counter)    
print(wylosowane_liczby)

print('Wygrałbyś szóstkę za ' + str(counter) + ' razem')


