def menu():
    print( """
    ===== MENU =====

    [d] Depósito
    [s] Saque
    [e] Extrato
    [u] Cadastrar usuário
    [c] Criar conta
    [l] Listar contas
    [q] Sair

    -> """)
    opcao = input("Digite a opção desejada: ")
    return opcao

def cadastrar_usuário(*,usuarios):
    cpf = str(input("Digite seu CPF(Apenas os números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já foi cadastrado!")
        return

    nome = str(input("Digite seu nome: "))
    data_nascimento = str(input("Digite sua data de nascimento: "))
    endereco = str(input("Digite seu endereço(logradouro, nro - bairro - cidade/sigla estado): "))

    informacoes = {"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco" : endereco}
    usuarios.append(informacoes)

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios, /):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def conta_corrente(NUMERO_AGENCIA, numero_conta, usuarios,/):
    cpf = str(input("Digite seu CPF(Apenas os números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Sua conta foi criada com sucesso!")
        return {"numero_agencia": NUMERO_AGENCIA, "numero_conta": numero_conta, "usuario" : usuario}

    print("Usuário não encontrado.")

def listar_contas(contas, /):
    for conta in contas:
        linha = f''' CONTAS
        =============================================
            Agência: {conta["numero_agencia"]}
            Número da conta: {conta["numero_conta"]}
            Usuário: {conta["usuario"]["nome"]}
        =============================================
        '''
        print(linha)

def depositar(saldo, extrato, /):
    valor_deposito = float(input("Indique o valor que deseja depositar: "))

    if valor_deposito < 0:
        print("O valor para o depósito deve ser maior que zero(0).")

    else:
        saldo += valor_deposito
        extrato += f"""
        Você realizou um depósito de: R$ {valor_deposito:.2f}

        Saldo: R$ {saldo: .2f}
        """
    return saldo, extrato

def sacar(*,saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
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

    return saldo, extrato, numero_saques

def exibir_extrato(*, extrato):
    return extrato

def main():

    saldo = 0
    limite = 500
    extrato = f"""
        ===== EXTRATO ===== 
                    """
    numero_saques = 0
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"
    numero_conta = 0
    contas = []
    usuarios = []

    while True:

        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
            print("Seu saldo é de :",saldo)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo = saldo, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES, extrato = extrato)
            print("Seu saldo é de :",saldo)

        elif opcao == "e":
            extrato = exibir_extrato(extrato = extrato)
            print(extrato)

        elif opcao == "c":
            numero_conta += 1
            conta = conta_corrente(NUMERO_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas) 

        elif opcao == "u":
            cadastrar_usuário(usuarios = usuarios)

        elif opcao == "q":
            break

        else:
            print("OPÇÃO INVÁLIDA. Selecione uma opção presente no menu")

main()
