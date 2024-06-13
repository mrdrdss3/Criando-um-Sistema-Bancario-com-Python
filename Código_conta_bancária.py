# Descrição/Pontos a serem abordados: 
# - Depósitos devem ser armazenados em uma variável(valores positivos somente) *
# - 3 saques diários com o limite máximo de 500 reais por saque *
# - Se não tiver saldo imprimir que não é possível sacar *
# - Todos os saques devem ser armazenados em uma variável e exibidos no extrato *
# - Extrato -> Lista todos os depósitos e saques realizados na conta *
# - Imprimir no formato R$ xxxx.xx * 


menu = """
===== MENU =====

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

-> """

saldo = 0
limite = 500
extrato = f"""
                ===== EXTRATO ===== 
                """
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor_deposito = float(input("Indique o valor que deseja depositar: "))

        if valor_deposito < 0:
            print("O valor para o depósito deve ser maior que zero(0).")

        else:
            saldo += valor_deposito
            extrato += f"""
            Você realizou um depósito de: R$ {valor_deposito:.2f}

            Saldo: R$ {saldo: .2f}
            """
    
    elif opcao == "s":

        valor_saque = float(input("Informe quanto deseja sacar: "))

        if valor_saque > limite or valor_saque < 0:
            print("O limite de saque é de R$ 500.")

        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Você não pode mais realizar saques. O limite diário de saques é igual a 3.")
            
            else: 

                if saldo >= valor_saque:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"""
            Você realizou um saque de: R$ {valor_saque:.2f}
            Você pode realizar {3 - numero_saques} saques. 
                    
            Saldo: R$ {saldo: .2f} 
            """

                else:
                    print("Você não tem saldo o suficiente para realizar esse saque.")

    elif opcao == "e":
        print(extrato)
    
    elif opcao == "q":
        break

    else:
        print("OPÇÃO INVÁLIDA. Selecione uma opção presente no menu")





