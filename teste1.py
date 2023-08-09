def menu():
    print('Selecione uma opção:')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Exibir extrato')
    print('4. Criar usuário')
    print('5. Filtrar usuário')
    print('6. Criar conta')
    print('7. Listar contas')
    print('8. Sair')
 

    option = int(input('Digite sua opção: '))

    if option == 1:
        saldo = float(input('seja bem vindo, digite sua opção novamente: '))
        valor = float(input('Digite o valor a ser depositado: '))
        extrato = []
        depositar(saldo, valor, extrato)
    elif option == 2:
        saldo = float(input('seja bem vindo, digite sua opção novamente: '))
        valor = float(input('Digite o valor a ser sacado: '))
        extrato = []
        limite = 1000
        numero_saques = 0
        limite_saques = 5
        sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
    elif option == 3:
        saldos = []
        extratos = []
        saldo = float(input('Digite o saldo atual: '))

        while True:
            valor = float(input('Digite o valor a ser adicionado ao extrato (digite 0 para finalizar): '))
            if valor == 0:
                break
            extratos.append(valor)
            saldo += valor
            saldos.append(saldo)

        exibir_extratos(saldos, extratos)
    elif option == 4:
        usuarios = []
        criar_usuario(usuarios)
    elif option == 5:
        usuarios = []
        cpf = input('Digite o CPF a ser filtrado: ')
        filtrar_usuario(cpf, usuarios)
    elif option == 6:
        usuarios = []
        contas = []
        agencia = input('Digite a agência da conta: ')
        numero_conta = input('Digite o número da conta: ')
        criar_contas(agencia, numero_conta, usuarios)
    elif option == 7:
        contas = []
        listar_contas(contas)
    elif option == 8:
        return
    else:
        print('Opção inválida.')
        menu()

def depositar(saldo, valor, extrato):
    if saldo < valor:
        print('Saldo insuficiente.')
        return

    saldo += valor
    extrato.append((saldo, valor))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo < valor:
        print('Saldo insuficiente.')
        return

    if numero_saques >= limite_saques:
        print('Limite de saques excedido.')
        return

    saldo -= valor
    extrato.append((saldo, valor))

def exibir_extratos(saldos, extratos):
    for saldo, valor in zip(saldos, extratos):
        print(f'Saldo: {saldo}, Valor: {valor}')

def criar_usuario(usuarios):
    nome = input('Digite o nome do usuário: ')
    cpf = input('Digite o CPF do usuário: ')
    email = input('Digite o e-mail do usuário: ')
    senha = input('Digite a senha do usuário: ')

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'senha': senha,
        'contas': [],
    })

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

    return None

def criar_contas(agencia, numero_conta, usuarios):
    cpf = input('Digite o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario is None:
        print('Usuário não encontrado.')
        return

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'saldo': 0,
        'extrato': [],
    }

    usuario['contas'].append(conta)

def listar_contas(contas):
    for conta in contas:
        print(f'Agência: {conta["agencia"]}, Número da conta: {conta["numero_conta"]}, Saldo: {conta["saldo"]}')

def main():
    while True:
        menu()
        if option == 8:
            break

option = None
main()