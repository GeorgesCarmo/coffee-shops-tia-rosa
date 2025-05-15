import lib.interface as interface
import lib.archive as archive

archiveName = 'pedidos.txt'
if not archive.archiveExists(archiveName):
    archive.createArchive(archiveName)

interface.header('Coffee Shops Tia Rosa')

while True:
    response = interface.menu(['PEDIDOS', 'CARDÁPIO', 'CLIENTES' ,'SAIR'])
    if response == 1:
        interface.header('PEDIDOS')
        while True:
            response = interface.menu(['Novo Pedido', 'Listar Pedidos', 'Atender Pedido' ,'Voltar'])
            if response == 1:
                interface.header('NOVO PEDIDO')
                customerName = input('Nome do cliente: ')
                order = input('Pedido: ')
                price = interface.readFloat('Preço: R$ ')
                archive.addOrder(archiveName, customerName, order, price)
            elif response == 2:
                interface.header('LISTA DE PEDIDOS')
                archive.listOrders(archiveName)
            elif response == 3:
                print('Atender Pedido')
            elif response == 4:
                print('Voltar')
                break
    elif response == 2:
        response = interface.menu(['Novo Item', 'Listar Itens', 'Deletar Item' ,'Voltar'])
        if response == 1:
            interface.header('NOVO ITEM')
        if response == 2:
            interface.header('LISTA DE ITENS DO CARDÁPIO')
        if response == 3:
            interface.header('DELETAR ITEM DO CARDÁPIO')
        if response == 4:
            print('Voltar')
            break        
    elif response == 3:
        print('Clientes')
    elif response == 4:
        print('Sair')
        break
    else:
        print('Opção inválida. Tente novamente.')