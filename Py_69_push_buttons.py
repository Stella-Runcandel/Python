#PyQt5 intro
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celestia Project GUI")
        self.setGeometry(750,300,500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\mrram\\Pictures\\Screenshot 2021-07-14 3.06.29 PM.png"))
        self.button = QPushButton("Click Me!!",self)
        self.lable = QLabel("Hello",self)

        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.lable.setStyleSheet("font-size: 50px")
        self.lable.setGeometry(150,300,200,100)



    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.lable.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()