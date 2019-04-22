from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from MarketInfo.UI_ShenhuStockWidget import Ui_ShenhuStockWindow
import GlobalData
import numpy
import _thread
from pylab import *
import mpl_finance
from Common.PY_StockFigure import StockFigure
from matplotlib.gridspec import GridSpec


class ShenhuStockWidget(QWidget, Ui_ShenhuStockWindow):
    def __init__(self, parent = None):
        super(ShenhuStockWidget,self).__init__(parent)
        self.setupUi(self)

        # 初始化数据参数
        self.InitData()
        # 绑定按钮事件
        self.BindEvent()

    def InitData(self):
        #获取股票数据,保存到本地
        self.TotalStock = GlobalData.GetValue("TotalStock")
        #获取股票数量
        StockCount = len(self.TotalStock)
        #计算组件高度
        self.ParamTotalHeight = StockCount * 20 + 6
        #获取股票y轴间隔
        self.StockItemSpace = self.ParamTotalHeight / StockCount

        #设置ParamButton的选中和不被选中的样式
        self.ParamButtonSelectStyle = "background-color: rgb(0, 0, 0); color: rgb(255, 215, 0);"
        self.ParamButtonUnSelectStyle = "background-color: rgb(0, 0, 0); color: rgb(168, 168, 168);"
        #设置当前被选中的序列是空
        self.CurrentSelectParam = ""
        #设置升序为true, 由上往下从小到大
        self.SortOrderUp = True
        #设定按钮宽度, 忽略symbol和name
        ParamWidthDict = {"total_mv" : 120, "total_share" : 120, "close" : 60, "turnover_rate" : 60, "volume_ratio" : 60, "industry" : 100, "pe" : 100, "pe_ttm" : 100, "pb" : 100, "ps" : 100, "ps_ttm" : 100, "circ_mv" : 120, "float_share" : 120, "free_share" : 120}
        #设定Param颜色
        self.ParamColorDict = {"symbol" : "#CDB79E", "name" : "#CD950C", "total_mv" : "#E0FFFF", "total_share" : "#E0FFFF", "close" : "#CDAA7D", "turnover_rate" : "#B0C4DE", "volume_ratio" : "#8B8B00", "industry" : "#FFDEAD", "pe" : "#FA8072", "pe_ttm" : "#FA8072", "pb" : "#FA8072", "ps" : "#FA8072", "ps_ttm" : "#FA8072", "circ_mv" : "#DA70D6", "float_share" : "#DA70D6", "free_share" : "#DA70D6"}
        #填充按钮逐渐到按钮字典
        self.ParamButtonDict = {"symbol" : self.SymbolButton, "name" : self.NameButton, "total_mv" : self.TotalMVButton, "total_share" : self.TotalShareButton, "close" : self.CloseButton, "turnover_rate" : self.TurnOverRateButton, "volume_ratio" : self.VolumeRatioButton, "industry" : self.IndustryButton, "pe" : self.PEButton, "pe_ttm" : self.PETTMButton, "pb" : self.PBButton, "ps" : self.PSButton, "ps_ttm" : self.PSTTMButton, "circ_mv" : self.CircMVButton, "float_share" : self.FloatShareButton, "free_share" : self.FreeShareButton}
        #按钮总宽度
        self.ParamTotalWidth = 0
        #循环设置按钮位置与宽度
        for ParamWidthItem in ParamWidthDict.items():
            self.ParamButtonDict[ParamWidthItem[0]].setGeometry(self.ParamTotalWidth, 0, ParamWidthItem[1], 30)
            self.ParamTotalWidth += ParamWidthItem[1]
        #设置ParamWidget和StockWidget和LeftContentWidget的宽度
        self.ParamWidget.setGeometry(0, 0, self.ParamTotalWidth, 30)
        self.StockWidget.setGeometry(0, 0, self.ParamTotalWidth, self.ParamTotalHeight)
        self.LeftContentWidget.setGeometry(0, 0, 260, self.ParamTotalHeight)
        #生成字体
        ParamLabelFont = QFont("SimSun", 12)
        #生成序列Label
        self.OrderLabel = QLabel(self.LeftContentWidget)
        self.OrderLabel.setGeometry(0, 0, 50, self.ParamTotalHeight)
        self.OrderLabel.setFont(ParamLabelFont)
        self.OrderLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        #定义Label字典
        self.ParamLabelDict = {}
        #定义生成的ParamLabel的x轴位置
        ParamLabelPosX = 0
        #循环生成其他ParamLabel
        for ParamButtonItem in self.ParamButtonDict.items():
            #先设置一次按钮样式
            ParamButtonItem[1].setStyleSheet(self.ParamButtonUnSelectStyle)
            #如果是股票代码或者名字
            if ParamButtonItem[0] == "symbol" or ParamButtonItem[0] == "name":
                NewParamLabel = QLabel(self.LeftContentWidget)
                NewParamLabel.setGeometry(50 if ParamButtonItem[0] == "symbol" else 140, 0, ParamButtonItem[1].width(), self.ParamTotalHeight)
                NewParamLabel.setFont(ParamLabelFont)
                NewParamLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.ParamLabelDict[ParamButtonItem[0]] = NewParamLabel
            else:
                NewParamLabel = QLabel(self.StockWidget)
                NewParamLabel.setGeometry(ParamLabelPosX, 0, ParamButtonItem[1].width(), self.ParamTotalHeight)
                NewParamLabel.setFont(ParamLabelFont)
                NewParamLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.ParamLabelDict[ParamButtonItem[0]] = NewParamLabel
                #更新下一个Label生成的位置
                ParamLabelPosX += ParamButtonItem[1].width()

        #生成股票下划线
        self.LeftUnderLineLabel = QLabel(self.LeftContentWidget)
        self.MiddleUnderLineLabel = QLabel(self.StockWidget)
        #定义样式和位置, 一开始放在第一只股票下面
        self.LeftUnderLineLabel.setGeometry(0, self.StockItemSpace - 1, 260, 1)
        self.LeftUnderLineLabel.setStyleSheet("background-color: rgb(255, 99, 71);")
        self.MiddleUnderLineLabel.setGeometry(0, self.StockItemSpace - 1, self.ParamTotalWidth, 1)
        self.MiddleUnderLineLabel.setStyleSheet("background-color: rgb(255, 99, 71);")

        #Order文字序列
        OrderLabelText = ""
        #属性文字字典
        ParamLabelTextDict = {}
        for ParamLabelItem in self.ParamLabelDict.items():
            ParamLabelTextDict[ParamLabelItem[0]] = ""
        #设定循环股票序号
        StockIndex = 1
        #循环生成组件
        for TotalStockRow in self.TotalStock.itertuples():
            #生成序列文字
            OrderLabelText += "<p style='line-height:0.4446;color:#CCCCCC'>" + str(StockIndex) + "</p>"
            #循环生成属性序列
            for ParamLabelItem in self.ParamLabelDict.items():
                ParamValue = getattr(TotalStockRow, ParamLabelItem[0])
                if type(ParamValue) == float:
                    ParamValue = round(ParamValue, 6)
                ParamLabelTextDict[ParamLabelItem[0]] += "<p style='line-height:0.4446;color:" + self.ParamColorDict[ParamLabelItem[0]] + "'>" + str(ParamValue) + "</p>"
            #序号加1
            StockIndex += 1
        self.OrderLabel.setText(OrderLabelText)
        for ParamLabelItem in self.ParamLabelDict.items():
            ParamLabelItem[1].setText(ParamLabelTextDict[ParamLabelItem[0]])

        #实例化渲染组件
        self.StockFigure = StockFigure()
        #设定Figure的背景颜色为黑色, 颜色表查看 https://docs.microsoft.com/zh-cn/dotnet/api/system.drawing.color.black?view=netframework-4.8
        FigureRect = self.StockFigure.Figure.patch
        FigureRect.set_facecolor('black')
        #分区块,设定范围
        StockGridSpec = GridSpec(3, 1, figure = self.StockFigure.Figure)
        StockGridSpec.update(left = 0.1, right = 0.9, top = 0.95, bottom = 0.05)
        self.Axes1 = self.StockFigure.Figure.add_subplot(StockGridSpec[0, :])
        self.Axes2 = self.StockFigure.Figure.add_subplot(StockGridSpec[1, :])
        self.Axes3 = self.StockFigure.Figure.add_subplot(StockGridSpec[2, :])
        self.Axes1.set_facecolor('#000000')
        self.Axes1.tick_params(labelcolor = '#FFFFFF', labelsize = 25)
        self.Axes2.set_facecolor('#000000')
        self.Axes2.tick_params(labelcolor = '#FFFFFF', labelsize = 25)
        self.Axes3.set_facecolor('#000000')
        self.Axes3.tick_params(labelcolor = '#FFFFFF', labelsize = 25)
        #添加Figure到界面
        self.RenderLayout.addWidget(self.StockFigure)

        #设置期望渲染的股票代码
        self.ExpectStockCode = ""
        #定义是否在运行多线程
        self.ThreadIsAlive = False
        #跑一次多线程
        _thread.start_new(self.ThreadRun, (self.TotalStock.iloc[0]["ts_code"],))


    def BindEvent(self):
        #绑定ScrollBar的滑动事件
        self.VerScrollBar.valueChanged.connect(self.VerScrollEvent)
        self.HorScrollBar.valueChanged.connect(self.HorScrollEvent)

        #绑定Param按钮事件
        self.SymbolButton.clicked.connect(lambda : self.ParamButtonEvent("symbol"))
        self.NameButton.clicked.connect(lambda : self.ParamButtonEvent("name"))
        self.TotalMVButton.clicked.connect(lambda : self.ParamButtonEvent("total_mv"))
        self.TotalShareButton.clicked.connect(lambda : self.ParamButtonEvent("total_share"))
        self.CloseButton.clicked.connect(lambda : self.ParamButtonEvent("close"))
        self.TurnOverRateButton.clicked.connect(lambda : self.ParamButtonEvent("turnover_rate"))
        self.VolumeRatioButton.clicked.connect(lambda : self.ParamButtonEvent("volume_ratio"))
        self.IndustryButton.clicked.connect(lambda : self.ParamButtonEvent("industry"))
        self.PEButton.clicked.connect(lambda : self.ParamButtonEvent("pe"))
        self.PETTMButton.clicked.connect(lambda : self.ParamButtonEvent("pe_ttm"))
        self.PBButton.clicked.connect(lambda : self.ParamButtonEvent("pb"))
        self.PSButton.clicked.connect(lambda : self.ParamButtonEvent("ps"))
        self.PSTTMButton.clicked.connect(lambda : self.ParamButtonEvent("ps_ttm"))
        self.CircMVButton.clicked.connect(lambda : self.ParamButtonEvent("circ_mv"))
        self.FloatShareButton.clicked.connect(lambda : self.ParamButtonEvent("float_share"))
        self.FreeShareButton.clicked.connect(lambda : self.ParamButtonEvent("free_share"))

    def VerScrollEvent(self, InValue):
        #范围在0-999,计算y位置
        TargetPosY = - InValue / 999 * (self.ParamTotalHeight - 825)
        #设定位置
        self.LeftContentWidget.move(0, TargetPosY)
        self.StockWidget.move(self.StockWidget.pos().x(), TargetPosY)

    def HorScrollEvent(self, InValue):
        #范围在0-49
        #计算ParamWidget和StockWidget的x轴位置
        TargetPosX = - InValue / 49 * (self.ParamTotalWidth - 600)
        #设定位置
        self.ParamWidget.move(TargetPosX, 0)
        self.StockWidget.move(TargetPosX, self.StockWidget.pos().y())

    def wheelEvent(self, event):
        #计算y值
        TargetPosY = self.StockWidget.pos().y()
        TargetPosY += self.StockItemSpace if event.angleDelta().y() > 0 else -self.StockItemSpace
        #限定范围
        TargetPosY = numpy.clip(TargetPosY, 825 - self.ParamTotalHeight, 0)
        # 设定位置
        self.LeftContentWidget.move(0, TargetPosY)
        self.StockWidget.move(self.StockWidget.pos().x(), TargetPosY)
        #更改滑动条位置
        self.VerScrollBar.setValue(-TargetPosY / self.ParamTotalHeight * 999)

    #Param按钮点击事件, 传回来Param的名字
    def ParamButtonEvent(self, ParamName):
        #根据传回来的值进行排序
        if self.CurrentSelectParam != ParamName:
            #如果当前选中不为空, 把当前选中修改颜色与文字
            if self.CurrentSelectParam != "":
                #获取当前选中的按钮
                CurrentSelectButton = self.ParamButtonDict[self.CurrentSelectParam]
                CurrentSelectButton.setStyleSheet(self.ParamButtonUnSelectStyle)
                CurrentSelectButton.setText(CurrentSelectButton.text()[:-1])
            #获取新选中的按钮
            NewSelectButton = self.ParamButtonDict[ParamName]
            NewSelectButton.setStyleSheet(self.ParamButtonSelectStyle)
            NewSelectButton.setText(NewSelectButton.text() + "↑")
            #设置为升序
            self.SortOrderUp = True
        else:
            #修改升降序
            CurrentSelectButton = self.ParamButtonDict[self.CurrentSelectParam]
            CurrentSelectButton.setText(CurrentSelectButton.text()[:-1] + ("↓" if self.SortOrderUp else "↑"))
            self.SortOrderUp = not self.SortOrderUp

        #修改当前选中的Param
        self.CurrentSelectParam = ParamName
        #进行排序
        self.TotalStock = self.TotalStock.sort_values(ParamName, ascending = self.SortOrderUp)
        #更新数据
        # 属性文字字典
        ParamLabelTextDict = {}
        for ParamLabelItem in self.ParamLabelDict.items():
            ParamLabelTextDict[ParamLabelItem[0]] = ""
        #循环设置数据
        for TotalStockRow in self.TotalStock.itertuples():
            # 循环生成属性序列
            for ParamLabelItem in self.ParamLabelDict.items():
                ParamValue = getattr(TotalStockRow, ParamLabelItem[0])
                if type(ParamValue) == float:
                    ParamValue = round(ParamValue, 6)
                ParamLabelTextDict[ParamLabelItem[0]] += "<p style='line-height:0.4446;color:" + self.ParamColorDict[
                    ParamLabelItem[0]] + "'>" + str(ParamValue) + "</p>"
        for ParamLabelItem in self.ParamLabelDict.items():
            ParamLabelItem[1].setText(ParamLabelTextDict[ParamLabelItem[0]])

    def mousePressEvent (self, event):
        #x范围限定在0,860, y范围限定在30,855
        if not (event.x() > 0 and event.y() < 860 and event.y() > 30 and event.y() < 855):
            return
        #获取点击到点相对于股票的y轴位置
        RelativePosY = event.y() - 30 - self.StockWidget.pos().y()
        #获取是第几个股票
        StockIndex = math.floor(RelativePosY / self.StockItemSpace)
        #设置下划线位置
        self.LeftUnderLineLabel.move(0, (StockIndex + 1) * self.StockItemSpace - 1)
        self.MiddleUnderLineLabel.move(0, (StockIndex + 1) * self.StockItemSpace - 1)
        #获取股票代码对应的数据, 使用iloc才能够获取排序后对应的行, 使用loc不行
        self.CurrentStockItem = self.TotalStock.iloc[StockIndex]
        #设置Label名字
        self.StockNameLabel.setText(self.CurrentStockItem["name"])
        #如果多线程没有结束, 设定期望获取的代码
        if self.ThreadIsAlive:
            self.ExpectStockCode = self.CurrentStockItem["ts_code"]
        else:
            #设定期望股票代码为空
            self.ExpectStockCode = ""
            #执行线程
            _thread.start_new(self.ThreadRun, (self.CurrentStockItem["ts_code"],))

    #线程执行的方法
    def ThreadRun(self, ExpectTSCode):
        #设定正在执行线程
        self.ThreadIsAlive = True

        wdyx = GlobalData.GetValue("Tushare").get_k_data(ExpectTSCode[:-3], '2018-01-01')
        wdyx.info()
        mat_wdyx = wdyx.as_matrix()

        num_time = []
        for date in mat_wdyx[:, 0]:
            date_time = datetime.datetime.strptime(date, '%Y-%m-%d')
            num_date = date2num(date_time)
            num_time.append(num_date)
        mat_wdyx[:, 0] = num_time

        mpl_finance.candlestick_ochl(self.Axes1, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=1.0)
        self.Axes1.set_title('wandayuanxian')
        self.Axes1.set_ylabel('Price')
        self.Axes1.grid(True)
        self.Axes1.xaxis_date()

        self.Axes2.bar(mat_wdyx[:, 0] - 0.25, mat_wdyx[:, 5], width=0.5)
        self.Axes2.set_ylabel('Volume')
        self.Axes2.xaxis_date()
        self.Axes2.grid(True)

        n = 12
        X = numpy.arange(n)
        Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
        Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
        self.Axes3.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
        self.Axes3.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

        # 重新绘制
        self.StockFigure.Figure.canvas.draw()

        #设定已经执行完线程
        self.ThreadIsAlive = False

        #如果期望获取的股票不为空, 开启新的线程
        if self.ExpectStockCode != "":
            # 执行线程
            _thread.start_new(self.ThreadRun, (self.CurrentStockItem["ts_code"],))
            #设置期望股票为空
            self.ExpectStockCode = ""









"""
 border: 1px solid red;
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
            
            
            
    
#渲染股票多线程类
class RenderStockThread(threading.Thread):
    def __init__(self, StockFigure, Axes1, Axes2, Axes3, CallBack):
        threading.Thread.__init__(self)
        #获取股票代码
        self.StockFigure = StockFigure
        self.Axes1 = Axes1
        self.Axes2 = Axes2
        self.Axes3 = Axes3
        self.CallBack = CallBack

    #设定股票代码
    def InitTSCode(self, StockTSCode):
        self.StockTSCode = StockTSCode

    def run(self):
        wdyx = GlobalData.GetValue("Tushare").get_k_data('002739', '2018-01-01')
        wdyx.info()
        mat_wdyx = wdyx.as_matrix()

        num_time = []
        for date in mat_wdyx[:, 0]:
            date_time = datetime.datetime.strptime(date, '%Y-%m-%d')
            num_date = date2num(date_time)
            num_time.append(num_date)
        mat_wdyx[:, 0] = num_time

        mpl_finance.candlestick_ochl(self.Axes1, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=1.0)
        self.Axes1.set_title('wandayuanxian')
        self.Axes1.set_ylabel('Price')
        self.Axes1.grid(True)
        self.Axes1.xaxis_date()

        self.Axes2.bar(mat_wdyx[:, 0] - 0.25, mat_wdyx[:, 5], width=0.5)
        self.Axes2.set_ylabel('Volume')
        self.Axes2.xaxis_date()
        self.Axes2.grid(True)

        #重新绘制
        self.StockFigure.Figure.canvas.draw()
        #执行回调函数
        self.CallBack()
"""