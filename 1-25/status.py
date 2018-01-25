import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()
    
    def contextMenuEvent(self, event): #此方法继承父类，实现右键菜单

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos())) #exec_显示菜单，从鼠标右键获取事件对象的当前坐标

        if action == quitAct:
            qApp.quit()
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())