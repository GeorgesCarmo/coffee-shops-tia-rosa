
def archiveExists(archiveName):
    '''
    Verifica se o arquivo existe
    :param archiveName: Nome do arquivo a ser verificado
    :return: True se o arquivo existe, False caso contrário
    '''
    try:
        a = open(archiveName, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArchive(archiveName):
    ''' 
    Cria um novo arquivo
    :param archiveName: Nome do arquivo a ser criado
    '''
    try:
        a = open(archiveName, 'wt+')
        a.close()
    except Exception as e:
        print(f'Erro ao criar o arquivo: {e}')
    else:
        print(f'Arquivo {archiveName} criado com sucesso!')

def addOrder(archiveName, customerName, order, price):
    '''
    Adiciona um novo pedido ao arquivo
    :param archiveName: Nome do arquivo onde o pedido será adicionado
    :param customerName: Nome do cliente
    :param order: Pedido do cliente
    :param price: Preço do pedido
    '''
    newOrder = f'{customerName};{order};{price};PENDENTE\n'
    with open(archiveName, 'r') as f:
        linhas = f.readlines()

    for i in range(len(linhas)):
        if linhas[i].startswith("---"):
            linhas[i] = newOrder
            break
    else:
        # Nenhuma linha "vazia", adiciona no final
        linhas.append(newOrder)

    with open(archiveName, 'w') as f:
        f.writelines(linhas)

    print("Pedido adicionado com sucesso.")

def listOrders(archiveName):
    '''
    Lista os pedidos do arquivo
    :param archiveName: Nome do arquivo onde os pedidos estão armazenados
    '''
    try:
        a = open(archiveName, 'rt')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        c = 0
        for line in a:
            data = line.split(';')
            data[2] = data[2].replace('\n', '')
            print(f'{c} - {data[0]:<10}  {data[1]:<15}  R${data[2]:<4} -> {data[3]}')
            c += 1
        a.close()
    finally:
        a.close()

def listPendingOrders(archiveName):
    '''
    Lista os pedidos pendentes do arquivo
    :param archiveName: Nome do arquivo onde os pedidos estão armazenados
    '''
    with open(archiveName, 'r') as f:
        linhas = f.readlines()

    for i, linha in enumerate(linhas):
        dados = linha.strip().split(";")
        if len(dados) >= 4 and dados[3] == "PENDENTE":
            print(f"N. pedido: {i} - {dados[0]:<10}  {dados[1]:<15}  R${dados[2]:<4} -> {dados[3]}")

def executeOrder(archiveName, index):
    '''
    Remove um pedido do arquivo
    :param archiveName: Nome do arquivo onde os pedidos estão armazenados
    :param order: Pedido a ser removido
    '''
    with open(archiveName, 'r') as f:
        linhas = f.readlines()

    if index < 0 or index >= len(linhas):
        print("Índice fora do intervalo do arquivo.")
        return

    dados = linhas[index].strip().split(";")
    if len(dados) < 4:
        dados.append("ATENDIDO")
    else:
        dados[3] = "ATENDIDO"

    linhas[index] = ";".join(dados) + "\n"

    with open(archiveName, 'w') as f:
        f.writelines(linhas)

    print(f"Pedido da linha {index} marcado como ATENDIDO.")

def addMenuItem(archiveName, itemName, ingredients, price):
    '''
    Adiciona um novo item ao cardápio
    :param archiveName: Nome do arquivo onde o item será adicionado
    :param itemName: Nome do item
    :param ingredients: Ingredientes do item
    :param price: Preço do item
    '''
    newItem = f'{itemName};{ingredients};{price};DISPONIVEL\n'
    with open(archiveName, 'a') as f:
        f.write(newItem)
    print("Item adicionado ao cardápio com sucesso.")

def listMenu(archiveName):
    '''
    Lista os itens do cardápio
    :param archiveName: Nome do arquivo onde os itens estão armazenados
    '''
    try:
        a = open(archiveName, 'rt')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        c = 0
        for line in a:
            data = line.split(';')
            data[2] = data[2].replace('\n', '')
            print(f'{c} - {data[0]:<15}  {data[1]:<50}  R${data[2]:<5} -> {data[3]}')
            c += 1
        a.close()
    finally:
        a.close()

def disableMenuItem(archiveName, index):
    '''
    Desativa um item do cardápio
    :param archiveName: Nome do arquivo onde o item será desativado
    :param index: Índice do item a ser desativado
    '''
    with open(archiveName, 'r') as f:
        linhas = f.readlines()

    if index < 0 or index >= len(linhas):
        print("Índice fora do intervalo do arquivo.")
        return

    dados = linhas[index].strip().split(";")
    if len(dados) < 4:
        dados.append("INDISPONIVEL")
    else:
        dados[3] = "INDISPONIVEL"

    linhas[index] = ";".join(dados) + "\n"

    with open(archiveName, 'w') as f:
        f.writelines(linhas)

    print(f"Item da linha {index} marcado como INDISPONIVEL.")

def addCustomer(archiveName, customerName, customerEmail, customerPhone, customerAddress):
    '''
    Adiciona um novo cliente ao arquivo
    :param archiveName: Nome do arquivo onde o cliente será adicionado
    :param customerName: Nome do cliente
    :param customerEmail: Email do cliente
    :param customerPhone: Telefone do cliente
    :param customerAddress: Endereço do cliente
    '''
    newCustomer = f'{customerName};{customerEmail};{customerPhone};{customerAddress}\n'
    with open(archiveName, 'a') as f:
        f.write(newCustomer)
    print(f'Cliente {customerName} adicionado com sucesso!') 

def listCustomers(archiveName):
    '''
    Lista os clientes do arquivo
    :param archiveName: Nome do arquivo onde os clientes são armazenados
    '''
    try:
        a = open(archiveName, 'rt')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        c = 0
        for line in a:
            data = line.split(';')
            data[3] = data[3].replace('\n', '')
            print(f'{c} - {data[0]:<15}  {data[1]:<30}  {data[2]:<15}  {data[3]}')
            c += 1
        a.close()
    finally:
        a.close()
