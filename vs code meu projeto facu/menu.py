import cal
import fin

gastos = []

while True:
    print("=== MENU ===")
    print("1 - Calculadora")
    print("2 - Financeiro")
    print("0 - Sair")
    
    op = input("Escolha: ")
    
    if op == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        
        escolha = input("Operação: ")
        
        if escolha == "1":
            print("Resultado:", cal.somar(a, b))
        elif escolha == "2":
            print("Resultado:", cal.subtrair(a, b))
        elif escolha == "3":
            print("Resultado:", cal.multiplicar(a, b))
        elif escolha == "4":
            print("Resultado:", cal.dividir(a, b))
    
    elif op == "2":
        fin.financeiro(gastos)
    
    elif op == "0":
        print("Saindo...")
        break
