# input de horas minutos e segundos, output apenas de segundos.

def fun_segunds(horas, minutos, segundos):

    horas = (horas * 36000)
    minutos = (minutos * 60)
    total_segunds = (horas + minutos + segundos)

    return total_segunds, horas, minutos
    


def conversao_str(entrada_hora):
    #try pode dar erro a entrada de dados para a conversão
    try:
        #numero_string = hora
        numero_inteiro = entrada_hora.split(":") #converte string em int
        
        horas = int(numero_inteiro[0])
        minutos = int(numero_inteiro[1])
        segundos = int(numero_inteiro[2])

    except Exception as erro:
        print(f'DEU ERRO PAIZÃO!!!!!!!: {erro}')
        return None
    
    else:
        print('tipo hora', type(entrada_hora))
        print('tipo inteiro', type(numero_inteiro))
        print('horas tipo:', type(horas))
        print('seu numero inteiro:horas {}, minutos {}, segundos{}'.format( horas, minutos, segundos))
        print('--------------antes da conversao----------')
        total_segunds, minutos, horas = fun_segunds(horas, minutos, segundos)
        print('horas em segundos:',horas)
        print('minutos em horas',minutos)
        print('segundos',segundos)
        print('total de segundos:',total_segunds)


def main():
    entrada_hora = input('exemplo 24:30:10 \n qual a hora de agora ?:')
    conversao_str(entrada_hora)


main()