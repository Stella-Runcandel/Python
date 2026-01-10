#PyQt5 intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #lable let's us diplay text,iamges
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celestia Project GUI")
        self.setGeometry(750,300,500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\mrram\\Pictures\\Screenshot 2021-07-14 3.06.29 PM.png"))

        lable = QLabel("Hello",self)
        lable.setFont(QFont("Arial",30))
        #lable.adjustSize()
        lable.setGeometry(0,0,500,100)
        lable.setStyleSheet("Color: #a688ba;"
                            "background-color: #6b0f0f;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #lable.setAlignment(Qt.AlignTop) #vertically to the top , also exists align bottom
        #lable.setAlignment(Qt.AlignBottom) #vertically to the top , also exists align bottom
        #lable.setAlignment(Qt.AlignVCenter) #aligns to center
        #lable.setAlignment(Qt.AlignRight) #aligns to right horizontally
        #lable.setAlignment(Qt.AlignLeft) #aligns to left horizontally
        #lable.setAlignment(Qt.AlignHCenter) #aligns to center horizontally
        #lable.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        lable.setAlignment(Qt.AlignCenter) #same as above



def main():#
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()