x = float(input('input:'))

if x >= 0 and x <= 100 :
    if x >= 0 and x <= 25 :
        print('Intervalo [{}]'.format('0,25'))
    elif x > 25 and x <= 50 :
        print('Intervalo [{}]'.format('25,50'))
    elif x > 50 and x <= 75 :
        print('Intervalo [{}]'.format('50,75'))
    elif x > 75 and x <= 100 :
        print('Intervalo [{}]'.format('75,100'))
else :
    print('fora do intervalo')