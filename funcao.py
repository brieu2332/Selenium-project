def somar_lista(qualquercoisa):
    somaTotal = 0
    for numero in qualquercoisa:
        somaTotal += numero
    
    return somaTotal

def main():
    lista_valores = [1, 2, 3, 4, 5]
    soma = somar_lista(lista_valores)
    print('a soma sera: {}'.format(soma))

main()