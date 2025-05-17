def line(size = 42):
    """
    Returns a line of dashes of a given size.
    :param size: The size of the line.
    :return: A string of dashes of the given size.
    """
    return "-" * size

def header(text):
    """
    Prints a header with a given text.
    :param text: The text to be printed as a header.
    """
    print(line())
    print(text.center(42))
    print(line())

def menu(list):
    '''
    Prints a menu with a list of options.
    :param list: A list of options to be printed in the menu.
    :return: The option chosen by the user.
    '''
    header('MENU')
    c = 1
    for item in list:
        print(f'[{c}] {item}')
        c += 1
    print(line())
    option = readInt('Sua opção: ')
    return option

def readFloat(msg):
    """
    Reads a float from the user.
    :param msg: The message to be displayed to the user.
    :return: The float entered by the user.
    """
    while True:
        value = str(input(msg)).replace(',', '.').strip()
        if value.isalpha() or value == '':
            print(f'\033[0;31mERRO! "{value}" é um preço inválido.\033[m')
        else:
            return float(value)

def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu parar o programa!\033[m')
            return 0
        else:
            return n

def errorMessage(msg):
    """
    Prints an error message.
    :param msg: The error message to be printed.
    """
    print(f'\033[0;31m{msg}\033[m')

def successMessage(msg):
    """
    Prints a success message.
    :param msg: The success message to be printed.
    """
    print(f'\033[0;32m{msg}\033[m')

def warningMessage(msg):
    """
    Prints a warning message.
    :param msg: The warning message to be printed.
    """
    print(f'\033[0;33m{msg}\033[m')