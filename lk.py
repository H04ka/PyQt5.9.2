# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovgorodovProrab(object):
    def setupUi(self, NovgorodovProrab):
        NovgorodovProrab.setObjectName("NovgorodovProrab")
        NovgorodovProrab.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NovgorodovProrab)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 30, 471, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/i.qrc.webp"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 231, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 90, 341, 471))
        self.textEdit.setObjectName("textEdit")
        NovgorodovProrab.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NovgorodovProrab)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        NovgorodovProrab.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NovgorodovProrab)
        self.statusbar.setObjectName("statusbar")
        NovgorodovProrab.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(NovgorodovProrab)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(NovgorodovProrab)
        self.action_2.setObjectName("action_2")
        self.actionAdd_file = QtWidgets.QAction(NovgorodovProrab)
        self.actionAdd_file.setObjectName("actionAdd_file")
        self.actionOpen_file = QtWidgets.QAction(NovgorodovProrab)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.menuMenu.addAction(self.action)
        self.menuMenu.addAction(self.action_2)
        self.menuFile.addAction(self.actionOpen_file)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(NovgorodovProrab)
        QtCore.QMetaObject.connectSlotsByName(NovgorodovProrab)

    def retranslateUi(self, NovgorodovProrab):
        _translate = QtCore.QCoreApplication.translate
        NovgorodovProrab.setWindowTitle(_translate("NovgorodovProrab", "MainWindow"))
        self.menuMenu.setTitle(_translate("NovgorodovProrab", "Menu"))
        self.menuFile.setTitle(_translate("NovgorodovProrab", "File"))
        self.action.setText(_translate("NovgorodovProrab", "О программе"))
        self.action.setShortcut(_translate("NovgorodovProrab", "Ctrl+I"))
        self.action_2.setText(_translate("NovgorodovProrab", "Выход"))
        self.actionAdd_file.setText(_translate("NovgorodovProrab", "Add file"))
        self.actionOpen_file.setText(_translate("NovgorodovProrab", "Open file "))
        self.actionOpen_file.setShortcut(_translate("NovgorodovProrab", "Ctrl+L"))
import tests1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NovgorodovProrab = QtWidgets.QMainWindow()
    ui = Ui_NovgorodovProrab()
    ui.setupUi(NovgorodovProrab)
    NovgorodovProrab.show()
    sys.exit(app.exec_())