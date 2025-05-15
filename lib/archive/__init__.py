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
    try:
        a = open(archiveName, 'at')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        try:
            a.write(f'{customerName};{order};{price}\n')
        except Exception as e:
            print(f'Erro ao escrever no arquivo: {e}')
        else:
            print('\033[32mPedido adicionado com sucesso!\033[m')
        finally:
            a.close()
    finally:
        a.close()

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
        for line in a:
            data = line.split(';')
            data[2] = data[2].replace('\n', '')
            print(f'{data[0]:<10}  {data[1]:<20}  R${data[2]}')
        a.close()
    finally:
        a.close()

def removeOrder(archiveName, order):
    '''
    Remove um pedido do arquivo
    :param archiveName: Nome do arquivo onde os pedidos estão armazenados
    :param order: Pedido a ser removido
    '''
    try:
        a = open(archiveName, 'rt')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        try:
            lines = a.readlines()
            a.close()
            a = open(archiveName, 'wt')
            for line in lines:
                if line.strip() != order:
                    a.write(line)
        except Exception as e:
            print(f'Erro ao remover o pedido: {e}')
        finally:
            a.close()
    finally:
        a.close()
