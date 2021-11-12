# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_ubs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_ubs(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 480)
        MainWindow.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame.setStyleSheet("background-color: #4285f4;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.btn_inicio = QtWidgets.QPushButton(self.frame)
        self.btn_inicio.setGeometry(QtCore.QRect(10, 110, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_inicio.setFont(font)
        self.btn_inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_inicio.setStyleSheet("border:none;\n"
                                      "color: #fff;")
        self.btn_inicio.setObjectName("btn_inicio")
        self.btn_ubs = QtWidgets.QPushButton(self.frame)
        self.btn_ubs.setGeometry(QtCore.QRect(10, 150, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_ubs.setFont(font)
        self.btn_ubs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ubs.setStyleSheet("border:none;\n"
                                   "color: #fff;")
        self.btn_ubs.setObjectName("btn_ubs")
        self.btn_comunitario = QtWidgets.QPushButton(self.frame)
        self.btn_comunitario.setGeometry(QtCore.QRect(10, 350, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_comunitario.setFont(font)
        self.btn_comunitario.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_comunitario.setStyleSheet("border:none;\n"
                                           "color: #fff;")
        self.btn_comunitario.setObjectName("btn_comunitario")
        self.btn_acs = QtWidgets.QPushButton(self.frame)
        self.btn_acs.setGeometry(QtCore.QRect(10, 190, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_acs.setFont(font)
        self.btn_acs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_acs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_acs.setStyleSheet("border:none;\n"
                                   "color: #fff;")
        self.btn_acs.setCheckable(False)
        self.btn_acs.setObjectName("btn_acs")
        self.btn_laboratorio = QtWidgets.QPushButton(self.frame)
        self.btn_laboratorio.setGeometry(QtCore.QRect(10, 310, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_laboratorio.setFont(font)
        self.btn_laboratorio.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_laboratorio.setStyleSheet("border:none;\n"
                                           "color: #fff;")
        self.btn_laboratorio.setObjectName("btn_laboratorio")
        self.btn_lote = QtWidgets.QPushButton(self.frame)
        self.btn_lote.setGeometry(QtCore.QRect(10, 230, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_lote.setFont(font)
        self.btn_lote.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_lote.setStyleSheet("border:none;\n"
                                    "color: #fff;")
        self.btn_lote.setObjectName("btn_lote")
        self.btn_vacina = QtWidgets.QPushButton(self.frame)
        self.btn_vacina.setGeometry(QtCore.QRect(10, 270, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_vacina.setFont(font)
        self.btn_vacina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_vacina.setStyleSheet("border:none;\n"
                                      "color: #fff;")
        self.btn_vacina.setObjectName("btn_vacina")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 191, 17))
        self.label_11.setStyleSheet("color: #4285f4;")
        self.label_11.setObjectName("label_11")
        self.btn_adicionar = QtWidgets.QPushButton(self.frame_4)
        self.btn_adicionar.setGeometry(QtCore.QRect(390, 10, 121, 25))
        self.btn_adicionar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_adicionar.setStyleSheet("background-color: #4285F4;\n"
                                         "color: #FFF;")
        self.btn_adicionar.setObjectName("btn_adicionar")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 431, 192))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(211, 215, 207))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(211, 215, 207))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(211, 215, 207))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(143)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(100, 30, 311, 17))
        self.label_10.setStyleSheet("color: #4285f4;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SINFOR"))
        self.label_9.setText(_translate("MainWindow", "Versão 1.0"))
        self.btn_inicio.setText(_translate("MainWindow", "Início"))
        self.btn_ubs.setText(_translate("MainWindow", "UBS"))
        self.btn_comunitario.setText(_translate("MainWindow", "Comunitário"))
        self.btn_acs.setText(_translate("MainWindow", "ACS"))
        self.btn_laboratorio.setText(_translate("MainWindow", "Laboratório"))
        self.btn_lote.setText(_translate("MainWindow", "Lote"))
        self.btn_vacina.setText(_translate("MainWindow", "Vacina"))
        self.label_11.setText(_translate("MainWindow", "Home / UBS "))
        self.btn_adicionar.setText(_translate("MainWindow", "Adicionar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CÓDIGO"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Impueiras"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Vicente Baldino"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "47"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "Paroquial"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "55"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate(
            "MainWindow", "2021 - SINFOR |  Todos os direitos reservados"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Tela_ubs()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
