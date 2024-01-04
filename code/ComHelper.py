import serial
import serial.tools.list_ports
import datetime
import openpyxl
import os
import time

import CH_UI
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
import sys


# selected_port = input("Select port: ")


# baudrate = input("Baudrate: ")
# bytesize = serial.EIGHTBITS
# parity = serial.PARITY_NONE
# stopbits = serial.STOPBITS_ONE

# workbook = openpyxl.Workbook( )
# sheet = workbook.active
# sheet['A1'] = "Time"

# ser = serial.Serial(selected_port, baudrate, bytesize, parity, stopbits,timeout = 5)

# if ser.isOpen():
#     ser.close()
#     time.sleep(1)
#     ser.open()
# else:
#     ser.open()

# name = 'Comdata'
# num = 0
# sheet.append([0])
# workbook.save(name + str(num) + '.xlsx')


# size = os.path.getsize(name + str(num) + '.xlsx')


class ComHelper(QMainWindow, CH_UI.Ui_MainWindow):
    def __init__(self):
        super(ComHelper, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":

    baudrate = 9600
    bytesize = serial.EIGHTBITS
    parity = serial.PARITY_NONE
    stopbits = serial.STOPBITS_ONE

    ser = serial.Serial("COM1-vir", 9600, bytesize, parity, stopbits,timeout = 5)
    ser.open()

    # app = QApplication(sys.argv)
    # MainWindow = ComHelper()
    # # ui = CH_UI.Ui_MainWindow()
    # # ui.setupUi(MainWindow)

    # MainWindow.show()##��ʾ

    # sys.exit(app.exec_())##�˳�����


    # while True:
    #     if size < 10000000:
    #         data = ser.read_all()
    #         if data:
    #             line = HexStrAddSpace(data.hex().strip())
    #             now = datetime.datetime.now()
    #             mill = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    #             print("Time : " + mill + "    " + line)

    #             sheet.append([mill + line])
    #             workbook.save(name + str(num) + '.xlsx')

    #             size = os.path.getsize(name + str(num) + '.xlsx')
    #         else:
    #             print("No Data")
    #             time.sleep(0.1)
    #     else:
    #         num +=1
    #         workbook = openpyxl.Workbook( )
    #         sheet = workbook.active
    #         sheet['A1'] = "Time"
    #         workbook.save(name + str(num) + '.xlsx')
    #         size = os.path.getsize(name + str(num) + '.xlsx')
