from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from MarketInfo.UI_ShenhuStockWidget import Ui_ShenhuStockWindow
import GlobalData


class ShenhuStockItem():
    def __init__(self, ItemLabelList, LeftButton, RightButton, TotalStockRow):
        self.ItemLabelList = ItemLabelList
        self.LeftButton = LeftButton
        self.RightButton = RightButton
        for ItemLabel in self.ItemLabelList:
            ItemLabel.setStyleSheet("color: rgb(208, 208, 208);font-size:16px;")
            ItemLabel.setText("bilibi")

class ShenhuStockWidget(QWidget, Ui_ShenhuStockWindow):
    def __init__(self, parent = None):
        super(ShenhuStockWidget,self).__init__(parent)
        self.setupUi(self)

        # 生成各个界面保存到本地
        self.CreatePanel()
        # 初始化数据参数
        self.InitData()
        # 绑定按钮事件
        self.BindEvent()

    def CreatePanel(self):
        pass

    def InitData(self):
        #获取股票数量
        StockCount = len(GlobalData.GetValue("TotalStock"))
        #设置self.OrderContentWidget高度
        self.OrderContentWidget.setMinimumHeight(StockCount * 20)
        self.OrderContentWidget.setMaximumHeight(StockCount * 20)
        self.LeftContentWidget.setMinimumHeight(StockCount * 20)
        self.LeftContentWidget.setMaximumHeight(StockCount * 20)
        self.ScrollContentWidget.setMinimumHeight(StockCount * 20)
        self.ScrollContentWidget.setMaximumHeight(StockCount * 20)

        #设置ParamButton的选中和不被选中的样式
        self.ParamButtonSelectStyle = "background-color: rgb(0, 0, 0); color: rgb(255, 215, 0);"
        self.ParamButtonUnSelectStyle = "background-color: rgb(0, 0, 0); color: rgb(168, 168, 168);"
        #填充按钮逐渐到列表
        self.ParamButtonList = [self.SymbolButton, self.NameButton, self.TotalMVButton, self.TotalShareButton, self.CloseButton, self.TurnOverRateButton, self.VolumeRatioButton, self.IndustryButton, self.PEButton, self.PETTMButton, self.PBButton, self.PSButton, self.PSTTMButton, self.CircMvButton, self.FloatShareButton, self.FreeShareButton]
        #循环设定按钮样式
        for ParamButton in self.ParamButtonList:
            ParamButton.setStyleSheet(self.ParamButtonUnSelectStyle)

        #设定股票item列表
        self.StockItemList = []

        return

        #设定循环股票序号
        StockIndex = 1
        #绘制序号的画笔
        OrderPainter = QPainter()
        OrderPainter.begin(self.OrderContentWidget)
        print(OrderPainter.isActive())
        OrderPainter.setPen(QColor(208, 208, 208, 255))
        OrderPainter.setFont(QFont("Arial", 16))
        #循环生成组件
        for TotalStockRow in GlobalData.GetValue("TotalStock").itertuples():
            #生成序列
            OrderPainter.drawText(QRect(0, 20 * (StockIndex - 1), 50, 20), QtCore.Qt.AlignCenter, str(StockIndex))


            #序号加1
            StockIndex += 1
        OrderPainter.end()


    def BindEvent(self):
        pass




"""
    #绘制函数
    def paintEvent(self, event):
        # 设定循环股票序号
        StockIndex = 1
        # 绘制序号的画笔
        OrderPainter = QPainter()
        OrderPainter.begin(self)
        print(OrderPainter.isActive())
        OrderPainter.setPen(QColor(208, 208, 208, 255))
        OrderPainter.setFont(QFont("Arial", 16))
        # 循环生成组件
        for TotalStockRow in GlobalData.GetValue("TotalStock").itertuples():
            # 生成序列
            OrderPainter.drawText(QRect(0, 20 * (StockIndex - 1) + 30, 50, 20), QtCore.Qt.AlignCenter, str(StockIndex))
            # 序号加1
            StockIndex += 1
        OrderPainter.end()

self.SymbolLabel = SymbolLabel
        self.NameLabel = NameLabel
        self.TotalMVLabel = TotalMVLabel
        self.TotalShareLabel = TotalShareLabel
        self.CloseLabel = CloseLabel
        self.TurnOverRateLabel = TurnOverRateLabel
        self.VolumeRatioLabel = VolumeRatioLabel
        self.IndustryLabel = IndustryLabel
        self.PELabel = PELabel
        self.PETTMLabel = PETTMLabel
        self.PBLabel = PBLabel
        self.PSLabel = PSLabel
        self.PSTTMLabel = PSTTMLabel
        self.CircMvLabel = CircMvLabel
        self.FloatShareLabel = FloatShareLabel
        self.FreeShareLabel = FreeShareLabel
        
        
        
        
            #生成Item控件
            ItemLabelList = []
            ItemPosX = 0
            LeftButton = None
            for i in range(0, len(self.ParamButtonList) - 1):
                if i == 0:
                    ItemLabel = QLabel("", self.LeftContentWidget)
                    ItemLabel.setGeometry(0, 20 * (StockIndex - 1), self.ParamButtonList[i].width(), 20)
                    ItemLabelList.append(ItemLabel)
                elif i == 1:
                    ItemLabel = QLabel("", self.LeftContentWidget)
                    ItemLabel.setGeometry(90, 20 * (StockIndex - 1), self.ParamButtonList[i].width(), 20)
                    ItemLabelList.append(ItemLabel)
                    LeftButton = QPushButton(self.LeftContentWidget)
                    LeftButton.setGeometry(0, 20 * (StockIndex - 1), 260, 20)
                    LeftButton.setText("")
                    LeftButton.setStyleSheet("QPushButton{ background-color: rgba(0, 0, 0, 0) }QPushButton:hover{ background-color: rgb(150, 30, 0);}")
                else:
                    ItemLabel = QLabel("", self.ScrollContentWidget)
                    ItemLabel.setGeometry(ItemPosX, 20 * (StockIndex - 1), self.ParamButtonList[i].width(), 20)
                    ItemLabelList.append(ItemLabel)
                    ItemPosX += self.ParamButtonList[i].width()
            RightButton = QPushButton(self.ScrollContentWidget)
            RightButton.setGeometry(0, 20 * (StockIndex - 1), 1180, 20)
            RightButton.setText("")
            RightButton.setStyleSheet("QPushButton{ background-color: rgba(0, 0, 0, 0) }QPushButton:hover{ background-color: rgb(150, 30, 0);}")
            self.StockItemList.append(ShenhuStockItem(ItemLabelList, LeftButton, RightButton, TotalStockRow))
"""