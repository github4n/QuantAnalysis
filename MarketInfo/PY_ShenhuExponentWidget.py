from PyQt5.QtWidgets import QWidget
from MarketInfo.UI_ShenhuExponentWidget import Ui_ShenhuExponentWindow

class ShenhuExponentWidget(QWidget, Ui_ShenhuExponentWindow):
    def __init__(self, parent = None):
        super(ShenhuExponentWidget,self).__init__(parent)
        self.setupUi(self)