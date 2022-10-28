
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,GUI.res as res

class Ui_loading(object):
    def setupUi(self, loading):
        loading.setObjectName("loading")
        loading.resize(355, 341)
        loading.setStyleSheet("")
        loading.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        loading.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(loading)
        self.centralwidget.setObjectName("centralwidget")
        self.conntener = QtWidgets.QFrame(self.centralwidget)
        self.conntener.setGeometry(QtCore.QRect(30, 10, 281, 281))
        self.conntener.setStyleSheet("")
        self.conntener.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conntener.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conntener.setObjectName("conntener")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.conntener)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back_gr = QtWidgets.QFrame(self.conntener)
        self.back_gr.setStyleSheet("QFrame{\n"
"    \n"
"    background-image: url(:/image/background.png);\n"
"    background-color: #44475a;\n"
"    border-radius:120px;\n"
"}")
        self.back_gr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.back_gr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.back_gr.setObjectName("back_gr")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.back_gr)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.back_gr)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 90, 181, 21))
        self.progressBar.setStyleSheet("border-bottom-color: rgb(48, 60, 165);\n"
"text-align:center;\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 81, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";\n"
"border-radius:10px;\n"
"background-color: rgb(98, 64, 140);\n"
"text-align:center;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 151, 41))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"color: #f8f8f2;\n"
"font: 75 20pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 71, 31))
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
"color: #282a36;\n"
"font: 9pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.back_gr)
        loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(loading)
        QtCore.QMetaObject.connectSlotsByName(loading)

    def retranslateUi(self, loading):
        _translate = QtCore.QCoreApplication.translate
        loading.setWindowTitle(_translate("loading", "Loading"))
        self.label_2.setText(_translate("loading", "version:1.5"))
        self.pushButton.setText(_translate("loading", "Program_GA"))
        self.pushButton_2.setText(_translate("loading", "Loading...."))

