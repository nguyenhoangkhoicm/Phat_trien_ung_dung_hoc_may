import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from GUI.gui2 import Ui_home
from PyQt5.QtCore import QCoreApplication
import matplotlib.pyplot as plt
import pandas as pd

from functools import lru_cache
@lru_cache(maxsize=10)

class MainWindow:
    def __init__(self):
        
        self.main_win = QMainWindow()
        self.uic = Ui_home()
        self.uic.setupUi(self.main_win)
        self.uic.camera.clicked.connect(self.openfile)
        self.uic.img.clicked.connect(self.open_cmd)
        self.uic.chart.clicked.connect(self.analysis)
        self.uic.exit.clicked.connect(QCoreApplication.instance().quit)


    def openfile(self):
        os.startfile(r'gad.exe') 


    def open_cmd(self):  
        file , check = QFileDialog.getOpenFileName(None, "Open image",
                                               ".\image", "All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)")
        if check:
            fname = os.path.basename(file)
            os.system(r'gad.exe --image .\image\{}'.format(fname))
          
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


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())