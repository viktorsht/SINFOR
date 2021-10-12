from comunitario import Comunitario
from autorizacao import Autorizacao
from ubs import UBS
from servidor import Servidor
from menu import *

def carregar_dados():
    ubs._lista_prioridade.append('Saúde')
    ubs._lista_prioridade.append('Transporte')
    ubs._lista_prioridade.append('Pressão Alta')
    ubs._lista_prioridade.append('Gravidez')
    ubs._lista_prioridade.append('Diabetes')

    ubs.add_comunitario('Eva', '1', '23/02/1985', '111111111111111')
    ubs.add_comunitario('Luana', '4', '20/10/1980', '444444444444444')
    ubs.add_comunitario('Almeida', '5', '03/02/2010', '555555555555555')
    ubs.add_comunitario('Silva', '6', '09/09/1983', '666666666666666')
    ubs.add_comunitario('Heitor', '3', '09/11/2016', '333333333333333')
    ubs.add_servidor('Júlia', '2', '09/04/1990', '222222222222222', 'auxiliar', 'Administração')

    ubs.add_servidor('João', '7', '09/04/1990', '777777777777777', 'enfermeira', 'Recursos Humanos')
    ubs.add_servidor('Marina', '8', '09/04/1990', '888888888888888', 'médica', 'Saúde')
    ubs.add_servidor('Pedro', '9', '09/04/1990', '999999999999999', 'cozinheiro', 'Educação')

    ubs.add_vacina_lab('Jansen', 'Jhonson')
    ubs.add_vacina_lab('Coronavac', 'Butantan/Sinovac', 1, 15, 30)
    ubs.add_lote_vacina('Coronavac', 'ABC123', '22/02/2021', '22/10/2021', 100)
    print('\n\tPRIORIDADES: ', ubs._lista_prioridade)

def vacinar_1dose():
    cpf = input('CPF: ')
    lote = input('Lote: ')
    if ubs.existe_lote(lote):
        if ubs.existe_comunitario(cpf) or ubs.existe_servidor(cpf):
            ubs.vacinar_1dose(cpf, lote)
            if ubs._lote_vacina[lote]._qtd == 0:
                ubs.remover_lote(lote)
        else:
            print('Pessoa não cadastrada!')
    else:
        print('Lote não cadastrado!')

def vacinar_2dose():
    cpf = input('CPF: ')
    lote = input('Lote: ')
    if ubs.existe_lote(lote):
        if ubs.existe_comunitario(cpf) or ubs.existe_servidor(cpf):
            ubs.vacinar_2dose(cpf, lote)
            if ubs._lote_vacina[lote]._qtd == 0:
                ubs.remover_lote(lote)
        else:
            print('Pessoa não cadastrada!')
    else:
        print('Lote não cadastrado!')

def imprimir():

    op = menu_imprimir_objeto()
    if op == 1:
        ubs.imprimir_td_comunitario()
    elif op == 2:
        ubs.imprimir_td_servidor()
    elif op == 3:
        ubs.imprimir_td_vacina()
    elif op == 4:
        ubs.imprimir_td_lote()

def gerar_relatorios():

    op = menu_relatorios()
    if op == 1:
        print('Total: ', len(ubs._vacinados_1dose))
        ubs.imprimir_relatorio_1dose()
    elif op == 2:
        print ('Total: ', len(ubs._vacinados_2dose))
        ubs.imprimir_relatorio_2dose()
    elif op == 3:
        vacina = input('Vacina: ')
        if ubs.existe_vacina(vacina):
            print('Total: ', ubs.vacinados_tipo(vacina))
        else:
            print('Vacina não cadastrada!')
    elif op == 4:
        print('total: ', ubs.total_vacinas())
        ubs.imprimir_relatorio_vacina()
    elif op == 5:
        vacina = input('Vacina: ')
        if ubs.existe_vacina(vacina):
            print('total: ', ubs.qtd_tipo_vacina(vacina))
        print('Vacina não cadastrada!')

def cadastrar():
    op = menu_cadastrar()
    if op == 1:
        cpf = input('CPF: ')
        try:
            if not ubs.existe_servidor(cpf):
                nome = input('Nome: ')
                nasc = input('Nasc: ')
                sus = input('sus: ')
                alocacao = input('Alocado em: ')
                ocupacao = input('Ocopação: ')
                cond = int(input('Possui condição pré-existente? 1 - Sim ou 0 Não: '))
                if cond:
                    condicao = input('Qual: ')
                    servidor = Servidor(nome, cpf, nasc, sus, ocupacao, alocacao, condicao)
                    try:
                        if isinstance(servidor, Autorizacao):
                            ubs.add_servidor(nome, cpf, nasc, sus, ocupacao, alocacao, condicao)
                    except:
                        print('Instância não autorizada, verifique os dados e tente novamente!')
                else:
                    servidor = Servidor(nome, cpf, nasc, sus, ocupacao, alocacao)
                    try:
                        if isinstance(servidor,Autorizacao):
                            ubs.add_servidor(nome, cpf, nasc, sus, ocupacao, alocacao)
                    except:
                        print('Instância não autorizada, verifique os dados e tente novamente!')
        except:
            print('Servidor já se encontra no cadastro!')
    elif op == 2:
        cpf = input('CPF: ')
        try:
            if not ubs.existe_comunitario(cpf):
                nome = input('Nome: ')
                nasc = input('Nasc: ')
                sus = input('sus: ')
                cond = int(input('Possui condição pré-existente? 1 - Sim ou 0 Não: '))
                if cond:
                    condicao = input('Qual: ')
                    comunitario = Comunitario(nome, cpf, nasc, sus, condicao)
                    if isinstance(comunitario, Autorizacao):
                        ubs.add_comunitario(nome, cpf, nasc, sus, condicao)
                else:
                    comunitario = Comunitario(nome, cpf, nasc, sus)
                    if isinstance(comunitario,Autorizacao):
                        ubs.add_comunitario(nome, cpf, nasc, sus)
        except:
            print('Comunitário já se encontra no cadastro!')
    elif op == 3:
        nome = input('Nome da vacina: ')
        try:
            if not ubs.existe_vacina(nome):
                lab = input('Laboratório da vacina: ')
                ref = int(input('Possui reforço? 1 - Sim ou 0 Não: '))
                if ref:
                    min = int(input('Prazo mínimo: '))
                    max = int(input('Prazo máximo: '))
                    ubs.add_vacina_lab(nome, lab, ref, min, max)
                else:
                    ubs.add_vacina_lab(nome, lab)
        except:
            print('Esta vacina já está cadstrada!')
    elif op == 4:
        nome = input('Nome da vacina: ')
        try:
            if ubs.existe_vacina(nome):
                lote = input('Lote da vacina: ')
                if not ubs.existe_lote(lote):
                    fab = input('Fabricação: ')
                    val = input('Validade: ')
                    qtd = int(input('Validade: '))
                    ubs.add_lote_vacina(nome, lote, fab, val, qtd)
        except:
            print('Vacina não cadastrada! tente novamente com outra vacina ou cadastre', nome)
    elif op == 5:
        condicao = input('Condição de prioridade: ')
        if not ubs.existe_condicao:
            ubs._lista_prioridade.append(condicao)
            print('Condição cadastrada com sucesso!')
        else:
            print('Esta condição já está no cadastro')


# help(Autorizacao)
Autorizacao.register(Comunitario)
Autorizacao.register(Servidor)

ubs = UBS()
carregar_dados()

while True:
    op = menu()
    if op == 1:
        cadastrar()
    elif op == 2:
        gerar_relatorios()
    elif op == 3:
        imprimir()
    elif op == 4:
        vacinar_1dose()
    elif op == 5:
        vacinar_2dose()
    elif op == 6:
        break