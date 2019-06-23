def getInput():
    #variaveis
    numeros = []
    entrada = 0

    try:
        #ação
        while True:
            entrada = int(input('> '))
            if entrada == 999:
                break

            numeros.append(entrada)

        print('Processando....')

    except ValueError:
        print('Invalido!')

    return numeros

def helper():
    lin()
    print('''
    Digite a operação desejada:
        +: soma
        -: subtração
        *: multiplicação
        /: divisão
        **: potenciação 
        exit: to exit program
    ''')
    lin()

def title(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

def lin(lin=40):
    print(f'-' * lin) 
    