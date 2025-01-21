a = int(input(''))
b = int(input(''))
c = int(input(''))
d = int(input(''))

soma1 = c + d
soma2 = a + b

if b > c:
    if d > a :
        if soma1 > soma2 :
            if a % 2 == 0:
                print('Valores aceitos')
else:
    print('Valores nao aceitos')