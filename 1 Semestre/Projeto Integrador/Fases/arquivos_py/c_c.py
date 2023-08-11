from PyQt5 import QtCore, QtGui, QtWidgets
import sql_funcs as sql

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 553)
        Form.setStyleSheet("\n"
                           "background-color: rgb(226, 226, 226);")
        self.Logo = QtWidgets.QLabel(Form)
        self.Logo.setGeometry(QtCore.QRect(-50, 0, 791, 371))
        self.Logo.setStyleSheet("\n"
                                "background-color: rgb(226, 226, 226);")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../uis/imagens/LOGO GERAL.png"))
        self.Logo.setObjectName("Logo")
        self.signButton = QtWidgets.QPushButton(Form)
        self.signButton.setGeometry(QtCore.QRect(240, 440, 251, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../uis/imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(17)
        self.signButton.setFont(font)
        self.signButton.setMouseTracking(False)
        self.signButton.setAutoFillBackground(False)
        self.signButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.signButton.setIconSize(QtCore.QSize(32, 32))
        self.signButton.setCheckable(False)
        self.signButton.setAutoDefault(False)
        self.signButton.setDefault(False)
        self.signButton.setFlat(False)
        self.signButton.setObjectName("signButton")
        self.userinput = QtWidgets.QLineEdit(Form)
        self.userinput.setGeometry(QtCore.QRect(240, 400, 251, 20))
        self.userinput.setText("")
        self.userinput.setObjectName("userinput")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 380, 251, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.signButton.clicked.connect(self.criar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Criar Ar"))
        self.signButton.setText(_translate("Form", "Criar Ar"))
        self.label.setText(_translate("Form", "Digite o nome do Ar:"))

    def criar(self):
        username = self.userinput.text()
        resp = sql.criar_conta(username)
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../uis/imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle('Aviso!')
        msg.setText(resp)

        x = msg.exec_()

