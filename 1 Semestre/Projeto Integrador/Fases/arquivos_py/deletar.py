from PyQt5 import QtCore, QtGui, QtWidgets
import sql_funcs as sql


class Ui_Form(object):
    def setupUi(self, Form):
        self.ar = ''
        Form.setObjectName("Form")
        Form.resize(798, 713)
        Form.setStyleSheet("\n"
                           "background-color: rgb(226, 226, 226);")
        self.Logo = QtWidgets.QLabel(Form)
        self.Logo.setGeometry(QtCore.QRect(210, -10, 371, 301))
        self.Logo.setStyleSheet("\n"
                                "background-color: rgb(226, 226, 226);")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../uis/imagens/LOGO GERAL.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.deletarButton = QtWidgets.QPushButton(Form)
        self.deletarButton.setGeometry(QtCore.QRect(250, 520, 311, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../uis/imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(17)
        self.deletarButton.setFont(font)
        self.deletarButton.setMouseTracking(False)
        self.deletarButton.setAutoFillBackground(False)
        self.deletarButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.deletarButton.setIconSize(QtCore.QSize(32, 32))
        self.deletarButton.setCheckable(False)
        self.deletarButton.setAutoDefault(False)
        self.deletarButton.setDefault(False)
        self.deletarButton.setFlat(False)
        self.deletarButton.setObjectName("deletarButton")
        self.amostraBox = QtWidgets.QComboBox(Form)
        self.amostraBox.setGeometry(QtCore.QRect(260, 350, 301, 22))
        self.amostraBox.setObjectName("amostraBox")
        self.optionsButton = QtWidgets.QPushButton(Form)
        self.optionsButton.setGeometry(QtCore.QRect(580, 340, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        self.optionsButton.setFont(font)
        self.optionsButton.setMouseTracking(False)
        self.optionsButton.setAutoFillBackground(False)
        self.optionsButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.optionsButton.setIconSize(QtCore.QSize(32, 32))
        self.optionsButton.setCheckable(False)
        self.optionsButton.setAutoDefault(False)
        self.optionsButton.setDefault(False)
        self.optionsButton.setFlat(False)
        self.optionsButton.setObjectName("optionsButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.optionsButton.clicked.connect(self.getAms)
        self.deletarButton.clicked.connect(self.deletar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Deletar Amostra"))
        self.deletarButton.setText(_translate("Form", "DELETAR AMOSTRA"))
        self.optionsButton.setText(_translate("Form", "Obter Amostras"))

    def deletar(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Aviso!')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../uis/imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        resp = sql.deletar(self.selected)
        msg.setText(resp)

        x = msg.exec_()

    def getAms(self):
        self.amostraBox.addItems(sql.usuarios('amostras', self.ar))
        self.selected = self.amostraBox.currentText()
