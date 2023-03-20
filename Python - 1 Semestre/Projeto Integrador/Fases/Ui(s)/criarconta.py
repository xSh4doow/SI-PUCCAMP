# coding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 600)
        Form.setStyleSheet("\n"
                           "background-color: rgb(226, 226, 226);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(100.0)
        self.Logo = QtWidgets.QLabel(Form)
        self.Logo.setGeometry(QtCore.QRect(-50, 0, 791, 371))
        self.Logo.setStyleSheet("\n"
                                "background-color: rgb(226, 226, 226);")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Imagens/LOGO GERAL.png"))
        self.Logo.setObjectName("Logo")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(240, 440, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(17)
        self.loginButton.setFont(font)
        self.loginButton.setMouseTracking(False)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.loginButton.setIconSize(QtCore.QSize(32, 32))
        self.loginButton.setCheckable(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 400, 251, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 380, 251, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 520, 251, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CRIAR CONTA"))
        self.loginButton.setText(_translate("Form", "CRIAR CONTA"))
        self.label.setText(_translate("Form", "DIGITE SEU USERNAME DESEJADO:"))
        self.label_2.setText(_translate("Form", "ERRO!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
