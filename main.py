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

while True:
    interface.clearScreen()
    interface.header('Coffee Shops Tia Rosa')
    response = interface.menu(['PEDIDOS', 'CARDÁPIO', 'CLIENTES' ,'SAIR'])
    if response == 1:
        interface.clearScreen()
        interface.header('PEDIDOS')
        while True:
            response = interface.menu(['Novo Pedido', 'Listar todos os Pedidos', 'Listar Pedidos Pendentes', 'Atender Pedido' ,'Voltar'])
            if response == 1:
                interface.clearScreen()
                interface.header('NOVO PEDIDO')
                customerName = input('Nome do cliente: ')
                order = input('Pedido: ')
                price = interface.readFloat('Preço: R$ ')
                archive.addOrder(archiveOrder, customerName, order, price)
            elif response == 2:
                interface.clearScreen()
                interface.header('LISTA DE PEDIDOS')
                archive.listOrders(archiveOrder)
            elif response == 3:
                interface.clearScreen()
                interface.header('PEDIDOS PENDENTES')
                archive.listPendingOrders(archiveOrder)
            elif response == 4:
                interface.clearScreen()
                interface.header('ATENDER PEDIDO')
                archive.listPendingOrders(archiveOrder)
                print(interface.line())
                orderNumber = interface.readInt('\033[0;33mNúmero do pedido a ser atendido: \033[m')
                archive.executeOrder(archiveOrder, orderNumber)
            elif response == 5:
                interface.clearScreen()
                print(interface.line())
                interface.successMessage('Retornar ao menu principal')
                break
    elif response == 2:
        interface.clearScreen()
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
                itemNumber = int(input('\033[0;33mNúmero do item a ser desativado: \033[m'))
                archive.disableMenuItem(archiveMenu, itemNumber)
            if response == 4:
                print(interface.line())
                interface.successMessage('Retornar ao menu principal')
                break        
    elif response == 3:
        interface.clearScreen()
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
                interface.clearScreen()
                interface.header('LISTA DE CLIENTES')
                archive.listCustomers(archiveCustomer)
            elif response == 3:
                print(interface.line())
                interface.successMessage('Retornar ao menu principal')
                break
    elif response == 4:
        print(interface.line())
        interface.warningMessage('SAINDO... MUITO OBRIGADO!')
        break
    else:
        interface.errorMessage('Opção inválida. Tente novamente.')