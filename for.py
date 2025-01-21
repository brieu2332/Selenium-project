numero_inteiro = int(10)

numero_inteiro = 20

numero_inteiro *= numero_inteiro

numero_inteiro_2 = int(5)

varios_numeros = [1,2,3]#variavel tipo lista

#for, i que ira percorrer e repetir toda variavel varios_numeros que nele tem 1 2 3, print que mostra esse esse i
for i in varios_numeros:
    print(i)
print("-----------print de separação----------")


#range vai de n até -1n
for i in range(0, numero_inteiro_2, 1): # (1°, é o inicio(opcional)) (2°, é o fim(obrigatotio)) (3°, O intervalo entre os números da sequência padrão é 1 (opcional))
    print(i)
print("-----------print de separação----------")
    
for i in range(5, 0, -1):
    print(i)
print("-----------print de separação----------")


##### MAIN
print('--main--')
print(numero_inteiro)
print(type(numero_inteiro))
