# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MarketInfoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarketInfoWindow(object):
    def setupUi(self, MarketInfoWindow):
        MarketInfoWindow.setObjectName("MarketInfoWindow")
        MarketInfoWindow.resize(1600, 870)
        MarketInfoWindow.setMinimumSize(QtCore.QSize(1600, 870))
        MarketInfoWindow.setMaximumSize(QtCore.QSize(1600, 870))
        self.verticalLayoutWidget = QtWidgets.QWidget(MarketInfoWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 102, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ShenhuStockButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ShenhuStockButton.setMinimumSize(QtCore.QSize(100, 30))
        self.ShenhuStockButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ShenhuStockButton.setFont(font)
        self.ShenhuStockButton.setStyleSheet("QPushButton{\n"
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
        self.ShenhuStockButton.setObjectName("ShenhuStockButton")
        self.verticalLayout.addWidget(self.ShenhuStockButton)
        self.ShenhuExponentButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ShenhuExponentButton.setMinimumSize(QtCore.QSize(100, 30))
        self.ShenhuExponentButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ShenhuExponentButton.setFont(font)
        self.ShenhuExponentButton.setStyleSheet("QPushButton{\n"
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
        self.ShenhuExponentButton.setObjectName("ShenhuExponentButton")
        self.verticalLayout.addWidget(self.ShenhuExponentButton)
        self.NewStockIPOButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.NewStockIPOButton.setMinimumSize(QtCore.QSize(100, 30))
        self.NewStockIPOButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NewStockIPOButton.setFont(font)
        self.NewStockIPOButton.setStyleSheet("QPushButton{\n"
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
        self.NewStockIPOButton.setObjectName("NewStockIPOButton")
        self.verticalLayout.addWidget(self.NewStockIPOButton)
        self.FundBondsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.FundBondsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.FundBondsButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FundBondsButton.setFont(font)
        self.FundBondsButton.setStyleSheet("QPushButton{\n"
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
        self.FundBondsButton.setObjectName("FundBondsButton")
        self.verticalLayout.addWidget(self.FundBondsButton)
        self.OptionsMarketButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OptionsMarketButton.setMinimumSize(QtCore.QSize(100, 30))
        self.OptionsMarketButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OptionsMarketButton.setFont(font)
        self.OptionsMarketButton.setStyleSheet("QPushButton{\n"
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
        self.OptionsMarketButton.setObjectName("OptionsMarketButton")
        self.verticalLayout.addWidget(self.OptionsMarketButton)
        self.HotInfoButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.HotInfoButton.setMinimumSize(QtCore.QSize(100, 30))
        self.HotInfoButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HotInfoButton.setFont(font)
        self.HotInfoButton.setStyleSheet("QPushButton{\n"
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
        self.HotInfoButton.setObjectName("HotInfoButton")
        self.verticalLayout.addWidget(self.HotInfoButton)
        self.LeftLine = QtWidgets.QLabel(MarketInfoWindow)
        self.LeftLine.setGeometry(QtCore.QRect(100, 0, 1, 870))
        self.LeftLine.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LeftLine.setText("")
        self.LeftLine.setObjectName("LeftLine")
        self.ContentWidget = QtWidgets.QWidget(MarketInfoWindow)
        self.ContentWidget.setGeometry(QtCore.QRect(100, 0, 1500, 870))
        self.ContentWidget.setMinimumSize(QtCore.QSize(1500, 870))
        self.ContentWidget.setMaximumSize(QtCore.QSize(1500, 870))
        self.ContentWidget.setObjectName("ContentWidget")
        self.verticalLayoutWidget.raise_()
        self.ContentWidget.raise_()
        self.LeftLine.raise_()

        self.retranslateUi(MarketInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(MarketInfoWindow)

    def retranslateUi(self, MarketInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        MarketInfoWindow.setWindowTitle(_translate("MarketInfoWindow", "Form"))
        self.ShenhuStockButton.setText(_translate("MarketInfoWindow", "深沪个股"))
        self.ShenhuExponentButton.setText(_translate("MarketInfoWindow", "深沪指数"))
        self.NewStockIPOButton.setText(_translate("MarketInfoWindow", "新股IPO"))
        self.FundBondsButton.setText(_translate("MarketInfoWindow", "基金债券"))
        self.OptionsMarketButton.setText(_translate("MarketInfoWindow", "期权市场"))
        self.HotInfoButton.setText(_translate("MarketInfoWindow", "热点资讯"))


