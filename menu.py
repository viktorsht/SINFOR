def menu():
    while True:
        try:
            opcao = int(input('\n\t BEM-VINDO!\nSistema de Imunização contra Covid-19\n\tUBS: Ipueiras\n'
                              '[01] - Cadastrar\n'
                              '[02] - Relatórios\n'
                              '[03] - Imprimir dados\n'
                              '[04] - Vacinar 1ª dose\n'
                              '[05] - Vacinar 2ª dose\n'
                              '[06] - Sair\n'))
            if opcao >= 1 and opcao <= 6:
                return opcao
        except ValueError:
            print('Digite um valor inteiro')

def menu_cadastrar():
    while True:
        try:
            opcao = int(input('\n\t CADASTRAR \n'
                              '[01] - Servidor\n'
                              '[02] - Comunitário\n'
                              '[03] - Vacina (Lab)\n'
                              '[04] - Lote de Vacina\n'
                              '[05] - Condição de Priridade\n'
                              '[06] - Sair\n'))
            if opcao >= 1 and opcao <= 6:
                return opcao
        except ValueError:
            print('Digite um valor inteiro')

def menu_relatorios():
    while True:
        try:
            opcao = int(input('\n\t BEM-VINDO!\nSistema de Imunização contra Covid-19\n\tUBS: Ipueiras\n'
                              'Impressão de Relatórios\n'
                              '[01] - Total de vacinados com a 1ª Dose\n'
                              '[02] - Total de vacinados com a 2ª Dose\n'
                              '[03] - Quantidade de vacinados por tipo de vacina\n'
                              '[04] - Quantidade Total de Vacinas\n'
                              '[05] - Quantidade de Vacinas por tipo\n'
                              '[06] - Sair\n'))
            if opcao >= 1 or opcao <= 6:
                return opcao
        except ValueError:
            print("Digite um valor inteiro")


def menu_imprimir_objeto():
    while True:
        try:
            opcao = int(input('\n\t BEM-VINDO!\nSistema de Imunização contra Covid-19\n\tUBS: Ipueiras\n'
                              'Impressão todos os objetos\n'
                              '[01] - Imprimir Comunitários\n'
                              '[02] - Imprimir Servidores\n'
                              '[03] - Imprimir Vacinas (Lab)\n'
                              '[04] - Imprimir Lotes de Vacina\n'
                              '[05] - Sair\n'))
            if opcao >= 1 and opcao <= 5:
                return opcao
        except ValueError:
            print("Digite um valor inteiro")
