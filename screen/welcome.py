
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.wel2 import Ui_loading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_loading()
        self.uic.setupUi(self)
        
        
    def progres(self):
        for i in range(100):
            time.sleep(0.1)
            self.uic.progressBar.setValue(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


 
 