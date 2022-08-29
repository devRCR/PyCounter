#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os, time
from SerialThread import *
from gui import *

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)

		self.mySerial = SerialPort()
		self.ListPorts()

		self.radioButton_cps.setChecked(True)
		self.conv_factor = 0.252

		self.pushButton_UpdatePorts.clicked.connect(self.ListPorts)
		self.pushButton_OpenClosePort.clicked.connect(self.OpenClosePort)
		self.mySerial.msg_str.connect(self.PlotData)
		self.pushButton_Salir.clicked.connect(self.Salir)
		self.radioButton_cps.toggled.connect(self.TipoDato)
		self.radioButton_rate.toggled.connect(self.TipoDato)

	def ListPorts(self):
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(20)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = ['/dev/ttyACM%s' % i for i in range(20)]
			for i in range(20):
				ports.append('/dev/ttyUSB%s' % i)
		else:
			raise EnvironmentError('Unsupported platform')
		result = []
		for port in ports:
			self.mySerial.OpenList(port)
			if self.mySerial.IsOpen() == True:
				result.append(port)
			self.mySerial.Close()
		self.comboBox_ComPort.clear()
		self.comboBox_ComPort.addItems(result)

	def OpenClosePort(self):
		if self.pushButton_OpenClosePort.text() == 'Open Port':
			comport = self.comboBox_ComPort.currentText()
			baudrate = self.comboBox_BaudRate.currentText()
			self.mySerial.Open(comport,baudrate)
			if self.mySerial.IsOpen() == True:
				self.mySerial.start()
				self.pushButton_OpenClosePort.setText('Close Port')

				self.comboBox_BaudRate.setEnabled(False)
				self.comboBox_ComPort.setEnabled(False)
				self.pushButton_UpdatePorts.setEnabled(False)


		elif self.pushButton_OpenClosePort.text() == 'Close Port':
			self.mySerial.Close()
			if self.mySerial.IsOpen() == False:
				self.pushButton_OpenClosePort.setText('Open Port')
				self.comboBox_BaudRate.setEnabled(True)
				self.comboBox_ComPort.setEnabled(True)
				self.pushButton_UpdatePorts.setEnabled(True)
				self.mySerial.terminate()

	def PlotData(self,stringData):
		if len(stringData) != 0:
			self.getData=True
			if self.radioButton_cps.isChecked() == True:
				self.lineEdit_data.setText(stringData[18:len(stringData)])
			else:
				aux = float(stringData[18:len(stringData)])*self.conv_factor
				self.lineEdit_data.setText(str(aux))
			
	def TipoDato(self):
		if self.radioButton_cps.isChecked() == True:
			self.lineEdit_type.setText("cps")
		else:
			self.lineEdit_type.setText("uSv/h")

	def Salir(self):
		self.mySerial.Close()
		self.mySerial.terminate()
		#time.sleep(1)
		sys.exit()

if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
