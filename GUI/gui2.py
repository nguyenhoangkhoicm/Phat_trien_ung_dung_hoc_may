


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,GUI.res as res

class Ui_home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 453)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 631, 451))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 451))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("border-image: url(:/image/background.png);\n"
"border-radius: 20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 601, 431))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius:15px;\n"
"color:rgba(255, 255, 255,210);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 340, 321, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camera = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.camera.setFont(font)
        self.camera.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0,0,90,100);\n"
"    border-radius:8px;\n"
"    color:rgba(255, 255, 255,210);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 103, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.camera.setObjectName("camera")
        self.horizontalLayout.addWidget(self.camera)
        self.img = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.img.setFont(font)
        self.img.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0,0,90,100);\n"
"    border-radius:8px;\n"
"    color:rgba(255, 255, 255,210);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 103, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.img.setObjectName("img")
        self.horizontalLayout.addWidget(self.img)
        self.chart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.chart.setFont(font)
        self.chart.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0,0,90,100);\n"
"    border-radius:8px;\n"
"    color:rgba(255, 255, 255,210);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 103, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.chart.setObjectName("chart")
        self.horizontalLayout.addWidget(self.chart)
        self.exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0,0,90,100);\n"
"    border-radius:8px;\n"
"    color:rgba(255, 255, 255,210);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 103, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 90, 511, 231))
        self.textBrowser.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius:15px;\n"
"color:rgba(255, 255, 255,210);")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trang chu"))
        self.label_3.setText(_translate("MainWindow", "Nhận diện tuổi và giới tính"))
        self.camera.setText(_translate("MainWindow", "🎦"))
        self.img.setText(_translate("MainWindow", "🧑‍🦱"))
        self.chart.setText(_translate("MainWindow", "💹"))
        self.exit.setText(_translate("MainWindow", "❌"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       <span style=\" color:#6b9fff;\"> </span><span style=\" font-size:12pt; font-weight:600; color:#6b9fff;\">Môn học: Phát triển ứng dụng học máy.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#5500ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Đề tài: Nhận diện tuổi và giới tính</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Thành viên nhóm:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nguyễn Hoàng Khởi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Phan Quốc Bảo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nguyễn Hải Đăng</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Mô tả chương trình:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">Gồm 2 chức năng chính</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\"> +Nhận diện giới tính và tuổi thông qua camera laptop.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\"> +Nhận diện qua hình ảnh.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Hướng dẫn sử dụng:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nút Camera dùng để nhận diện tuổi và giới tính thông qua camera của máy tính, để thoát chương trình nhận diện nhấn phím &quot;q&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nút Image dùng dể nhận diện tuổi và giới tính thông qua hình ảnh.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nút Phân tích dùng để thống kê dữ liệu chúng ta vừa thu thập được.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">-Nút thoát dùng để thoát khỏi chương trình.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#000000;\"><br /></p></body></html>"))

