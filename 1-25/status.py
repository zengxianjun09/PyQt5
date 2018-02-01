import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
QVBoxLayout, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

       lcd = QLCDNumber(self) #建立数码管数字
       sld = QSlider(Qt.Horizontal, self) #平行的滑块

       vbox = QVBoxLayout() #建立箱子布局
       vbox.addWidget(lcd) #将数码管和滑块加入到箱子里面
       vbox.addWidget(sld)

       self.setLayout(vbox) #设置布局
       sld.valueChanged.connect(lcd.display)#滑块变化带动数码管数字显示改动

       self.setGeometry(300,300, 250, 150) 
       self.setWindowTitle('Signal and slot')    
       self.show()
    
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())