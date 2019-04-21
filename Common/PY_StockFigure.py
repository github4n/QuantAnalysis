import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")  # 声明使用QT5

#股票绘制类
class StockFigure(FigureCanvasQTAgg):
    def __init__(self):
        self.Figure = Figure(figsize = (1, 1), dpi = 30)
        # 此句必不可少，否则不能显示图形
        super(StockFigure, self).__init__(self.Figure)