import lib.interface as interface

interface.header('Coffee Shops Tia Rosa')

while True:
    response = interface.menu(['PEDIDOS', 'CARDÁPIO', 'CLIENTES' ,'SAIR'])
    if response == 1:
        interface.header('CADASTRAR NOVO PEDIDO')
        while True:
            response = interface.menu(['Novo Pedido', 'Listar Pedidos', 'Atender Pedido' ,'Voltar'])
            if response == 1:
                print('Novo Pedido')
            elif response == 2:
                print('Listar Pedidos')
            elif response == 3:
                print('Atender Pedido')
            elif response == 4:
                print('Voltar')
                break
    elif response == 2:
        print('Listar')
    elif response == 3:
        print('Atender')
    elif response == 4:
        print('Sair')
        break
    else:
        print('Opção inválida. Tente novamente.')