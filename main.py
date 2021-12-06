import sys
import pandas as pd
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from configFW import Ui_Dialog
from configFW_G import Ui_Dialog_Graph
from configFW_T import Ui_Dialog_Tables
from setingsSW_1 import Ui_OtherWindow_1
from setingsSW import Ui_OtherWindow
from setingsOW_2 import Ui_OtherWindow_2
from config import Ui_Dialog_0


app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def openTables():
    global Dialog_Tables
    Dialog_Tables = QtWidgets.QDialog()
    ui = Ui_Dialog_Tables()
    ui.setupUi(Dialog_Tables)
    Dialog.close()
    Dialog_Tables.show()

    def openTables_1():
        global OtherWindow_1
        OtherWindow_1 = QtWidgets.QDialog()
        ui = Ui_OtherWindow_1()
        ui.setupUi(OtherWindow_1)
        OtherWindow_1.show()


    ui.pushButton_2.clicked.connect(openTables_1)

    def openTables_2():
        global OtherWindow
        OtherWindow = QtWidgets.QDialog()
        ui = Ui_OtherWindow()
        ui.setupUi(OtherWindow)
        OtherWindow.show()


    ui.pushButton.clicked.connect(openTables_2)

    def openTables_3():
        global OtherWindow_2
        OtherWindow_2 = QtWidgets.QDialog()
        ui = Ui_OtherWindow_2()
        ui.setupUi(OtherWindow_2)
        OtherWindow_2.show()

    ui.pushButton_3.clicked.connect(openTables_3)


    def returnTOMain():
        Dialog_Tables.close()
        Dialog.show()

    ui.pushButton_4.clicked.connect(returnTOMain)

ui.pushButton.clicked.connect(openTables)

def openGraph():
    global Dialog_Graph
    Dialog_Graph = QtWidgets.QDialog()
    ui = Ui_Dialog_Graph()
    ui.setupUi(Dialog_Graph)
    Dialog.close()
    Dialog_Graph.show()

    def openG():
        img = Image.open('Figure_1.png')
        img.show()

    ui.pushButton_5.clicked.connect(openG)

    def returnTOMain_1():
        Dialog_Graph.close()
        Dialog.show()

    ui.pushButton_4.clicked.connect(returnTOMain_1)


ui.pushButton_2.clicked.connect(openGraph)

def exito():
    Dialog.close()

ui.pushButton_4.clicked.connect(exito)

def conf():
    global Dialog_0
    Dialog_0 = QtWidgets.QDialog()
    ui = Ui_Dialog_0()
    ui.setupUi(Dialog_0)
    Dialog_0.show()


ui.pushButton_3.clicked.connect(conf)

sys.exit(app.exec_())