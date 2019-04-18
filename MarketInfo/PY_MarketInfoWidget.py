from PyQt5.QtWidgets import QWidget
from MarketInfo.UI_MarketInfoWidget import Ui_MarketInfoWindow
import GlobalData

from MarketInfo.PY_ShenhuStockWidget import ShenhuStockWidget

class MarketInfoWidget(QWidget, Ui_MarketInfoWindow):
    def __init__(self, parent = None):
        super(MarketInfoWidget,self).__init__(parent)
        self.setupUi(self)

        #生成子窗体
        self.CreatePanel()
        #初始化数据参数
        self.InitData()
        #绑定事件
        self.BindEvent()

    def CreatePanel(self):
        self.ShenhuStockPanel = ShenhuStockWidget(self.ContentWidget)
        self.ShenhuStockPanel.move(0, 0)

    def InitData(self):
        #把按钮填充入队列
        self.LeftButtonList = [self.ShenhuStockButton, self.ShenhuExponentButton, self.NewStockIPOButton, self.FundBondsButton, self.OptionsMarketButton, self.HotInfoButton]
        #默认选中第一个
        self.CurrectSelectIndex = 0
        #选中第一个
        self.LeftButtonList[self.CurrectSelectIndex].setStyleSheet(GlobalData.GetValue("ButtonSelectStyle"))

    def BindEvent(self):
        self.ShenhuStockButton.clicked.connect(self.ShenhuStockButtonEvent)
        self.ShenhuExponentButton.clicked.connect(self.ShenhuExponentButtonEvent)
        self.NewStockIPOButton.clicked.connect(self.NewStockIPOButtonEvent)
        self.FundBondsButton.clicked.connect(self.FundBondsButtonEvent)
        self.OptionsMarketButton.clicked.connect(self.OptionsMarketButtonEvent)
        self.HotInfoButton.clicked.connect(self.HotInfoButtonEvent)


    def ShenhuStockButtonEvent(self):
        self.LeftButtonEvent(0)

    def ShenhuExponentButtonEvent(self):
        self.LeftButtonEvent(1)

    def NewStockIPOButtonEvent(self):
        self.LeftButtonEvent(2)

    def FundBondsButtonEvent(self):
        self.LeftButtonEvent(3)

    def OptionsMarketButtonEvent(self):
        self.LeftButtonEvent(4)

    def HotInfoButtonEvent(self):
        self.LeftButtonEvent(5)

    def LeftButtonEvent(self, InIndex):
        if self.CurrectSelectIndex == InIndex:
            return
        self.LeftButtonList[InIndex].setStyleSheet(GlobalData.GetValue("ButtonSelectStyle"))
        self.LeftButtonList[self.CurrectSelectIndex].setStyleSheet(GlobalData.GetValue("ButtonUnSelectStyle"))
        self.CurrectSelectIndex = InIndex





