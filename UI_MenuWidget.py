# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MenuWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(1600, 900)
        MenuWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MenuWindow.setMaximumSize(QtCore.QSize(1600, 900))
        self.horizontalLayoutWidget = QtWidgets.QWidget(MenuWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 604, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MarketInfoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MarketInfoButton.setMinimumSize(QtCore.QSize(0, 30))
        self.MarketInfoButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MarketInfoButton.setFont(font)
        self.MarketInfoButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.MarketInfoButton.setObjectName("MarketInfoButton")
        self.horizontalLayout.addWidget(self.MarketInfoButton)
        self.SelectStocksButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SelectStocksButton.setMinimumSize(QtCore.QSize(0, 30))
        self.SelectStocksButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SelectStocksButton.setFont(font)
        self.SelectStocksButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.SelectStocksButton.setObjectName("SelectStocksButton")
        self.horizontalLayout.addWidget(self.SelectStocksButton)
        self.TradeStrategyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TradeStrategyButton.setMinimumSize(QtCore.QSize(0, 30))
        self.TradeStrategyButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TradeStrategyButton.setFont(font)
        self.TradeStrategyButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.TradeStrategyButton.setObjectName("TradeStrategyButton")
        self.horizontalLayout.addWidget(self.TradeStrategyButton)
        self.SimulateTradeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SimulateTradeButton.setMinimumSize(QtCore.QSize(0, 30))
        self.SimulateTradeButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SimulateTradeButton.setFont(font)
        self.SimulateTradeButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.SimulateTradeButton.setObjectName("SimulateTradeButton")
        self.horizontalLayout.addWidget(self.SimulateTradeButton)
        self.QuantAnalysisButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.QuantAnalysisButton.setMinimumSize(QtCore.QSize(0, 30))
        self.QuantAnalysisButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QuantAnalysisButton.setFont(font)
        self.QuantAnalysisButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.QuantAnalysisButton.setObjectName("QuantAnalysisButton")
        self.horizontalLayout.addWidget(self.QuantAnalysisButton)
        self.UserFunctionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.UserFunctionButton.setMinimumSize(QtCore.QSize(0, 30))
        self.UserFunctionButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserFunctionButton.setFont(font)
        self.UserFunctionButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 30, 0);\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(0, 0, 255);\n"
"}")
        self.UserFunctionButton.setObjectName("UserFunctionButton")
        self.horizontalLayout.addWidget(self.UserFunctionButton)
        self.ContentWidget = QtWidgets.QWidget(MenuWindow)
        self.ContentWidget.setGeometry(QtCore.QRect(0, 30, 1600, 870))
        self.ContentWidget.setMinimumSize(QtCore.QSize(1600, 870))
        self.ContentWidget.setMaximumSize(QtCore.QSize(1600, 870))
        self.ContentWidget.setObjectName("ContentWidget")
        self.TopLine = QtWidgets.QLabel(MenuWindow)
        self.TopLine.setGeometry(QtCore.QRect(0, 30, 1600, 1))
        self.TopLine.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.TopLine.setText("")
        self.TopLine.setObjectName("TopLine")

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "量化金融"))
        self.MarketInfoButton.setText(_translate("MenuWindow", "股市资讯"))
        self.SelectStocksButton.setText(_translate("MenuWindow", "自选股票"))
        self.TradeStrategyButton.setText(_translate("MenuWindow", "交易策略"))
        self.SimulateTradeButton.setText(_translate("MenuWindow", "模拟交易"))
        self.QuantAnalysisButton.setText(_translate("MenuWindow", "量化分析"))
        self.UserFunctionButton.setText(_translate("MenuWindow", "用户功能"))


