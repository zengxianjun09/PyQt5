import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        #self.closeEvent()
        
        
    def initUI(self):               
        
        self.resize(250, 250)
        self.center()

        self.setWindowTitle('Center')    
        self.show()
    
    def center(self):

        qr = self.frameGeometry() #得到主窗口大小
        cp = QDesktopWidget().availableGeometry().center() #获取显示器分辨率，然后得到中间点的位置
        qr.moveCenter(cp) #把窗口中心点放置在qr的中心点
        self.move(qr.topLeft()) #把窗口的左上角坐标设置成qr的矩形左上角坐标    
        
    def closeEvent(self, event): # 关闭窗口时自动触发的事件！不能更改方法名字
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())