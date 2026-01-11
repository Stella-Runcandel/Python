#PyQt5 intro
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                              QWidget,QVBoxLayout,QHBoxLayout,
                              QGridLayout)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celestia Project GUI")
        self.setGeometry(750,300,500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\mrram\\Pictures\\Screenshot 2021-07-14 3.06.29 PM.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lable1 = QLabel(" 1 ",self)
        lable2 = QLabel(" 2 ",self)
        lable3 = QLabel(" 3 ",self)
        lable4 = QLabel(" 4 ",self)
        lable5 = QLabel(" 5 ",self)
        lable1.setStyleSheet("background-color: red;")
        lable2.setStyleSheet("background-color: yellow;")
        lable3.setStyleSheet("background-color: green;")
        lable4.setStyleSheet("background-color: blue;")
        lable5.setStyleSheet("background-color: purple;")

        grid = QGridLayout()
        grid.addWidget(lable1,0,0)
        grid.addWidget(lable2,0,1)
        grid.addWidget(lable3,1,0)
        grid.addWidget(lable4,1,1)
        grid.addWidget(lable5,2,2)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()