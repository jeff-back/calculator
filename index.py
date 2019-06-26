from operator import somas, multi, sub, div
from model import getInput, helper, title, lin
from time import sleep

title('Calculadora')
print('aguarde...')
sleep(1)

while True:
    #processo
    title('Cl menu')
    helper()
    opcao = str(input('=> '))
    if opcao == '+':
        #inputs
        print('> Numeros: (999 para sair) ')
        numeros = getInput()

        #processo
        resultado = somas(numeros)
        sleep(2)

    elif opcao == '-':
        #inputs
        print('> Numeros: (999 para sair) ')
        numeros = getInput()

        #processo
        resultado = sub(numeros)
        sleep(2)

    elif opcao == '*':
        #inputs
        print('> Numeros: (999 para sair) ')
        numeros = getInput()

        #processo
        resultado = multi(numeros)
        sleep(2)

    elif opcao == '/':
        #inputs
        print('> Numeros: (999 para sair) ')
        numeros = getInput()

        #processo
        resultado = div(numeros)
        sleep(2)

    elif opcao == '--help':
        helper()
    
    elif opcao == 'exit':
        exit()

    #output
    print(f'Resultado: {resultado}')
    lin()
    sleep(3)
    