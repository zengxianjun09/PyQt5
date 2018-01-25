import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # 建立一级菜单 File
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
       

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(False) #显示是否默认打钩
        viewStatAct.triggered.connect(self.toggleMenu) # ！！是否打钩连接至这个方法，作为此方法的形参

        viewMenu.addAction(viewStatAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()
    
    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())