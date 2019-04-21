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
        """使用循环来设置lambda的参数没有效果
        for i in range(0, len(self.LeftButtonList) - 1):
            print("i --> ", i)
            self.LeftButtonList[i].clicked.connect(lambda: self.LeftButtonEvent(i))
        """
        self.ShenhuStockButton.clicked.connect(lambda: self.LeftButtonEvent(0))
        self.ShenhuExponentButton.clicked.connect(lambda: self.LeftButtonEvent(1))
        self.NewStockIPOButton.clicked.connect(lambda: self.LeftButtonEvent(2))
        self.FundBondsButton.clicked.connect(lambda: self.LeftButtonEvent(3))
        self.OptionsMarketButton.clicked.connect(lambda: self.LeftButtonEvent(4))
        self.HotInfoButton.clicked.connect(lambda: self.LeftButtonEvent(5))

    def LeftButtonEvent(self, InIndex):
        if self.CurrectSelectIndex == InIndex:
            return
        self.LeftButtonList[InIndex].setStyleSheet(GlobalData.GetValue("ButtonSelectStyle"))
        self.LeftButtonList[self.CurrectSelectIndex].setStyleSheet(GlobalData.GetValue("ButtonUnSelectStyle"))
        self.CurrectSelectIndex = InIndex





