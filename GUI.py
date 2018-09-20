
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_MainWindow(object)
    def setupUI(self, mainWindow):


import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    UI = UI_MainWindow()
    UI.setupUI(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())