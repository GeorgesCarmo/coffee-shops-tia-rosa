import lib.interface as interface
import lib.archive as archive

archiveOrder = 'pedidos.txt'
archiveMenu = 'cardapio.txt'
archiveCustomer = 'clientes.txt'
if not archive.archiveExists(archiveOrder):
    archive.createArchive(archiveOrder)

if not archive.archiveExists(archiveMenu):
    archive.createArchive(archiveMenu)

if not archive.archiveExists(archiveCustomer):
    archive.createArchive(archiveCustomer)        

interface.header('Coffee Shops Tia Rosa')

while True:
    response = interface.menu(['PEDIDOS', 'CARDÁPIO', 'CLIENTES' ,'SAIR'])
    if response == 1:
        interface.header('PEDIDOS')
        while True:
            response = interface.menu(['Novo Pedido', 'Listar todos os Pedidos', 'Listar Pedidos Pendentes', 'Atender Pedido' ,'Voltar'])
            if response == 1:
                interface.header('NOVO PEDIDO')
                customerName = input('Nome do cliente: ')
                order = input('Pedido: ')
                price = interface.readFloat('Preço: R$ ')
                archive.addOrder(archiveOrder, customerName, order, price)
            elif response == 2:
                interface.header('LISTA DE PEDIDOS')
                archive.listOrders(archiveOrder)
            elif response == 3:
                interface.header('PEDIDOS PENDENTES')
                archive.listPendingOrders(archiveOrder)
            elif response == 4:
                interface.header('ATENDER PEDIDO')
                archive.listPendingOrders(archiveOrder)
                print(interface.line())
                orderNumber = interface.readInt('Número do pedido a ser atendido: ')
                archive.executeOrder(archiveOrder, orderNumber)
            elif response == 5:
                print('Voltar')
                break
    elif response == 2:
        interface.header('CARDÁPIO')
        while True:
            response = interface.menu(['Novo Item do Cardápio', 'Listar Itens do Cardápio', 'Desativar Item do Cardápio' ,'Voltar'])
            if response == 1:
                interface.header('NOVO ITEM')
                itemName = input('Nome do item: ')
                ingredients = input('Ingredientes: ')
                price = interface.readFloat('Preço: R$ ')
                archive.addMenuItem(archiveMenu, itemName, ingredients, price)
            if response == 2:
                interface.header('LISTA DE ITENS DO CARDÁPIO')
                archive.listMenu(archiveMenu)
            if response == 3:
                interface.header('DESATIVAR ITEM DO CARDÁPIO')
                archive.listMenu(archiveMenu)
                itemNumber = int(input('Número do item a ser desativado: '))
                archive.disableMenuItem(archiveMenu, itemNumber)
            if response == 4:
                print('Voltar')
                break        
    elif response == 3:
        interface.header('CLIENTES')
        while True:
            response = interface.menu(['Novo Cliente', 'Listar Clientes', 'Voltar'])
            if response == 1:
                interface.header('NOVO CLIENTE')
                customerName = input('Nome do cliente: ')
                customerEmail = input('Email do cliente: ')
                customerPhone = input('Telefone do cliente: ')
                customerAddress = input('Endereço do cliente: ')
                archive.addCustomer(archiveCustomer, customerName, customerEmail, customerPhone, customerAddress)
            elif response == 2:
                interface.header('LISTA DE CLIENTES')
                archive.listCustomers(archiveCustomer)
            elif response == 3:
                print('Voltar')
                break
    elif response == 4:
        print('Sair')
        break
    else:
        interface.errorMessage('Opção inválida. Tente novamente.')