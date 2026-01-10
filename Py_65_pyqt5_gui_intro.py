#PyQt5 intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Celestia Project GUI")
        self.setGeometry(750,300,500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\mrram\\Pictures\\Screenshot 2021-07-14 3.06.29 PM.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()