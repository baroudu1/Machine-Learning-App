import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from untitled import Ui_Form


class Welcome(QMainWindow, Ui_Form):
    def __init__(self):
        super(Welcome, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = Welcome()
    welcome.show()
    sys.exit(app.exec_())