def financeiro(gastos):
    print("\n--- FINANCEIRO ---")
    
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    
    opçao = input("Escolha: ")
    
    if opçao == "1":
        nome = input("Nome do gasto: ")
        valor = float(input("Valor: "))
        gastos.append((nome, valor))
        
    elif opçao == "2":
        total = 0
        
        for nome, valor in gastos:
            print(nome, "-", valor)
            total += valor
        
        print("Total:", total)