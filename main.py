import time
from PyQt5.QtCore import QTimer
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
from datetime import datetime, timedelta, date
import threading
import sqlite3
import pkgutil
import xml
import xml.etree
import xml.etree.ElementTree

stop = 0

Form, Window = uic.loadUiType("lokodrom.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
today = datetime.today()

sqlite_connection = sqlite3.connect("lokofile.db", check_same_thread=False)
cursor = sqlite_connection.cursor()
lock = threading.Lock()

pause_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=1""")).fetchone()[0])  # 0
start_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=7""")).fetchone()[0])  # 1
pause_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=2""")).fetchone()[0])  # 0
start_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=8""")).fetchone()[0])  # 1
pause_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=3""")).fetchone()[0])  # 0
start_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=9""")).fetchone()[0])  # 1
pause_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=4""")).fetchone()[0])  # 0
start_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=10""")).fetchone()[0])  # 1
pause_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=5""")).fetchone()[0])  # 0
start_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=11""")).fetchone()[0])  # 1
pause_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=6""")).fetchone()[0])  # 0
start_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=12""")).fetchone()[0])  # 1
flag = 0


def Reset1():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=1""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=1""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=1""")
    sqlite_connection.commit()
    form.tableWidget.item(0, 2).setText(str("0h 0m"))
    form.progressBar.setProperty("value", 0)


def Reset2():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=7""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=7""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=7""")
    sqlite_connection.commit()
    form.tableWidget.item(1, 2).setText(str("0h 0m"))
    form.progressBar_2.setProperty("value", 0)


def Reset3():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=2""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=2""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=2""")
    sqlite_connection.commit()
    form.tableWidget.item(2, 2).setText(str("0h 0m"))
    form.progressBar_3.setProperty("value", 0)


def Reset4():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=8""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=8""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=8""")
    sqlite_connection.commit()
    form.tableWidget.item(3, 2).setText(str("0h 0m"))
    form.progressBar_4.setProperty("value", 0)


def Reset5():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=3""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=3""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=3""")
    sqlite_connection.commit()
    form.tableWidget.item(4, 2).setText(str("0h 0m"))
    form.progressBar_5.setProperty("value", 0)


def Reset6():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=9""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=9""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=9""")
    sqlite_connection.commit()
    form.tableWidget.item(5, 2).setText(str("0h 0m"))
    form.progressBar_6.setProperty("value", 0)


def Reset7():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=4""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=4""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=4""")
    sqlite_connection.commit()
    form.tableWidget.item(6, 2).setText(str("0h 0m"))
    form.progressBar_7.setProperty("value", 0)


def Reset8():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=10""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=10""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=10""")
    sqlite_connection.commit()
    form.tableWidget.item(7, 2).setText(str("0h 0m"))
    form.progressBar_8.setProperty("value", 0)


def Reset9():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=5""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=5""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=5""")
    sqlite_connection.commit()
    form.tableWidget.item(8, 2).setText(str("0h 0m"))
    form.progressBar_9.setProperty("value", 0)


def Reset10():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=11""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=11""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=11""")
    sqlite_connection.commit()
    form.tableWidget.item(9, 2).setText(str("0h 0m"))
    form.progressBar_10.setProperty("value", 0)


def Reset11():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=6""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=6""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=6""")
    sqlite_connection.commit()
    form.tableWidget.item(10, 2).setText(str("0h 0m"))
    form.progressBar_11.setProperty("value", 0)


def Reset12():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET clear=(clear+current_main) WHERE ID=12""")
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET current_main='0' WHERE ID=12""")
    cursor.execute(f"""UPDATE poll SET main='0' WHERE ID=12""")
    sqlite_connection.commit()
    form.tableWidget.item(11, 2).setText(str("0h 0m"))
    form.progressBar_12.setProperty("value", 0)


def button():
    form.pushButton_10.clicked.connect(button_clicked1)
    form.pushButton_21.clicked.connect(button_clicked2)
    form.pushButton_9.clicked.connect(button_clicked3)
    form.pushButton_22.clicked.connect(button_clicked4)
    form.pushButton_6.clicked.connect(button_clicked5)
    form.pushButton_23.clicked.connect(button_clicked6)
    form.pushButton_8.clicked.connect(button_clicked7)
    form.pushButton_24.clicked.connect(button_clicked8)
    form.pushButton_5.clicked.connect(button_clicked9)
    form.pushButton_25.clicked.connect(button_clicked10)
    form.pushButton_7.clicked.connect(button_clicked11)
    form.pushButton_26.clicked.connect(button_clicked12)


def pause1():
    global pause_flag_1, start_flag_1
    if pause_flag_1 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=1""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=7""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=1""")).fetchone()[0])
    start_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=7""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(1, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(0, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_15.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_3.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_7.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_1.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def pause2():
    global pause_flag_2, start_flag_2
    if pause_flag_2 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=2""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=8""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=2""")).fetchone()[0])
    start_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=8""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(3, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(2, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_16.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_4.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_8.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_2.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def pause3():
    global pause_flag_3, start_flag_3
    if pause_flag_3 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=3""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=9""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=3""")).fetchone()[0])
    start_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=9""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(5, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(4, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_17.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
    form.pushButton_11.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_9.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_3.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def pause4():
    global pause_flag_4, start_flag_4
    if pause_flag_4 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=4""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=10""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=4""")).fetchone()[0])
    start_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=10""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(7, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(6, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_18.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
    form.pushButton_12.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_10.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_4.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def pause5():
    global pause_flag_5, start_flag_5
    if pause_flag_5 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=5""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=11""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=5""")).fetchone()[0])
    start_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=11""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(9, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(8, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_19.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
    form.pushButton_13.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_11.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_5.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def pause6():
    global pause_flag_6, start_flag_6
    if pause_flag_6 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=6""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=12""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=6""")).fetchone()[0])
    start_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=12""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(11, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(10, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_20.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189);color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
    form.pushButton_14.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_12.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_6.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def button_pause():
    form.pushButton_3.clicked.connect(pause1)
    form.pushButton_4.clicked.connect(pause2)
    form.pushButton_11.clicked.connect(pause3)
    form.pushButton_12.clicked.connect(pause4)
    form.pushButton_13.clicked.connect(pause5)
    form.pushButton_14.clicked.connect(pause6)


def start1():
    global start_flag_1, pause_flag_1
    if start_flag_1 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=1""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=7""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=1""")).fetchone()[0])
    start_flag_1 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=7""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(0, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(1, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_3.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_15.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_1.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_7.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def start2():
    global start_flag_2, pause_flag_2
    if start_flag_2 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=2""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=8""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=2""")).fetchone()[0])
    start_flag_2 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=8""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(2, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(3, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_4.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_16.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_2.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_8.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def start3():
    global start_flag_3, pause_flag_3
    if start_flag_3 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=3""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=9""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=3""")).fetchone()[0])
    start_flag_3 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=9""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(4, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(5, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_11.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_17.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_3.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_9.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def start4():
    global start_flag_4, pause_flag_4
    if start_flag_4 == 1:
        return
    start_flag_4 = 1
    pause_flag_4 = 0
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=4""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=10""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=4""")).fetchone()[0])
    start_flag_4 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=10""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(6, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(7, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_12.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_18.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_4.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_10.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def start5():
    global start_flag_5, pause_flag_5
    if start_flag_5 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=5""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=11""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=5""")).fetchone()[0])
    start_flag_5 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=11""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(8, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(9, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_13.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_19.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_5.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_11.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def start6():
    global start_flag_6, pause_flag_6
    if start_flag_6 == 1:
        return
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET flags=0 WHERE ID=6""")  # pause_flag_1
    cursor.execute(f"""UPDATE poll SET flags=1 WHERE ID=12""")  # start_flag_1
    sqlite_connection.commit()
    pause_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=6""")).fetchone()[0])
    start_flag_6 = int((cursor.execute(f"""SELECT flags FROM poll WHERE ID=12""")).fetchone()[0])
    for i in range(4):
        form.tableWidget.item(10, i).setBackground(QtGui.QColor(85, 255, 127))
        form.tableWidget.item(11, i).setBackground(QtGui.QColor(255, 161, 148))
    form.pushButton_14.setStyleSheet(
        "QPushButton{background-color: rgb(202, 201, 189); color: red;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.pushButton_20.setStyleSheet(
        "QPushButton{background-color: rgb(240, 240, 240); color: green;border: 1px solid black;border-radius: 4px} "
        "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
    form.spinBox_6.setStyleSheet(
        "QSpinBox {background-color: rgb(85,255,127);font-size: 12pt; font-family: Times New Roman;}")
    form.spinBox_12.setStyleSheet(
        "QSpinBox {background-color: rgb(255,161,148);font-size: 12pt; font-family: Times New Roman;}")


def button_start():
    form.pushButton_15.clicked.connect(start1)
    form.pushButton_16.clicked.connect(start2)
    form.pushButton_17.clicked.connect(start3)
    form.pushButton_18.clicked.connect(start4)
    form.pushButton_19.clicked.connect(start5)
    form.pushButton_20.clicked.connect(start6)


def norma():
    form.spinBox_1.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=1""")).fetchone()[0]))
    form.spinBox_2.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=2""")).fetchone()[0]))
    form.spinBox_3.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=3""")).fetchone()[0]))
    form.spinBox_4.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=4""")).fetchone()[0]))
    form.spinBox_5.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=5""")).fetchone()[0]))
    form.spinBox_6.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=6""")).fetchone()[0]))
    form.spinBox_7.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=7""")).fetchone()[0]))
    form.spinBox_8.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=8""")).fetchone()[0]))
    form.spinBox_9.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=9""")).fetchone()[0]))
    form.spinBox_10.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=10""")).fetchone()[0]))
    form.spinBox_11.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=11""")).fetchone()[0]))
    form.spinBox_12.setProperty("value", int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=12""")).fetchone()[0]))


def save():
    sqlite_connection.commit()
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(0, 0).text()}' WHERE ID=1""")  # train
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(2, 0).text()}' WHERE ID=2""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(4, 0).text()}' WHERE ID=3""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(6, 0).text()}' WHERE ID=4""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(8, 0).text()}' WHERE ID=5""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(10, 0).text()}' WHERE ID=6""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(1, 0).text()}' WHERE ID=7""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(3, 0).text()}' WHERE ID=8""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(5, 0).text()}' WHERE ID=9""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(7, 0).text()}' WHERE ID=10""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(9, 0).text()}' WHERE ID=11""")
    cursor.execute(f"""UPDATE poll SET train='{form.tableWidget.item(11, 0).text()}' WHERE ID=12""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_1.text().replace(" hour", "")}' WHERE ID=1""")  # norma
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_2.text().replace(" hour", "")}' WHERE ID=2""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_3.text().replace(" hour", "")}' WHERE ID=3""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_4.text().replace(" hour", "")}' WHERE ID=4""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_5.text().replace(" hour", "")}' WHERE ID=5""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_6.text().replace(" hour", "")}' WHERE ID=6""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_7.text().replace(" hour", "")}' WHERE ID=7""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_8.text().replace(" hour", "")}' WHERE ID=8""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_9.text().replace(" hour", "")}' WHERE ID=9""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_10.text().replace(" hour", "")}' WHERE ID=10""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_11.text().replace(" hour", "")}' WHERE ID=11""")
    cursor.execute(f"""UPDATE poll SET norma='{form.spinBox_12.text().replace(" hour", "")}' WHERE ID=12""")
    cursor.execute(f"""UPDATE datas SET minuts='{form.spinBox_13.text()}' WHERE ID=1""")  # data
    cursor.execute(f"""UPDATE datas SET seconds='{form.spinBox_14.text()}' WHERE ID=1""")
    sqlite_connection.commit()


def initialTrains():
    form.tableWidget.item(10, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=6""")).fetchone()[0]))
    form.tableWidget.item(8, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=5""")).fetchone()[0]))
    form.tableWidget.item(6, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=4""")).fetchone()[0]))
    form.tableWidget.item(4, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=3""")).fetchone()[0]))
    form.tableWidget.item(2, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=2""")).fetchone()[0]))
    form.tableWidget.item(0, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=1""")).fetchone()[0]))
    form.tableWidget.item(11, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=12""")).fetchone()[0]))
    form.tableWidget.item(9, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=11""")).fetchone()[0]))
    form.tableWidget.item(7, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=10""")).fetchone()[0]))
    form.tableWidget.item(5, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=9""")).fetchone()[0]))
    form.tableWidget.item(3, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=8""")).fetchone()[0]))
    form.tableWidget.item(1, 0).setText(str((cursor.execute(f"""SELECT train FROM poll WHERE ID=7""")).fetchone()[0]))


def progress_bar():
    lol2 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=1""")).fetchone()[0])
    lol3 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=7""")).fetchone()[0])
    lol4 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=2""")).fetchone()[0])
    lol5 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=8""")).fetchone()[0])
    lol6 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=3""")).fetchone()[0])
    lol7 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=9""")).fetchone()[0])
    lol8 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=4""")).fetchone()[0])
    lol9 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=10""")).fetchone()[0])
    lol10 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=5""")).fetchone()[0])
    lol11 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=11""")).fetchone()[0])
    lol12 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=6""")).fetchone()[0])
    lol13 = int((cursor.execute(f"""SELECT norma FROM poll WHERE ID=12""")).fetchone()[0])
    if int(lol2) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=1""")).fetchone()[0])) * go // 3600)):
        form.progressBar.setProperty("value", 100)
        form.progressBar.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                       "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                       "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol2) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=1""")).fetchone()[0])) * go // 3600))) / int(
            lol2)) * 100) < 60:
            form.progressBar.setProperty("value",
                                         int((1 - int(int(lol2) - int(
                                             ((int((cursor.execute(
                                                 f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) + int(
                                                 (cursor.execute(f"""SELECT main FROM poll WHERE ID=1""")).fetchone()[
                                                     0])) * go // 3600))) / int(
                                             lol2)) * 100))
        else:
            form.progressBar.setProperty("value",
                                         int((1 - int(int(lol2) - int(
                                             ((int((cursor.execute(
                                                 f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) + int(
                                                 (cursor.execute(f"""SELECT main FROM poll WHERE ID=1""")).fetchone()[
                                                     0])) * go // 3600))) / int(
                                             lol2)) * 100))
            form.progressBar.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol3) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=7""")).fetchone()[0])) * go // 3600)):
        form.progressBar_2.setProperty("value", 100)
        form.progressBar_2.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol3) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=7""")).fetchone()[0])) * go // 3600))) / int(
            lol3)) * 100) < 60:
            form.progressBar_2.setProperty("value",
                                           int((1 - int(int(lol3) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=7""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol3)) * 100))
        else:
            form.progressBar_2.setProperty("value",
                                           int((1 - int(int(lol3) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=7""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol3)) * 100))
            form.progressBar_2.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol4) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=2""")).fetchone()[0])) * go // 3600)):
        form.progressBar_3.setProperty("value", 100)
        form.progressBar_3.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol4) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=2""")).fetchone()[0])) * go // 3600))) / int(
            lol4)) * 100) < 60:
            form.progressBar_3.setProperty("value",
                                           int((1 - int(int(lol4) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=2""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol4)) * 100))
        else:
            form.progressBar_3.setProperty("value",
                                           int((1 - int(int(lol4) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=2""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol4)) * 100))
            form.progressBar_3.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol5) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=8""")).fetchone()[0])) * go // 3600)):
        form.progressBar_4.setProperty("value", 100)
        form.progressBar_4.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol5) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=8""")).fetchone()[0])) * go // 3600))) / int(
            lol5)) * 100) < 60:
            form.progressBar_4.setProperty("value",
                                           int((1 - int(int(lol5) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=8""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol5)) * 100))
        else:
            form.progressBar_4.setProperty("value",
                                           int((1 - int(int(lol5) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=8""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol5)) * 100))
            form.progressBar_4.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol6) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=3""")).fetchone()[0])) * go // 3600)):
        form.progressBar_5.setProperty("value", 100)
        form.progressBar_5.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol6) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=3""")).fetchone()[0])) * go // 3600))) / int(
            lol6)) * 100) < 60:
            form.progressBar_5.setProperty("value",
                                           int((1 - int(int(lol6) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=3""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol6)) * 100))
        else:
            form.progressBar_5.setProperty("value",
                                           int((1 - int(int(lol6) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=3""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol6)) * 100))
            form.progressBar_5.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol7) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=9""")).fetchone()[0])) * go // 3600)):
        form.progressBar_6.setProperty("value", 100)
        form.progressBar_6.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol7) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=9""")).fetchone()[0])) * go // 3600))) / int(
            lol7)) * 100) < 60:
            form.progressBar_6.setProperty("value",
                                           int((1 - int(int(lol7) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=9""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol7)) * 100))
        else:
            form.progressBar_6.setProperty("value",
                                           int((1 - int(int(lol7) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=9""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol7)) * 100))
            form.progressBar_6.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol8) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=4""")).fetchone()[0])) * go // 3600)):
        form.progressBar_7.setProperty("value", 100)
        form.progressBar_7.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol8) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=4""")).fetchone()[0])) * go // 3600))) / int(
            lol8)) * 100) < 60:
            form.progressBar_7.setProperty("value",
                                           int((1 - int(int(lol8) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=4""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol8)) * 100))
        else:
            form.progressBar_7.setProperty("value",
                                           int((1 - int(int(lol8) - int(
                                               (int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[
                                                        0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=4""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol8)) * 100)
            form.progressBar_7.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol9) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=10""")).fetchone()[0])) * go // 3600)):
        form.progressBar_8.setProperty("value", 100)
        form.progressBar_8.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol9) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=10""")).fetchone()[0])) * go // 3600))) / int(
            lol9)) * 100) < 60:
            form.progressBar_8.setProperty("value",
                                           int((1 - int(int(lol9) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[
                                                         0]) + int((cursor.execute(
                                                   f"""SELECT main FROM poll WHERE ID=10""")).fetchone()[
                                                                       0])) * go // 3600))) / int(
                                               lol9)) * 100))
        else:
            form.progressBar_8.setProperty("value",
                                           int((1 - int(int(lol9) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[
                                                         0]) + int((cursor.execute(
                                                   f"""SELECT main FROM poll WHERE ID=10""")).fetchone()[
                                                                       0])) * go // 3600))) / int(
                                               lol9)) * 100))
            form.progressBar_8.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol10) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=5""")).fetchone()[0])) * go // 3600)):
        form.progressBar_9.setProperty("value", 100)
        form.progressBar_9.setStyleSheet("QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
                                         "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
                                         "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol10) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=5""")).fetchone()[0])) * go // 3600))) / int(
            lol10)) * 100) < 60:
            form.progressBar_9.setProperty("value",
                                           int((1 - int(int(lol10) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=5""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol10)) * 100))
        else:
            form.progressBar_9.setProperty("value",
                                           int((1 - int(int(lol10) - int(
                                               ((int((cursor.execute(
                                                   f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[
                                                         0]) + int(
                                                   (cursor.execute(f"""SELECT main FROM poll WHERE ID=5""")).fetchone()[
                                                       0])) * go // 3600))) / int(
                                               lol10)) * 100))
            form.progressBar_9.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol11) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=11""")).fetchone()[0])) * go // 3600)):
        form.progressBar_10.setProperty("value", 100)
        form.progressBar_10.setStyleSheet(
            "QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
            "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
            "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol11) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=11""")).fetchone()[0])) * go // 3600))) / int(
            lol11)) * 100) < 60:
            form.progressBar_10.setProperty("value",
                                            int((1 - int(int(lol11) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=11""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol11)) * 100))
        else:
            form.progressBar_10.setProperty("value",
                                            int((1 - int(int(lol11) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=11""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol11)) * 100))
            form.progressBar_10.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol12) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=6""")).fetchone()[0])) * go // 3600)):
        form.progressBar_11.setProperty("value", 100)
        form.progressBar_11.setStyleSheet(
            "QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
            "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
            "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol12) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=6""")).fetchone()[0])) * go // 3600))) / int(
            lol12)) * 100) < 60:
            form.progressBar_11.setProperty("value",
                                            int((1 - int(int(lol12) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=6""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol12)) * 100))
        else:
            form.progressBar_11.setProperty("value",
                                            int((1 - int(int(lol12) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=6""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol12)) * 100))
            form.progressBar_11.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")
    if int(lol13) <= int(((int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=12""")).fetchone()[0])) * go // 3600)):
        form.progressBar_12.setProperty("value", 100)
        form.progressBar_12.setStyleSheet(
            "QProgressBar::chunk {background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,"
            "stop: 0 #FF0350,stop: 0.4999 #FF0020,stop: 0.5 #FF0019,stop: 1 #FF0000 );border"
            "-bottom-right-radius: 1px;border-bottom-left-radius: 1px;border: 1px solid black;}")
    else:
        if int((1 - int(int(lol13) - int(((int(
                (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) + int(
            (cursor.execute(f"""SELECT main FROM poll WHERE ID=12""")).fetchone()[0])) * go // 3600))) / int(
            lol13)) * 100) < 60:
            form.progressBar_12.setProperty("value",
                                            int((1 - int(int(lol13) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=12""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol13)) * 100))
        else:
            form.progressBar_12.setProperty("value",
                                            int((1 - int(int(lol13) - int(((int((cursor.execute(
                                                f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) + int(
                                                (cursor.execute(f"""SELECT main FROM poll WHERE ID=12""")).fetchone()[
                                                    0])) * go // 3600))) / int(lol13)) * 100))
            form.progressBar_12.setStyleSheet(
                "QProgressBar::chunk {background-color: rgb(250, 232, 25); border: 1px solid;}")


def minuts():
    global min
    min = int((cursor.execute(f"""SELECT minuts FROM datas WHERE ID=1""")).fetchone()[0])
    min = min * 60


def pool():
    form.spinBox_13.setProperty("value",
                                str((cursor.execute(f"""SELECT minuts FROM datas WHERE ID=1""")).fetchone()[0]))
    form.spinBox_14.setProperty("value",
                                str((cursor.execute(f"""SELECT seconds FROM datas WHERE ID=1""")).fetchone()[0]))


def seconds():
    global sec, go
    sec = int((cursor.execute(f"""SELECT seconds FROM datas WHERE ID=1""")).fetchone()[0])
    go = min + sec


def interval():
    minuts()
    seconds()
    minut1 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0])
    second1 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=1""")).fetchone()[0])
    minut2 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[0])
    second2 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=7""")).fetchone()[0])
    minut3 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[0])
    second3 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=2""")).fetchone()[0])
    minut4 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[0])
    second4 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=8""")).fetchone()[0])
    minut5 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[0])
    second5 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=3""")).fetchone()[0])
    minut6 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[0])
    second6 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=9""")).fetchone()[0])
    minut7 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[0])
    second7 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=4""")).fetchone()[0])
    minut8 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[0])
    second8 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=10""")).fetchone()[0])
    minut9 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[0])
    second9 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=5""")).fetchone()[0])
    minut10 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0])
    second10 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=11""")).fetchone()[0])
    minut11 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0])
    second11 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=6""")).fetchone()[0])
    minut12 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0])
    second12 = int((cursor.execute(f"""SELECT main FROM poll WHERE ID=12""")).fetchone()[0])
    time_now = f"{((minut1 + second1) * go // 3600)}h {((minut1 + second1) * go % 3600 // 60)}m"
    form.tableWidget.item(0, 2).setText(time_now)
    time_now1 = f"{((minut2 + second2) * go // 3600)}h {((minut2 + second2) * go % 3600 // 60)}m"
    form.tableWidget.item(1, 2).setText(time_now1)
    time_now2 = f"{((minut3 + second3) * go // 3600)}h {((minut3 + second3) * go % 3600 // 60)}m"
    form.tableWidget.item(2, 2).setText(time_now2)
    time_now3 = f"{((minut4 + second4) * go // 3600)}h {((minut4 + second4) * go % 3600 // 60)}m"
    form.tableWidget.item(3, 2).setText(time_now3)
    time_now4 = f"{((minut5 + second5) * go // 3600)}h {((minut5 + second5) * go % 3600 // 60)}m"
    form.tableWidget.item(4, 2).setText(time_now4)
    time_now5 = f"{((minut6 + second6) * go // 3600)}h {((minut6 + second6) * go % 3600 // 60)}m"
    form.tableWidget.item(5, 2).setText(time_now5)
    time_now6 = f"{((minut7 + second7) * go // 3600)}h {((minut7 + second7) * go % 3600 // 60)}m"
    form.tableWidget.item(6, 2).setText(time_now6)
    time_now7 = f"{((minut8 + second8) * go // 3600)}h {((minut8 + second8) * go % 3600 // 60)}m"
    form.tableWidget.item(7, 2).setText(time_now7)
    time_now8 = f"{((minut9 + second9) * go // 3600)}h {((minut9 + second9) * go % 3600 // 60)}m"
    form.tableWidget.item(8, 2).setText(time_now8)
    time_now9 = f"{((minut10 + second10) * go // 3600)}h {((minut10 + second10) * go % 3600 // 60)}m"
    form.tableWidget.item(9, 2).setText(time_now9)
    time_now10 = f"{((minut11 + second11) * go // 3600)}h {((minut11 + second11) * go % 3600 // 60)}m"
    form.tableWidget.item(10, 2).setText(time_now10)
    time_now11 = f"{((minut12 + second12) * go // 3600)}h {((minut12 + second12) * go % 3600 // 60)}m"
    form.tableWidget.item(11, 2).setText(time_now11)


def today_z():
    if str((cursor.execute(f"""SELECT datam FROM datas WHERE ID=1""")).fetchone()[0]) <= str(date.today()):
        days = str(date.today() + timedelta(days=1))
        cursor.execute(f"""UPDATE datas SET datam='{days}' WHERE ID=1""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=1""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=2""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=3""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=4""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=5""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=6""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=7""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=8""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=9""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=10""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=11""")
        cursor.execute(f"""UPDATE poll SET main=main+current_main WHERE ID=12""")
        sqlite_connection.commit()
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=1""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=2""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=3""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=4""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=5""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=6""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=7""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=8""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=9""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=10""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=11""")
        cursor.execute(f"""UPDATE poll SET current_main=0 WHERE ID=12""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=1""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=2""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=3""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=4""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=5""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=6""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=7""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=8""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=9""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=10""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=11""")
        cursor.execute(f"""UPDATE poll SET clear=0 WHERE ID=12""")
        sqlite_connection.commit()


def puff():
    if pause_flag_1 == 1:
        form.pushButton_15.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_3.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); color: green;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.tableWidget.item(1, 0).setBackground(QtGui.QColor(255, 255, 255))
        form.tableWidget.item(0, 0).setBackground(QtGui.QColor(255, 161, 148))
        form.spinBox_7.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_1.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(1, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(0, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_1 == 1:
        form.pushButton_3.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red;border:1px solid black;border-radius: 4px}"
            "QPushButton:hover{background-color:  rgb(225, 252, 255); }")
        form.pushButton_15.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240);color: green;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_1.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_7.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(0, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(1, i).setBackground(QtGui.QColor(255, 161, 148))
    if pause_flag_2 == 1:
        form.pushButton_16.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_4.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); color: green;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_8.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_2.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(3, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(2, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_2 == 1:
        form.pushButton_4.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189); color: red;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.pushButton_16.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240);color: green;border:1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_2.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_8.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(2, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(3, i).setBackground(QtGui.QColor(255, 161, 148))
    if pause_flag_3 == 1:
        form.pushButton_17.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red; border: 1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_11.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_9.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_3.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(5, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(4, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_3 == 1:
        form.pushButton_11.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189); border: 1px solid black;color: red;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.pushButton_17.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_3.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_9.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(4, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(5, i).setBackground(QtGui.QColor(255, 161, 148))
    if pause_flag_4 == 1:
        form.pushButton_18.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red; border: 1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_12.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_10.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_4.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(7, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(6, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_4 == 1:
        form.pushButton_12.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189); border: 1px solid black;color: red;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.pushButton_18.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_4.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_10.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(6, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(7, i).setBackground(QtGui.QColor(255, 161, 148))
    if pause_flag_5 == 1:
        form.pushButton_19.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red; border: 1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_13.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_11.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_5.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(9, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(8, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_5 == 1:
        form.pushButton_13.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189); border: 1px solid black;color: red;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.pushButton_19.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_5.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_11.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(8, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(9, i).setBackground(QtGui.QColor(255, 161, 148))
    if pause_flag_6 == 1:
        form.pushButton_20.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);color: red; border: 1px solid black;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255)}")
        form.pushButton_14.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_12.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_6.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(11, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(10, i).setBackground(QtGui.QColor(255, 161, 148))
    if start_flag_6 == 1:
        form.pushButton_14.setStyleSheet(
            "QPushButton{background-color: rgb(202, 201, 189);border: 1px solid black;color: red;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.pushButton_20.setStyleSheet(
            "QPushButton{background-color: rgb(240, 240, 240); border: 1px solid black;color: green;border-radius: 4px} "
            "QPushButton:hover{background-color:  rgb(225, 252, 255);}")
        form.spinBox_6.setStyleSheet("QSpinBox {background-color: rgb(85,255,127)}")
        form.spinBox_12.setStyleSheet("QSpinBox {background-color: rgb(255,161,148)}")
        for i in range(4):
            form.tableWidget.item(10, i).setBackground(QtGui.QColor(85, 255, 127))
            form.tableWidget.item(11, i).setBackground(QtGui.QColor(255, 161, 148))


def run():
    global pool
    i = 0
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT1\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run()
    with open(fr'\\PULT1\RailControl\log\{road}.txt') as t:
        try:
            while True:
                time.sleep(2)
                lock.acquire(True)
                nice = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=1""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=7""")).fetchone()[0])
                lock.release()
                time.sleep(7)
                for line in t:
                    if "total" in line:
                        i += 1
                if i != nice:
                    if pause_flag_1 == 0 and start_flag_1 == 1:
                        lock.acquire(True)
                        rowid01 = int(i) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=7""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=1""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=7""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid01)}' WHERE ID=1""")
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid02 = int(i) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=1""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=1""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=7""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid02)}' WHERE ID=7""")
                        sqlite_connection.commit()
        except:
            lock.release()
            return run()


def run1():
    global pool
    o = 0
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT2\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run1()
    with open(fr'\\PULT2\RailControl\log\{road}.txt') as t1:
        while True:
            try:
                time.sleep(4)
                lock.acquire(True)
                nice1 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=2""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=8""")).fetchone()[0])
                lock.release()
                time.sleep(10)
                for line1 in t1:
                    if "total" in line1:
                        o += 1
                if o != nice1:
                    if pause_flag_2 == 0 and start_flag_2 == 1:
                        lock.acquire(True)
                        rowid1 = int(o) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=8""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=2""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=8""")).fetchone()[0])
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid1)}' WHERE ID=2""")
                        lock.release()
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid2 = int(o) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=2""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=2""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=8""")).fetchone()[0])
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid2)}' WHERE ID=8""")
                        lock.release()
                        sqlite_connection.commit()
            except:
                lock.release()
                return run1()


def run2():
    global pool
    p = 0
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT3\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run2()
    with open(fr'\\PULT3\RailControl\log\{road}.txt') as t2:
        try:
            while True:
                time.sleep(6)
                lock.acquire(True)
                nice2 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=3""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=9""")).fetchone()[0])
                lock.release()
                time.sleep(13)
                for line2 in t2:
                    if "total" in line2:
                        p += 1
                if p != nice2:
                    if pause_flag_3 == 0 and start_flag_3 == 1:
                        lock.acquire(True)
                        rowid3 = int(p) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=9""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=3""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=9""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid3)}' WHERE ID=3""")
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid4 = int(p) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=3""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=3""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=9""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid4)}' WHERE ID=9""")
                        sqlite_connection.commit()
        except:
            lock.release()
            return run2()


def run3():
    global pool
    j = 0
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT4\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run3()
    with open(fr'\\PULT4\RailControl\log\{road}.txt') as t3:
        try:
            while True:
                time.sleep(8)
                lock.acquire(True)
                nice3 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=4""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=10""")).fetchone()[0])
                lock.release()
                time.sleep(16)
                for line3 in t3:
                    if "total" in line3:
                        j += 1
                if j != nice3:
                    if pause_flag_4 == 0 and start_flag_4 == 1:
                        lock.acquire(True)
                        rowid5 = int(j) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=10""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=4""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=10""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid5)}' WHERE ID=4""")
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid6 = int(j) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=4""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=4""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=10""")).fetchone()[0])
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid6)}' WHERE ID=10""")
                        lock.release()
                        sqlite_connection.commit()
        except:
            lock.release()
            return run3()


def run4():
    global pool
    k = 0
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT5\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run4()
    with open(fr'\\PULT5\RailControl\log\{road}.txt') as t4:
        while True:
            try:
                time.sleep(10)
                lock.acquire(True)
                nice4 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=5""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=11""")).fetchone()[0])
                lock.release()
                time.sleep(19)
                for line4 in t4:
                    if "total" in line4:
                        k += 1
                if k != nice4:
                    if pause_flag_5 == 0 and start_flag_5 == 1:
                        lock.acquire(True)
                        rowid7 = int(k) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=11""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=5""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=11""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid7)}' WHERE ID=5""")
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid8 = int(k) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=5""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=5""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=11""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid8)}' WHERE ID=11""")
                        sqlite_connection.commit()
            except:
                lock.release()
                return run4()


def run5():
    l = 0
    global pool
    road = today.date().strftime("%d.%m.%Y")
    try:
        open(fr'\\PULT6\RailControl\log\{road}.txt')
        pool = 1
    except:
        pool = 0
        time.sleep(5)
        return run5()
    with open(fr'\\PULT6\RailControl\log\{road}.txt') as t5:
        while True:
            try:
                time.sleep(12)
                lock.acquire(True)
                nice5 = int((cursor.execute(f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=6""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) + int(
                    (cursor.execute(f"""SELECT clear FROM poll WHERE ID=12""")).fetchone()[0])
                lock.release()
                time.sleep(23)
                for line5 in t5:
                    if "total" in line5:
                        l += 1
                if l != nice5:
                    if pause_flag_6 == 0 and start_flag_6 == 1:
                        lock.acquire(True)
                        rowid9 = int(l) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=12""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=6""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=12""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid9)}' WHERE ID=6""")
                        sqlite_connection.commit()
                    else:
                        lock.acquire(True)
                        rowid10 = int(l) - int(
                            (cursor.execute(f"""SELECT current_main FROM poll WHERE ID=6""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=6""")).fetchone()[0]) - int(
                            (cursor.execute(f"""SELECT clear FROM poll WHERE ID=12""")).fetchone()[0])
                        lock.release()
                        cursor.execute(f"""UPDATE poll SET current_main='{str(rowid10)}' WHERE ID=12""")
                        sqlite_connection.commit()
            except:
                lock.release()
                return run5()


def connect():
    if pool == 1:
        form.checkBox.setStyleSheet("QCheckBox::indicator {background-color: qlineargradient"
                                    "(spread:pad, x1:0.447, y1:0.341, x2:1, y2:0, stop:0 rgba(66, 200, 77, 255), stop:1 rgba(221, 221, 221, 255));}")
    else:
        form.checkBox.setStyleSheet("QCheckBox::indicator {background: qlineargradient"
                                    "(spread:pad, x1:0, y1:0.29, x2:1, y2:0, stop:0.253731 rgba(164, 0, 0, 255), stop:1 rgba(255, 0, 40, 255));}")


def button_clicked12():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=12""")).fetchone()[0]) + " ?"))

    def fact():
        Reset12()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked11():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=6""")).fetchone()[0]) + " ?"))

    def fact():
        Reset11()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked10():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=11""")).fetchone()[0]) + " ?"))

    def fact():
        Reset10()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked9():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=5""")).fetchone()[0]) + " ?"))

    def fact():
        Reset9()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked8():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=10""")).fetchone()[0]) + " ?"))

    def fact():
        Reset8()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked7():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=4""")).fetchone()[0]) + " ?"))

    def fact():
        Reset7()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked6():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=9""")).fetchone()[0]) + " ?"))

    def fact():
        Reset6()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked5():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=3""")).fetchone()[0]) + " ?"))

    def fact():
        Reset5()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked4():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=8""")).fetchone()[0]) + " ?"))

    def fact():
        Reset4()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked3():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=2""")).fetchone()[0]) + " ?"))

    def fact():
        Reset3()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked2():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=7""")).fetchone()[0]) + " ?"))

    def fact():
        Reset2()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


def button_clicked1():
    Form, App = uic.loadUiType("dialog.ui")
    app = QDialog()
    form = Form()
    form.setupUi(app)
    app.show()
    form.label_2.setText((str((cursor.execute(f"""SELECT train FROM poll WHERE ID=1""")).fetchone()[0]) + " ?"))

    def fact():
        Reset1()
        app.close()

    def close():
        app.close()

    form.pushButton.clicked.connect(fact)
    form.pushButton_2.clicked.connect(close)
    app.exec()


today_z()
pool()
button()
button_pause()
button_start()
norma()
interval()
initialTrains()
minuts()
seconds()
progress_bar()
puff()
form.pushButton.clicked.connect(save)
thr1 = threading.Thread(target=run, daemon=True).start()
thr2 = threading.Thread(target=run1, daemon=True).start()
thr3 = threading.Thread(target=run2, daemon=True).start()
thr4 = threading.Thread(target=run3, daemon=True).start()
thr5 = threading.Thread(target=run4, daemon=True).start()
thr6 = threading.Thread(target=run5, daemon=True).start()
timer = QTimer(interval=30000, timeout=connect)
timer.start()
timer1 = QTimer(interval=30000, timeout=interval)
timer1.start()
timer2 = QTimer(interval=600000, timeout=progress_bar)
timer2.start()
app.exec()
if thr1 == True:
    daemon = False
