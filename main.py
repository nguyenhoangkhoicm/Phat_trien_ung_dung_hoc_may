import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5 import QtWidgets
from screen.home import Ui_home
from screen.welcome import Ui_loading
from PyQt5.QtCore import QCoreApplication,QTimer
import matplotlib.pyplot as plt
import pandas as pd

from functools import lru_cache
@lru_cache(maxsize=10)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_loading()
        self.uic.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.prbar)
        self.timer.start(500)
             
    def prbar(self):
        value = self.uic.progressBar.value()
        if value < 100:
            value = value + 5
            self.uic.progressBar.setValue(value)
        else:
            self. Second_window = QtWidgets.QMainWindow()
            self.uic1 = Ui_home()
            self.uic1.setupUi(self.Second_window)
            self.Second_window.show()
            self.uic1.camera.clicked.connect(self.openfile)
            self.uic1.img.clicked.connect(self.open_cmd)
            self.uic1.chart.clicked.connect(self.analysis)
            self.uic1.exit.clicked.connect(QCoreApplication.instance().quit)
            self.timer.stop()
            self.close()
        
  
    def openfile(self):
        os.startfile('gad.exe') 


    def open_cmd(self):  
        file , check = QFileDialog.getOpenFileName(None, "Open image",
                                               ".\image", "All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)")
        if check:
            fname = os.path.basename(file)
            os.system('gad.exe --image .\image\{}'.format(fname))
          
    def analysis(self): 
        df = pd.read_csv(r'.\data\gender_age.csv')
        colors = ["#1f77b4", "#ff7f0e",'#FF0000','#FFFF00','#00FF00','#CC66CC','#33CCFF']

        group_by_diag = df.groupby("age").count().reset_index()
        sizes = group_by_diag['gender']
        labels = group_by_diag['age']

        plt.title("Biểu đồ phân chia độ tuổi")
        plt.pie(sizes, labels = labels, colors = colors,autopct='%1.0f%%')
        plt.savefig(r'.\chart\pie.png')
        plt.show()
            
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    main_win.prbar()
    sys.exit(app.exec())


 
 