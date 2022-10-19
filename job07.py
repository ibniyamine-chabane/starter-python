

for nbre in range(0,100):
    if nbre % 3 == 0 and nbre % 5 != 0:
        print('Fizz')
    elif nbre % 3 != 0 and nbre % 5 == 0:
        print("Buzz")
    elif nbre % 3 == 0 and nbre % 5 == 0:
        print("FizzBuzz")
    else:
        print(nbre)