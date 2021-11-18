
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QCoreApplication

# Telas
from Views.tela_acs import Tela_acs
from Views.tela_cadastrar_acs import Tela_cadastrar_acs
from Views.tela_cadastrar_comunitario import Tela_cadastrar_comunitario
from Views.tela_cadastrar_lote import Tela_cadastrar_lote
from Views.tela_cadastrar_ubs import Tela_cadastrar_ubs
from Views.tela_cadastrar_vacina import Tela_cadastrar_vacina
from Views.tela_cadastrar_laboratorio import Tela_cadastrar_laboratorio
from Views.tela_comunitario import Tela_comunitario
from Views.tela_laboratorio import Tela_labora
from Views.tela_dash import Tela_dash
from Views.tela_login import Tela_login
from Views.tela_lote import Tela_lote
from Views.tela_ubs import Tela_ubs
from Views.tela_vacina import Tela_vacina

# BACK
from Controllers.core import Core


class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()
        self.stack13 = QtWidgets.QMainWindow()
        self.stack14 = QtWidgets.QMainWindow()

        self.t_login = Tela_login()
        self.t_login.setupUi(self.stack0)

        self.t_cad_acs = Tela_cadastrar_acs()
        self.t_cad_acs.setupUi(self.stack1)

        self.t_cad_comunitario = Tela_cadastrar_comunitario()
        self.t_cad_comunitario.setupUi(self.stack2)

        self.t_cad_lote = Tela_cadastrar_lote()
        self.t_cad_lote.setupUi(self.stack3)

        self.t_cad_ubs = Tela_cadastrar_ubs()
        self.t_cad_ubs.setupUi(self.stack4)

        self.t_cad_vacina = Tela_cadastrar_vacina()
        self.t_cad_vacina.setupUi(self.stack5)

        self.t_cad_labora = Tela_cadastrar_laboratorio()
        self.t_cad_labora.setupUi(self.stack13)

        self.t_comunitario = Tela_comunitario()
        self.t_comunitario.setupUi(self.stack6)

        self.t_dash = Tela_dash()
        self.t_dash.setupUi(self.stack7)

        self.t_acs = Tela_acs()
        self.t_acs.setupUi(self.stack8)

        self.t_lote = Tela_lote()
        self.t_lote.setupUi(self.stack9)

        self.t_ubs = Tela_ubs()
        self.t_ubs.setupUi(self.stack10)

        self.t_vacina = Tela_vacina()
        self.t_vacina.setupUi(self.stack11)

        self.t_laboratorio = Tela_labora()
        self.t_laboratorio.setupUi(self.stack12)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # self.b = UBS()
        self.core = Core()

        # self.tela(self.t_dash)

        # login
        self.t_login.btn_login.clicked.connect(self.logar)

        # home

        # home-cadastro

        self.t_ubs.btn_adicionar.clicked.connect(self.add_ubs)
        self.t_acs.btn_adicionar.clicked.connect(self.add_acs)
        self.t_lote.btn_adicionar.clicked.connect(self.add_lote)
        self.t_vacina.btn_adicionar.clicked.connect(self.add_vacina)
        self.t_laboratorio.btn_adicionar.clicked.connect(self.add_laboratorio)
        self.t_comunitario.btn_adicionar.clicked.connect(self.add_comunitario)
        self.logado = ''

    def add_ubs(self):
        self.QtStack.setCurrentIndex(4)
        self.t_cad_ubs.btn_cadastrar.clicked.connect(self.cadastrar_ubs)

    def add_acs(self):
        self.QtStack.setCurrentIndex(1)
        self.t_cad_acs.btn_cadastrar.clicked.connect(self.cadastrar_acs)

    def add_lote(self):
        self.QtStack.setCurrentIndex(3)
        self.t_cad_lote.btn_cadastrar.clicked.connect(self.cadastrar_lote)

    def add_vacina(self):
        self.QtStack.setCurrentIndex(5)
        self.t_cad_vacina.btn_cadastrar.clicked.connect(self.cadastrar_vacina)

    def add_laboratorio(self):
        self.QtStack.setCurrentIndex(13)
        self.t_cad_labora.btn_cadastrar.clicked.connect(self.cadastrar_laboratorio)
    
    def add_comunitario(self):
        self.QtStack.setCurrentIndex(2)
        self.t_cad_comunitario.btn_cadastrar.clicked.connect(self.cadastrar_comunitario)

    def logar(self):
        cpf = self.t_login.cpf.text()
        senha = self.t_login.senha.text()

        if(cpf != '' and senha != ''):
            if self.core.login(cpf, senha):
                self.t_login.cpf.setText('')
                self.t_login.senha.setText('')
                # result =''
                # query = 'SELECT nivel_de_acesso FROM usu
                # self.core.connect(query, (), result
                # self.logado = nível de acesso
                self.inicio()
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Usuário ou senha incorretos!\nVerifique e tente novamente!')
        else:
            QMessageBox.information(None, 'Atenção!', 'Campos em branco!')

    def cadastrar_ubs(self):
        self.tela(self.t_cad_ubs)
        nome = self.t_cad_ubs.nome.text()
        cod = self.t_cad_ubs.codigo.text()

        if(nome != '' and cod != ''):
            if self.core.cadastrar_ubs(cod, nome):
                QMessageBox.information(
                    None, 'Sucesso!', 'Cadastro realizado!!')
                self.t_cad_ubs.nome.setText('')
                self.t_cad_ubs.codigo.setText('')
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Operação inválida!\nVerifique e tente novamente!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Preencha todos os campos!!')


    def cadastrar_acs(self):
        # self.QtStack.setCurrentIndex(1)
        self.tela(self.t_cad_acs)
        nome = self.t_cad_acs.nome.text()
        codigo = self.t_cad_acs.codigo.text()

        if(nome != '' and codigo != ''):
            if self.core.cadastrar_acs(nome, codigo):
                QMessageBox.information(
                    None, 'Atenção!', 'Inserido com sucesso!')
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Erro ao inserir!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_comunitario(self):
        # self.QtStack.setCurrentIndex(2)
        self.tela(self.t_cad_comunitario)

        nome = self.t_cad_comunitario.nome.text()
        cpf = self.t_cad_comunitario.cpf.text()
        n_sus = self.t_cad_comunitario.n_sus.text()
        s_d1 = self.t_cad_comunitario.dose_1.isChecked()
        data1 = self.t_cad_comunitario.data_1.date().toPyDate()
        s_d2 = self.t_cad_comunitario.dose_2.isChecked()
        data2 = self.t_cad_comunitario.data_2.date().toPyDate()
        codigo_acs = self.t_cad_comunitario.codigo_acs.text()
        codido_ubs = self.t_cad_comunitario.codigo_ubs.text()
        lote1 = self.t_cad_comunitario.lote_1.text()
        lote2 = self.t_cad_comunitario.lote_2.text()
        # s_d2 = self.t_cad_comunitario.dose_2.isChecked()
        # data2 = self.t_cad_comunitario.data_2.date().toPyDate()
        # lote2 = self.t_cad_comunitario.lote_2.text()
        # codido_ubs = self.t_cad_comunitario.codigo_ubs.text()
        # codigo_acs = self.t_cad_comunitario.codigo_acs.text()

        result  = self.core.cadastrar_comunitario(nome, cpf, n_sus, s_d1, data1, s_d2, data2, codigo_acs, codido_ubs, lote1, lote2)

        if result:
            nome = self.t_cad_comunitario.nome.setText('')
            cpf = self.t_cad_comunitario.cpf.setText('')
            n_sus = self.t_cad_comunitario.n_sus.setText('')
            # data1 = self.t_cad_comunitario.data_1.date().toPyDate()
            # lote1 = self.t_cad_comunitario.lote_1.setText('')
            # data2 = self.t_cad_comunitario.data_2.setText('')
            # lote2 = self.t_cad_comunitario.lote_2.setText('')
            # codido_ubs = self.t_cad_comunitario.codigo_ubs.setText('')
            # codigo_acs = self.t_cad_comunitario.codigo_acs.setText('')
            QMessageBox.information(
                None, 'Atenção!', 'Inserido com sucesso!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Erro ao inserir!')

        # if(self.t_cad_comunitario.dose_1.text()):
        #     dose1 = 1
        # else:
        #     dose1 = 0

        # if(self.t_cad_comunitario.dose_2.text()):
        #     dose2 = 1
        # else:
        #     dose2 = 0

        # if(data1 != '' and lote1 != '' and lote2 != '' and data2 != '' and codido_ubs != '' and codigo_acs != ''):
        #     if s_d1 == True:

        #         if self.core.validar_laboratorio_por_id(lote1):
        #             if s_d2:
        #                 if self.core.validar_laboratorio_por_id(lote2):
        #                     aux = 1
        #                 else:
        #                     aux = -1

        #             else:
        #                 data2 = 'NULL'
        #                 lote2 = 'NULL'
        #                 aux = 1

        #             if aux:
        #                 if self.core.validar_ubs_por_id(codido_ubs):
        #                     if self.core.validar_acs_por_id(codigo_acs):
                                
        #                         result  = self.core.cadastrar_comunitario(
        #                             nome,
        #                             cpf,
        #                             n_sus,
        #                             codido_ubs,
        #                             codigo_acs,
        #                             s_d1,
        #                             data1,
        #                             lote1,
        #                             s_d2,
        #                             data2,
        #                             lote2
        #                         )

        #                         if result:
        #                             nome = self.t_cad_comunitario.nome.setText('')
        #                             cpf = self.t_cad_comunitario.cpf.setText('')
        #                             n_sus = self.t_cad_comunitario.n_sus.setText('')
        #                             # s_d1 = self.t_cad_comunitario.dose_1.setCheckState(False)
        #                             data1 = self.t_cad_comunitario.data_1.date().toPyDate()
        #                             lote1 = self.t_cad_comunitario.lote_1.setText('')
        #                             # s_d2 = self.t_cad_comunitario.dose_2.isChecked()
        #                             data2 = self.t_cad_comunitario.data_2.setText('')
        #                             lote2 = self.t_cad_comunitario.lote_2.setText('')
        #                             codido_ubs = self.t_cad_comunitario.codigo_ubs.setText('')
        #                             codigo_acs = self.t_cad_comunitario.codigo_acs.setText('')
        #                             QMessageBox.information(
        #                                 None, 'Atenção!', 'Inserido com sucesso!')
        #                         else:
        #                             QMessageBox.information(
        #                                 None, 'Atenção!', 'Erro ao inserir!')

        #                     else:
        #                         QMessageBox.information(
        #                             None, 'Atenção!', 'Codigo ACS invalido')
        #                 else:
        #                    QMessageBox.information(
        #                     None, 'Atenção!', 'Codigo UBS invalido')
        #                 QMessageBox.information(
        #                     None, 'Atenção!', 'Lote 2 não encontrado!')
        #         else:
        #             QMessageBox.information(
        #                 None, 'Atenção!', 'Lote 1 não encontrado!')
        #     else:
        #         QMessageBox.information(
        #             None, 'Atenção!', 'Pelo menos uma dose precisa estar marcada!')

        #     # pass
        #     # Nome e código não existe no banco ? Se não, adicionar o nome no banco e código.
            

        # else:
        #     QMessageBox.information(
        #         None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_lote(self):
        # self.QtStack.setCurrentIndex(3)
        self.tela(self.t_cad_lote)

        vacina = self.t_cad_lote.vacina.text()
        lote = self.t_cad_lote.lote.text()
        fabricacao = self.t_cad_lote.fabricacao.text()
        validade = self.t_cad_lote.validade.text()

        if(vacina != '' and lote != '' and fabricacao != '' and validade != ''):

            if not self.core.validarData(validade):
                QMessageBox.information(
                    None, 'Atenção!', 'Formato da data validade errada')
            elif not self.core.validarData(fabricacao):
                QMessageBox.information(
                    None, 'Atenção!', 'Formato da data fabricacao errada')
            else:
                result  = self.core.cadastrar_lote(vacina, lote, fabricacao, validade)
                if result == -1:
                    QMessageBox.information(
                        None, 'Atenção!', 'Vacina não encontrado!')

                elif result:
                    QMessageBox.information(
                        None, 'Atenção!', 'Inserido com sucesso!')
                    self.t_cad_lote.vacina.setText('')
                    self.t_cad_lote.lote.setText('')
                    self.t_cad_lote.fabricacao.setText('')
                    self.t_cad_lote.validade.setText('')
                else:
                    QMessageBox.information(
                        None, 'Atenção!', 'Erro ao inserir!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_vacina(self):
        # self.QtStack.setCurrentIndex(5)
        self.tela(self.t_cad_vacina)
        nome = self.t_cad_vacina.nome.text()
        reforco = self.t_cad_vacina.reforco.text()
        laboratorio = self.t_cad_vacina.laboratorio.text()

        if(nome != '' and reforco != '' and laboratorio != ''):
            if int(reforco) >= 15:
                result  = self.core.cadastrar_vacina(nome, reforco, laboratorio)
                if result == -1:
                    QMessageBox.information(
                        None, 'Atenção!', 'Laboratorio não encontrado!')

                elif result:
                    QMessageBox.information(
                        None, 'Atenção!', 'Inserido com sucesso!')
                    self.t_cad_vacina.nome.setText('')
                    self.t_cad_vacina.reforco.setText('')
                    self.t_cad_vacina.laboratorio.setText('')
                else:
                    QMessageBox.information(
                        None, 'Atenção!', 'Erro ao inserir!')
            else:
                QMessageBox.information(
                None, 'Atenção!', 'Reforço incorreto!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_laboratorio(self):
        # self.QtStack.setCurrentIndex(13)
        self.tela(self.t_cad_labora)
        nome = self.t_cad_labora.nome.text()

        if nome != '':
            result = self.core.cadastrar_laboratorio(nome)
            print(result)
            if result:
                self.t_cad_labora.nome.setText('')
                QMessageBox.information(
                    None, 'Atenção!', 'Cadastrado com sucesso!')
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Erro ao inserir!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')


    # feito

    def acs(self):
        if self.core.getListACS():
            tela = self.t_acs
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 3):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))

        self.QtStack.setCurrentIndex(8)
        self.tela(self.t_acs)

    # feito
    def ubs(self):
        if self.core.getListUBS():
            tela = self.t_ubs
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 3):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))
        self.tela(self.t_ubs)
        self.QtStack.setCurrentIndex(10)

    # feito

    def lote(self):
        if self.core.getListBatchVaccine():
            tela = self.t_lote
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 5):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))

        self.QtStack.setCurrentIndex(9)
        self.tela(self.t_lote)

    # feito
    def laboratorio(self):
        if self.core.getListLaboratory():
            tela = self.t_laboratorio
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 2):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))

        self.QtStack.setCurrentIndex(12)
        self.tela(self.t_laboratorio)

    # feito
    def vacina(self):
        if self.core.getListVaccine():
            tela = self.t_vacina
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 4):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))

        self.QtStack.setCurrentIndex(11)
        self.tela(self.t_vacina)

    # feito
    def comunitario(self):
        if self.core.getListCommunity():
            tela = self.t_comunitario
            tamanho = len(self.core.result)
            tela.tableWidget.setRowCount(tamanho)
            for i, item in enumerate(self.core.result):
                for j in range(0, 9):
                    tela.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(item[j])))

        self.QtStack.setCurrentIndex(6)
        self.tela(self.t_comunitario)

    # feito
    def inicio(self):

        self.QtStack.setCurrentIndex(7)
        self.tela(self.t_dash)


    def tela(self, tela):
        tela.btn_ubs.clicked.connect(self.ubs)
        tela.btn_acs.clicked.connect(self.acs)
        tela.btn_comunitario.clicked.connect(self.comunitario)
        tela.btn_inicio.clicked.connect(self.inicio)
        tela.btn_laboratorio.clicked.connect(self.laboratorio)
        tela.btn_lote.clicked.connect(self.lote)
        tela.btn_vacina.clicked.connect(self.vacina)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
