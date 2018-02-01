import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QMainWindow, QPushButton,
QVBoxLayout, QApplication)

class Communicate(QObject):  #发送事件信号 QObject
    
    closeApp = pyqtSignal() #建立信号

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

      self.c = Communicate()
      self.c.closeApp.connect(self.close) #信号与关闭命令绑定

      self.setGeometry(300, 300, 290, 150)
      self.setWindowTitle('Emit signal')
      self.show()

    def mousePressEvent(self, event): #鼠标按下触发关闭信号 

        self.c.closeApp.emit()
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())