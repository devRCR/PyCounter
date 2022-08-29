# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 555)
        MainWindow.setMinimumSize(QtCore.QSize(333, 555))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(80, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/rad_shield.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_data.sizePolicy().hasHeightForWidth())
        self.lineEdit_data.setSizePolicy(sizePolicy)
        self.lineEdit_data.setMaximumSize(QtCore.QSize(1000, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(70)
        self.lineEdit_data.setFont(font)
        self.lineEdit_data.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.lineEdit_data.setFrame(False)
        self.lineEdit_data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_data.setReadOnly(True)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.gridLayout_3.addWidget(self.lineEdit_data, 1, 1, 1, 1)
        self.lineEdit_type = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_type.setSizePolicy(sizePolicy)
        self.lineEdit_type.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_type.setFont(font)
        self.lineEdit_type.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.lineEdit_type.setFrame(False)
        self.lineEdit_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_type.setReadOnly(True)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.gridLayout_3.addWidget(self.lineEdit_type, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.radioButton_cps = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_cps.setChecked(True)
        self.radioButton_cps.setObjectName("radioButton_cps")
        self.horizontalLayout_5.addWidget(self.radioButton_cps)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.radioButton_rate = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_rate.setObjectName("radioButton_rate")
        self.horizontalLayout_5.addWidget(self.radioButton_rate)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_ComPort = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ComPort.sizePolicy().hasHeightForWidth())
        self.comboBox_ComPort.setSizePolicy(sizePolicy)
        self.comboBox_ComPort.setMinimumSize(QtCore.QSize(100, 28))
        self.comboBox_ComPort.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_ComPort.setObjectName("comboBox_ComPort")
        self.horizontalLayout.addWidget(self.comboBox_ComPort)
        self.pushButton_UpdatePorts = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_UpdatePorts.sizePolicy().hasHeightForWidth())
        self.pushButton_UpdatePorts.setSizePolicy(sizePolicy)
        self.pushButton_UpdatePorts.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_UpdatePorts.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton_UpdatePorts.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../GCounter/Images/refresh_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_UpdatePorts.setIcon(icon)
        self.pushButton_UpdatePorts.setIconSize(QtCore.QSize(32, 20))
        self.pushButton_UpdatePorts.setObjectName("pushButton_UpdatePorts")
        self.horizontalLayout.addWidget(self.pushButton_UpdatePorts)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_BaudRate = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_BaudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_BaudRate.setSizePolicy(sizePolicy)
        self.comboBox_BaudRate.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_BaudRate.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_BaudRate.setFont(font)
        self.comboBox_BaudRate.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_BaudRate.setAutoFillBackground(False)
        self.comboBox_BaudRate.setObjectName("comboBox_BaudRate")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_BaudRate)
        self.pushButton_OpenClosePort = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OpenClosePort.sizePolicy().hasHeightForWidth())
        self.pushButton_OpenClosePort.setSizePolicy(sizePolicy)
        self.pushButton_OpenClosePort.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_OpenClosePort.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_OpenClosePort.setFont(font)
        self.pushButton_OpenClosePort.setObjectName("pushButton_OpenClosePort")
        self.horizontalLayout_2.addWidget(self.pushButton_OpenClosePort)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../GCounter/Images/logo-ipen.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.pushButton_Salir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.horizontalLayout_6.addWidget(self.pushButton_Salir)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 21))
        self.menubar.setObjectName("menubar")
        self.menuDile = QtWidgets.QMenu(self.menubar)
        self.menuDile.setObjectName("menuDile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "MONITOR GEIGER"))
        self.lineEdit_data.setText(_translate("MainWindow", "0"))
        self.lineEdit_type.setText(_translate("MainWindow", "cps"))
        self.radioButton_cps.setText(_translate("MainWindow", "cps"))
        self.radioButton_rate.setText(_translate("MainWindow", "Tasa de dosis"))
        self.label_2.setText(_translate("MainWindow", "Puerto COM:"))
        self.label_3.setText(_translate("MainWindow", "Baud Rate:     "))
        self.comboBox_BaudRate.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_BaudRate.setItemText(1, _translate("MainWindow", "19200"))
        self.comboBox_BaudRate.setItemText(2, _translate("MainWindow", "38400"))
        self.comboBox_BaudRate.setItemText(3, _translate("MainWindow", "115200"))
        self.pushButton_OpenClosePort.setText(_translate("MainWindow", "Abrir Puerto"))
        self.pushButton_Salir.setText(_translate("MainWindow", "SALIR"))
        self.menuDile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

