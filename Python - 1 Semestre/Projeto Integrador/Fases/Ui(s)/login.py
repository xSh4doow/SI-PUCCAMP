# coding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets


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
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/LOGO PEQUENA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(100.0)
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(226, 226, 226);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(230, 10, 791, 371))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Imagens/LOGO GERAL.png"))
        self.Logo.setObjectName("Logo")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(490, 520, 251, 61))
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
        self.userBox = QtWidgets.QComboBox(self.centralwidget)
        self.userBox.setGeometry(QtCore.QRect(500, 450, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        self.userBox.setFont(font)
        self.userBox.setObjectName("userBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Controle de Qualidade do Ar"))
        self.loginButton.setText(_translate("MainWindow", "Entrar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
