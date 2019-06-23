import operator

def somas(*numbers):
    for number in numbers:
        result = sum(number)
    return result


def multi(valores):
    multiplication = 1
    for num in valores:
        multiplication *= num
    #print(f'A multiplicação de {num} é de {multiplication}')
    return multiplication