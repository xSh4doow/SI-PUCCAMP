from PyQt5 import QtCore, QtGui, QtWidgets
from c_c import Ui_Form
from login import Ui_MainWindow as UMWL
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../uis/imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(100.0)
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(226, 226, 226);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(230, 10, 791, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Logo.setFont(font)
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../uis/imagens/LOGO GERAL.png"))
        self.Logo.setObjectName("Logo")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(500, 430, 251, 61))
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
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(500, 520, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(17)
        self.signupButton.setFont(font)
        self.signupButton.setAutoFillBackground(False)
        self.signupButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.signupButton.setIconSize(QtCore.QSize(32, 32))
        self.signupButton.setCheckable(False)
        self.signupButton.setObjectName("signupButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signupButton.clicked.connect(self.openSignup)
        self.loginButton.clicked.connect(self.openLogin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Controle de Qualidade do Ar"))
        self.loginButton.setText(_translate("MainWindow", "Entrar"))
        self.signupButton.setText(_translate("MainWindow", "Criar Ar"))

    def openSignup(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UMWL()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
