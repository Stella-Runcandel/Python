#PyQt5 intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #lable let's us diplay text,iamges
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celestia Project GUI")
        self.setGeometry(750,300,500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\mrram\\Pictures\\Screenshot 2021-07-14 3.06.29 PM.png"))

        lable = QLabel(self)
        lable.setGeometry(0,0,400,250)
        pixmap = QPixmap("C:\\Users\\mrram\\Pictures\\Ahri_85.jpg") 
        lable.setPixmap(pixmap)
        lable.setScaledContents(True)
        lable.setGeometry((self.width() -lable.width())//2,
                          (self.height()-lable.height())//2,
                          lable.width(),
                          lable.height())

def main():#
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()