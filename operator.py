import operator

def somas(*numbers):
    for number in numbers:
        result = sum(number)
    return result

def sub(numeros):
    # algoritmo: pegar o numero index e segundo numero de uma lista
    # ???
    subtracao = 0
    for numero in numeros:
        subtracao -= numero
    return subtracao

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