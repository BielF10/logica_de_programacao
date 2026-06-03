import cal
import fin

while True:
    print("\n1 - Calculadora")
    print("2 - Financeiro")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print("1 - Somar")
        print("2 - Subtrair")
        escolha = input("Operação: ")

        if escolha == "1":
            print(cal.somar(a, b))
        elif escolha == "2":
            print(cal.subtrair(a, b))

    elif op == "2":
        print("1 - Adicionar dinheiro")
        print("2 - Retirar dinheiro")
        print("3 - Ver saldo")

        escolha = input("Escolha: ")

        if escolha == "1":
            valor = float(input("Valor: "))
            fin.financeiro.adicionar(valor)

        elif escolha == "2":
            valor = float(input("Valor: "))
            fin.financeiro.retirar(valor)

        elif escolha == "3":
            print("Saldo:", fin.ver_saldo())

    elif op == "0":
        break