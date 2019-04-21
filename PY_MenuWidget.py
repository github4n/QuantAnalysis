from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor
from UI_MenuWidget import Ui_MenuWindow
from MarketInfo.PY_MarketInfoWidget import MarketInfoWidget
import GlobalData

class MenuWidget(QWidget, Ui_MenuWindow):
    def __init__(self, parent = None):
        super(MenuWidget,self).__init__(parent)
        self.setupUi(self)

        #生成各个界面保存到本地
        self.CreatePanel()
        #初始化数据参数
        self.InitData()
        #绑定按钮事件
        self.BindEvent()

    def CreatePanel(self):
        self.MarketInfoPanel = MarketInfoWidget(self.ContentWidget)
        self.MarketInfoPanel.move(0, 0)

    def InitData(self):
        #设定背景颜色纯黑
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(0, 0, 0, 0))
        self.setPalette(palette)
        #把按钮全部填入队列
        self.TopButtonList = [self.MarketInfoButton, self.SelectStocksButton, self.TradeStrategyButton, self.SimulateTradeButton, self.QuantAnalysisButton, self.UserFunctionButton]
        #设置当前选中的id
        self.CurrectSelectIndex = 0
        # 默认设置股市资讯选中
        self.TopButtonList[self.CurrectSelectIndex].setStyleSheet(GlobalData.GetValue("ButtonSelectStyle"))

    def BindEvent(self):
        self.MarketInfoButton.clicked.connect(lambda: self.TopButtonEvent(0))
        self.SelectStocksButton.clicked.connect(lambda: self.TopButtonEvent(1))
        self.TradeStrategyButton.clicked.connect(lambda: self.TopButtonEvent(2))
        self.SimulateTradeButton.clicked.connect(lambda: self.TopButtonEvent(3))
        self.QuantAnalysisButton.clicked.connect(lambda: self.TopButtonEvent(4))
        self.UserFunctionButton.clicked.connect(lambda: self.TopButtonEvent(5))


    def TopButtonEvent(self, InIndex):
        print(InIndex)
        if self.CurrectSelectIndex == InIndex:
            return
        self.TopButtonList[InIndex].setStyleSheet(GlobalData.GetValue("ButtonSelectStyle"))
        self.TopButtonList[self.CurrectSelectIndex].setStyleSheet(GlobalData.GetValue("ButtonUnSelectStyle"))
        self.CurrectSelectIndex = InIndex

