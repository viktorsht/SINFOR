import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QCoreApplication

# Back-End
# from ..Controllers.ubs import *

# Telas
from tela_acs import Tela_acs
from tela_cadastrar_acs import Tela_cadastrar_acs
from tela_cadastrar_comunitario import Tela_cadastrar_comunitario
from tela_cadastrar_lote import Tela_cadastrar_lote
from tela_cadastrar_ubs import Tela_cadastrar_ubs
from tela_cadastrar_vacina import Tela_cadastrar_vacina
from tela_cadastrar_laboratorio import Tela_cadastrar_laboratorio
from tela_comunitario import Tela_comunitario
from tela_laboratorio import Tela_labora
from tela_dash import Tela_dash
from tela_login import Tela_login
from tela_lote import Tela_lote
from tela_ubs import Tela_ubs
from tela_vacina import Tela_vacina


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

        self.tela(self.t_dash)

        # login
        self.t_login.btn_login.clicked.connect(self.logar)

        # home

        # home-cadastro
        self.t_ubs.btn_adicionar.clicked.connect(self.cadastrar_ubs)
        self.t_acs.btn_adicionar.clicked.connect(self.cadastrar_acs)
        self.t_comunitario.btn_adicionar.clicked.connect(
            self.cadastrar_comunitario)
        self.t_lote.btn_adicionar.clicked.connect(self.cadastrar_lote)
        self.t_vacina.btn_adicionar.clicked.connect(self.cadastrar_vacina)
        self.t_laboratorio.btn_adicionar.clicked.connect(
            self.cadastrar_laboratorio)

    def logar(self):
        cpf = self.t_login.cpf.text()
        senha = self.t_login.senha.text()
        if(cpf != '' and senha != ''):
            if self.b.existe_comunitario(cpf):
                if self.b._comunitario[cpf]._senha == senha:
                    self.t_login.cpf.setText('')
                    self.t_login.senha.setText('')
                    self.inicio()
                else:
                    QMessageBox.information(
                        None, 'Atenção!', 'Senha Incorreta!\nVerifique e tente novamente!')
            elif self.b.existe_servidor(cpf):
                if self.b._servidor[cpf]._senha == senha:
                    self.t_login.cpf.setText('')
                    self.t_login.senha.setText('')
                    self.inicio()
                else:
                    QMessageBox.information(
                        None, 'Atenção!', 'Senha Incorreta!\nVerifique e tente novamente!')
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Cliente não encontrado!\nVerifique e tente novamente!')
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campos em branco!')
        self.t_login.cpf.setText('')
        self.t_login.senha.setText('')

    def cadastrar_ubs(self):
        self.QtStack.setCurrentIndex(4)
        self.tela(self.t_cad_ubs)
        nome = self.t_cad_ubs.nome.text()
        if(nome != ''):
            pass
            # Nome não existe no banco ? Se não, adicionar o nome no banco.
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_acs(self):
        self.QtStack.setCurrentIndex(1)
        self.tela(self.t_cad_acs)
        nome = self.t_cad_acs.nome.text()
        codigo = self.t_cad_acs.codigo.text()
        if(nome != '' and codigo != ''):
            pass
            # Nome e código não existe no banco ? Se não, adicionar o nome no banco e código.
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_comunitario(self):
        self.QtStack.setCurrentIndex(2)
        self.tela(self.t_cad_comunitario)

        nome = self.t_cad_comunitario.nome.text()
        cpf = self.t_cad_comunitario.cpf.text()
        n_sus = self.t_cad_comunitario.n_sus.text()

        if(self.t_cad_comunitario.dose_1.text()):
            dose1 = 1
        else:
            dose1 = 0

        if(self.t_cad_comunitario.dose_2.text()):
            dose2 = 1
        else:
            dose2 = 0

        data1 = self.t_cad_comunitario.data_1.date().toPyDate()
        vacina1 = self.t_cad_comunitario.vacina_d1.text()
        lote1 = self.t_cad_comunitario.lote_1.text()
        data2 = self.t_cad_comunitario.data_2.date().toPyDate()
        vacina2 = self.t_cad_comunitario.vacina_d2.text()
        lote2 = self.t_cad_comunitario.lote_2.text()
        ubs = self.t_cad_comunitario.ubs.text()

        if(data1 != '' and vacina1 != '' and lote1 != '' and lote2 != '' and data2 != '' and vacina2 != '' and ubs != ''):
            pass
            # Nome e código não existe no banco ? Se não, adicionar o nome no banco e código.
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_lote(self):
        self.QtStack.setCurrentIndex(3)
        self.tela(self.t_cad_lote)
        vacina = self.t_cad_lote.vacina.text()
        lote = self.t_cad_lote.lote.text()
        fabricacao = self.t_cad_lote.fabricacao.text()
        validade = self.t_cad_lote.validade.text()

        if(vacina != '' and lote != '' and fabricacao != '' and validade != ''):
            pass
            # Nome e código não existe no banco ? Se não, adicionar o nome no banco e código.
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_vacina(self):
        self.QtStack.setCurrentIndex(5)
        self.tela(self.t_cad_vacina)
        nome = self.t_cad_vacina.nome.text()
        reforco = self.t_cad_vacina.reforco.text()
        laboratorio = self.t_cad_vacina.laboratorio.text()

        if(nome != '' and reforco != '' and laboratorio != ''):
            pass
            # Nome e código não existe no banco ? Se não, adicionar o nome no banco e código.
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Campo em branco!!')

    def cadastrar_laboratorio(self):
        self.QtStack.setCurrentIndex(13)
        self.tela(self.t_cad_labora)
        nome = self.t_cad_labora.nome.text()

    # feito

    def acs(self):
        self.QtStack.setCurrentIndex(8)
        self.tela(self.t_acs)

    # feito
    def ubs(self):
        self.QtStack.setCurrentIndex(10)

        self.tela(self.t_ubs)

    # feito
    def lote(self):
        self.QtStack.setCurrentIndex(9)
        self.tela(self.t_lote)

    # feito
    def laboratorio(self):
        self.QtStack.setCurrentIndex(12)
        self.tela(self.t_laboratorio)

    # feito
    def vacina(self):
        self.QtStack.setCurrentIndex(11)
        self.tela(self.t_vacina)

    # feito
    def comunitario(self):
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
