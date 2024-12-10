from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
import lk

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = lk.Ui_NovgorodovProrab()
        self.ui.setupUi(self)
        self.ui.action_2.triggered.connect(app.quit)
        self.ui.action.triggered.connect(self.avtor)
        self.ui.actionOpen_file.triggered.connect(self.open_file)
    
    def avtor(self):
        self.ui.label_2.setText("ИП 24-26б Г.Е")
    

    def open_file(self):
        try:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files(*.txt)", options=options)
            if file_name:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.ui.textEdit.setPlainText(content)
        except:
            QtWidgets.QMessageBox.critical(window, 'Invalid format Error', 'Неверный формат, выберите txt', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())