from random import sample

moje_liczby = [7, 11, 13, 23, 33, 45]

Totek_liczby = range(1, 50)

wylosowane_liczby = []
counter = 0

while wylosowane_liczby != moje_liczby:
    wylosowane_liczby = sample(Totek_liczby, 6)
    counter =+ 1

print(counter)    
 #   if moje_liczby == wylosowane_liczby:
  #      print('wygrałeś')
   # else:
    #    print('graj dalej')

print(wylosowane_liczby)


