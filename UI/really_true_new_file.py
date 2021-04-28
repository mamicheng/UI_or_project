# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys,serial,time
import serial.tools.list_ports
import random

from PyQt5 import QtCore, QtGui, QtWidgets,QtChart
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    global ser

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465,759)
#框架部分
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 490, 441, 241))
        self.frame_4.setStyleSheet("QFrame\n"
"{\n"
"    border:2px solid grey;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 441, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
#选择栏部分
        # 串口选择与开关
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(140, 10, 261, 21))
        self.comboBox.setObjectName("comboBox")
        # 获取串口状态
        self.port_list = list(serial.tools.list_ports.comports())

        for i in range(0,len(self.port_list)):
            self.comboBox.addItem(str(self.port_list[i]))

#编辑栏部分
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 270, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        #整数校验器，准对于延时分钟设定
        intValidator2 = QIntValidator(self)
        intValidator2.setRange(0, 59)
        self.lineEdit.setValidator(intValidator2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 270, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 整数校验器，准对于延时每秒设定
        self.lineEdit_2.setValidator(intValidator2)

        self.setTemperature = QtWidgets.QLineEdit(self.frame)
        self.setTemperature.setGeometry(QtCore.QRect(110, 90, 111, 21))
        self.setTemperature.setObjectName("lineEdit_3")
        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(0, 99)
        self.setTemperature.setValidator(intValidator)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 310, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        # 整数校验器，准对于延时分钟设定
        self.lineEdit_4.setValidator(intValidator2)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 310, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        # 整数校验器，准对于延时每秒设定
        self.lineEdit_5.setValidator(intValidator2)
#标签部分
        #可变标签
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(180, 450, 161, 16))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(180, 350, 171, 16))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label")

        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(180, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        #不可变标签
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 111, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(11)
        # 动态显示时间
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        timer_1 = QTimer(self)
        timer_1.timeout.connect(self.showtime)
        timer_1.start()

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(200, 270, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(310, 270, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(200, 310, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(310, 310, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(100, 120, 201, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(20, 120, 61, 31))
        self.label_14.setStyleSheet("label.setFrameStyle(QFrame::NoFrame);")
        self.label_14.setLineWidth(1)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setObjectName("label_15")

#按钮部分
        #设置温度+1按钮
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendTextA1)
        #设置温度-1按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 130, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.sendTextA2)
        #温度设置确定按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 90, 81, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sendTextA0)
        #设置退出按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.endProgram)
        # 打开和关闭串口按钮
        self.openPortBotton = QtWidgets.QPushButton(self.frame_4)
        self.openPortBotton.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.openPortBotton.setObjectName("pushButton_5")
        self.openPortBotton.setCheckable(True)
        self.closePortBotton = QtWidgets.QPushButton(self.frame_4)
        self.closePortBotton.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.closePortBotton.setObjectName("pushButton_6")
        self.closePortBotton.setCheckable(True)
        self.openPortBotton.setEnabled(True)
        self.closePortBotton.setEnabled(False)
        self.timer_2 = QTimer(self)
        self.openPortBotton.clicked.connect(self.openPort)
        self.closePortBotton.clicked.connect(self.closePort)
        # 设置开始调节温度命令按钮
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.sendTextA6__1)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setEnabled(True)
        # 设置停止温度调节命令按钮
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 180, 111, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.sendTextA6__2)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setEnabled(False)
        #延时启动确定按钮
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 270, 81, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.sendTextA4)
        #延时停止时间发送按钮
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 310, 81, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.sendTextA5)
        #延时启动时间查询按钮
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 440, 151, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.getStartTimeAA)
        #延时停止时间查询按钮
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 390, 151, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.getStopTimeAB)
        #当前状态查询按钮
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 342, 151, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.getConditionAE)
        #pc开始调节按钮
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(320, 180, 111, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.sendTextA3__2)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setEnabled(False)
        #温度查询按钮
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 60, 81, 23))
        self.pushButton_15.setObjectName("pushButton")
        self.pushButton_15.clicked.connect(self.getTextA8)
        #PC停止调节按钮
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(320, 130, 111, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.sendTextA3__1)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setEnabled(True)

        #绘制坐标系
        self.timer_3 = QTimer(self)
        self.timer_3.timeout.connect(self.drawLine)
        self.timer_3.start(1000)

        self.chartview = QChartView()
        self.chartview.setGeometry(470,0,720,720)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.chart = QChart()
        self.series = QSplineSeries()
        # 设置曲线名称
        self.series.setName("实时数据")
        # 把曲线添加到QChart的实例中
        self.chart.addSeries(self.series)
        # 声明并初始化X轴，Y轴
        self.dtaxisX = QDateTimeAxis()
        self.vlaxisY = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-300 * 1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(1500)
        # 设置X轴时间样式
        self.dtaxisX.setFormat("MM月dd hh:mm:ss")
        # 设置坐标轴上的格点
        self.dtaxisX.setTickCount(6)
        self.vlaxisY.setTickCount(11)
        # 设置坐标轴名称
        self.dtaxisX.setTitleText("时间")
        self.vlaxisY.setTitleText("温度")
        # 设置网格不显示
        self.vlaxisY.setGridLineVisible(True)
        # 把坐标轴添加到chart中
        self.chart.addAxis(self.dtaxisX, Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series.attachAxis(self.dtaxisX)
        self.series.attachAxis(self.vlaxisY)

        self.chartview.setChart(self.chart)
        self.chartview.show()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "退出"))
        self.openPortBotton.setText(_translate("MainWindow", "打开串口"))
        self.closePortBotton.setText(_translate("MainWindow", "关闭串口"))
        self.label_13.setText(_translate("MainWindow", "进行下一步操作前请确定串口已打开"))
        self.label_14.setText(_translate("MainWindow", "warning："))
        self.label_15.setText(_translate("MainWindow", "请选择串口："))
        self.label_5.setText(_translate("MainWindow", "控制面板"))
        self.pushButton_3.setText(_translate("MainWindow", "确定"))
        self.label_2.setText(_translate("MainWindow", "设置温度(A0)："))
        self.label_6.setText(_translate("MainWindow", "当前温度(A8)："))
        self.label.setText(_translate("MainWindow", "currentTemp"))
        self.pushButton.setText(_translate("MainWindow", "温度+1(A1)"))
        self.pushButton_2.setText(_translate("MainWindow", "温度-1（A2)"))
        self.pushButton_7.setText(_translate("MainWindow", "开始调节温度（A6)"))
        self.pushButton_8.setText(_translate("MainWindow", "停止调节温度（A6)"))
        self.label_10.setText(_translate("MainWindow", "当前时间："))
        self.label_4.setText(_translate("MainWindow", "currentTime"))
        self.pushButton_9.setText(_translate("MainWindow", "确定"))
        self.label_3.setText(_translate("MainWindow", "设定延时启动（A4)"))
        self.label_7.setText(_translate("MainWindow", "分"))
        self.label_8.setText(_translate("MainWindow", "秒"))
        self.label_9.setText(_translate("MainWindow", "设定延时停止（A5)"))
        self.label_11.setText(_translate("MainWindow", "分"))
        self.label_12.setText(_translate("MainWindow", "秒"))
        self.pushButton_10.setText(_translate("MainWindow", "确定"))
        self.label_18.setText(_translate("MainWindow", "currentDelayStartTime"))
        self.label_19.setText(_translate("MainWindow", "currentDelayStopTime"))
        self.pushButton_11.setText(_translate("MainWindow", "当前状态查询（AE)"))
        self.pushButton_12.setText(_translate("MainWindow", "延时停止时间查询（AB)"))
        self.pushButton_13.setText(_translate("MainWindow", "延时启动时间查询（AA)"))
        self.label_16.setText(_translate("MainWindow", "currentCondition"))
        self.pushButton_15.setText(_translate("MainWindow","查询"))
        self.pushButton_14.setText(_translate("MainWindow", "PC停止调节（A3)"))
        self.pushButton_16.setText(_translate("MainWindow", "PC开始调节(A3)"))
    #系统退出
    def endProgram(self):
        sys.exit()
    #动态上传时间
    def showtime(self):
        time=QTime.currentTime()
        text = time.toString()
        self.label_4.setText(text)

    def drawLine(self):
        # 获取当前时间
        bjtime = QDateTime.currentDateTime()
        # 更新X轴坐标
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-300 * 1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        # 当曲线上的点超出X轴的范围时，移除最早的点
        if (self.series.count() > 149):
            self.series.removePoints(0, self.series.count() - 149)
        # 产生随即数
        yint = random.randint(0,1500)
        # 添加数据到曲线末端
        self.series.append(bjtime.toMSecsSinceEpoch(), yint)

    #打开串口
    def openPort(self):
        self.timer_2.start()
        #串口配对
        for i in range(0,len(self.port_list)) :
            if self.comboBox.currentText()==str(self.port_list[i]) :
                text = str(self.port_list[i])
                port = text[0:4]
                try:
                    self.ser = serial.Serial(port, baudrate=9600, bytesize=8, parity='N', stopbits=1)
                    print(self.ser)
                except Exception as e:
                    print(str(e))
                finally:
                    break
            elif i==len(self.port_list):
                print("未检测到接口")
                break

        self.openPortBotton.setEnabled(False)
        self.closePortBotton.setEnabled(True)

    #关闭串口
    def closePort(self):
        self.timer_2.stop()
        ser.close()
        self.openPortBotton.setEnabled(True)
        self.closePortBotton.setEnabled(False)

    #传入设定温度至下位机,A0操作
    def sendTextA0(self):
        try:
            sendTextArray=[]
            setTemp = str(self.setTemperature.text())
            i=0
            if self.setTemperature.text() != "":
                sendTextArray.append(b'C')
                sendTextArray.append(b'O')
                sendTextArray.append(b'M')
                sendTextArray.append(0xA0)
                sendTextArray.append(bytes(setTemp.encode('utf-8')))
                sendTextArray.append(0xFF)

                for i in range(0,len(sendTextArray)-1):
                    self.ser.write(sendTextArray[i])
                print("OKA0")
        except Exception as e:
                print(str(e))

    #温度+1操作
    def sendTextA1(self):
        try:
            sendTextArray = []
            i = 0
            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA1)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0, len(sendTextArray) - 1):
                self.ser.write(sendTextArray[i])
            print("OKA1")
        except Exception as e:
            print(str(e))
    #温度-1操作
    def sendTextA2(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA2)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            print("OKA2")
        except Exception as e:
            print(str(e))
    def sendTextA3__1(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA3)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            self.pushButton_14.setEnabled(True)
            self.pushButton_16.setEnabled(False)
            print("OKA3__1")
        except Exception as e:
            print(str(e))

    def sendTextA3__2(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA3)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            self.pushButton_14.setEnabled(False)
            self.pushButton_16.setEnabled(True)
            print("OKA3__2")
        except Exception as e:
            print(str(e))


    def sendTextA4(self):
        try:
            sendTextArray=[]
            i=0
            setMin = str(self.lineEdit.text())
            setSec = str(self.lineEdit_2.text())
            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA4)
            sendTextArray.append(bytes(setMin.encode('utf-8')))
            sendTextArray.append(bytes(setSec.encode('utf-8')))

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            print("OKA4")
        except Exception as e:
            print(str(e))

    def sendTextA5(self):
        try:
            sendTextArray=[]
            i=0
            setMin2 = str(self.lineEdit_4.text())
            setSec2 = str(self.lineEdit_5.text())
            if setMin2 == "":
                setMin2 = 0
            if setSec2 == "":
                setSec2 = 0
            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA5)
            sendTextArray.append(bytes(setMin2.encode('utf-8')))
            sendTextArray.append(bytes(setSec2.encode('utf-8')))

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            print('OKA5')
        except Exception as e:
            print(str(e))

    def sendTextA6__1(self):
        try:
            sendTextArray = []
            i = 0
            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA6)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])

            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(True)

            print('OKA6__1')
        except Exception as e:
            print(str(e))

    def sendTextA6__2(self):
        try:
            sendTextArray = []
            i = 0
            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA6)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0, len(sendTextArray) - 1):
                self.ser.write(sendTextArray[i])

            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(False)

            print('OKA6__2')
        except Exception as e:
            print(str(e))

    #读取当前温度，A8操作
    def getTextA8(self):
        try:
            sendTextArray = []
            i = 0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xA8)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray) - 1):
                self.ser.write(sendTextArray[i])
            temp=1
            #temp=self.ser.read().decode()
            if temp != None:
                self.label.setText(str(temp))
            print('OKA8')
        except Exception as e:
            print(str(e))

    #读取当前延迟启动时间，AA操作
    def getStartTimeAA(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xAA)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)
            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            temp=1
            #temp = self.ser.read().decode()
            if temp != None:
                self.label_16.setText(str(temp))
            print('OKAA')
        except Exception as e:
            print(str(e))

    #读取当前延迟停止时间，AB操作
    def getStopTimeAB(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xAB)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            temp = 1
            #temp = ser.read().decode()
            if temp != None:
                self.label_19.setText(str(temp))
            print('OKAB')
        except Exception as e:
            print(str(e))

    #获取当前状态，AE操作
    def getConditionAE(self):
        try:
            sendTextArray=[]
            i=0

            sendTextArray.append(b'C')
            sendTextArray.append(b'O')
            sendTextArray.append(b'M')
            sendTextArray.append(0xAE)
            sendTextArray.append(0xFF)
            sendTextArray.append(0xFF)

            for i in range(0,len(sendTextArray)-1):
                self.ser.write(sendTextArray[i])
            temp=1
            #temp = self.ser.read().decode()
            if temp != None:
                self.label_18.setText(str(temp))
            print('OKAE')
        except Exception as e:
            print(str(e))


