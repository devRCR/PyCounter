import serial, sys
from PyQt5.QtCore import pyqtSignal, QThread, QObject

class SerialPort(QThread):
	msg_byte=pyqtSignal(bytes)
	msg_str =pyqtSignal(str)

	def __init__(self, parent=None):
		super(SerialPort,self).__init__(parent)
		self.baud = 0
		self.timeout = None
		self.isopen = False
		self.seriport=serial.Serial()

	def __del__(self):
		self.seriport.close()
		#self.wait()

	def IsOpen(self):
		return self.isopen
		print("puerto abierto")

	def Open(self, portname, baudrate):
		self.seriport.port = portname
		self.seriport.baudrate = baudrate
		try:
			self.seriport.open()
			self.isopen = True
			print("Puerto abierto :", self.seriport.port)
		except (OSError, serial.SerialException):
			pass

	def OpenList(self, portname):
		if self.isopen == False:
			self.seriport.port = portname
			try:
				self.seriport.open()
				self.isopen = True
			except (OSError, serial.SerialException):
				pass

	def Close(self):
		if self.isopen:
			try:
				self.seriport.close()
				self.isopen=False
				print("Puerto Cerrado: ", self.seriport.port)
			except:
				pass

	def Send(self,message):
		newmessage = message.strip()
		newmessage += '\r\n'
		self.seriport.write(newmessage.encode('utf-8'))

	def run(self):
		while True:
			try:
				if self.isopen:
					stringData = self.seriport.read_until(b'\r').decode('utf-8').strip()
					self.msg_str.emit(stringData) # pipeline
					# print(stringData)
			except:
				pass
