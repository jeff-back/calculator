import operator


def somas(*numbers):
    for number in numbers:
        result = sum(number)
    return result


def sub():
    # algoritmo: pegar o numero index e segundo numero de uma lista
    # ???
    numero = []
    numero.append(int(input('1º numero: ')))
    numero.append(int(input('2º numero: ')))
    
    subtração = numero[0] - numero[1]
    return subtração


def multi(valores):
    multiplication = 1
    for num in valores:
        multiplication *= num
    return multiplication


def div(valores):
    division = 1
    for num in valores:
        division /= num
    return division


def potent():
    valor = int(input('Numero: '))
    potencia = int(input('Potencia: '))

    potentiation = valor ** potencia
    return potentiation
    