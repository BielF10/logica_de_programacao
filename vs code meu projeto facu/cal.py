def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"def calculadora(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
