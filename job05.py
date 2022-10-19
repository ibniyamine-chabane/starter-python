value1 = int(input('valeur 1 : '))
value2 = int(input('valeur 2 : '))
if value1 < value2:
    for x in range(value1+1, value2):
        print(x)
elif value1 > value2:
    for x in range(value1-1, value2,-1):
        print(x)
else:
    print('Valeurs égales')