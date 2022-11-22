# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 611, 1021, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 580, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox_Temperature = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Temperature.setGeometry(QtCore.QRect(620, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Temperature.setFont(font)
        self.checkBox_Temperature.setChecked(True)
        self.checkBox_Temperature.setObjectName("checkBox_Temperature")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.checkBox_Temperature)
        self.checkBox_Depth = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Depth.setGeometry(QtCore.QRect(720, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Depth.setFont(font)
        self.checkBox_Depth.setChecked(True)
        self.checkBox_Depth.setObjectName("checkBox_Depth")
        self.buttonGroup.addButton(self.checkBox_Depth)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 560, 1041, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 125, 1041, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openfile.setGeometry(QtCore.QRect(820, 85, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_openfile.setFont(font)
        self.pushButton_openfile.setObjectName("pushButton_openfile")
        self.lineEdit_showpath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_showpath.setGeometry(QtCore.QRect(190, 90, 611, 21))
        self.lineEdit_showpath.setObjectName("lineEdit_showpath")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 180, 981, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Presure = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Presure.setGeometry(QtCore.QRect(820, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Presure.setFont(font)
        self.checkBox_Presure.setChecked(True)
        self.checkBox_Presure.setObjectName("checkBox_Presure")
        self.checkBox_Size = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Size.setGeometry(QtCore.QRect(920, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Size.setFont(font)
        self.checkBox_Size.setChecked(True)
        self.checkBox_Size.setObjectName("checkBox_Size")
        self.pushButton_openfile_xls = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openfile_xls.setGeometry(QtCore.QRect(940, 85, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_openfile_xls.setFont(font)
        self.pushButton_openfile_xls.setObjectName("pushButton_openfile_xls")
        self.pushButton_xs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_xs.setGeometry(QtCore.QRect(140, 150, 91, 23))
        self.pushButton_xs.setObjectName("pushButton_xs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 23))
        self.menubar.setObjectName("menubar")
        self.menu_shezhi = QtWidgets.QMenu(self.menubar)
        self.menu_shezhi.setObjectName("menu_shezhi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_shuchu = QtWidgets.QAction(MainWindow)
        self.action_shuchu.setObjectName("action_shuchu")
        self.menu_shezhi.addAction(self.action_shuchu)
        self.menubar.addAction(self.menu_shezhi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "深水钻孔取样贯入装置动态检测数据采集软件"))
        self.label.setText(_translate("MainWindow", "实 时 数 据 显 示"))
        self.label_2.setText(_translate("MainWindow", "读入文件路径："))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "温度(℃)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "深度(CM)"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "压力"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "速度"))
        self.label_3.setText(_translate("MainWindow", "趋势显示："))
        self.label_4.setText(_translate("MainWindow", "数值显示："))
        self.checkBox_Temperature.setText(_translate("MainWindow", "温度"))
        self.checkBox_Depth.setText(_translate("MainWindow", "深度"))
        self.pushButton_openfile.setText(_translate("MainWindow", "打开.txt文件"))
        self.lineEdit_showpath.setPlaceholderText(_translate("MainWindow", "请点击打开日志文件"))
        self.checkBox_Presure.setText(_translate("MainWindow", "压力"))
        self.checkBox_Size.setText(_translate("MainWindow", "速度"))
        self.pushButton_openfile_xls.setText(_translate("MainWindow", "打开.xls文件"))
        self.pushButton_xs.setText(_translate("MainWindow", "显示全部趋势"))
        self.menu_shezhi.setTitle(_translate("MainWindow", "设置"))
        self.action_shuchu.setText(_translate("MainWindow", "确认开机采样时间和频率"))
