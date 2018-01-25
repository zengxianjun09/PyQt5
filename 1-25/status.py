import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

        # 建立一级菜单 File
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        impMenu = QMenu('Import', self) # 新二级菜单名字叫Import
        impAct = QAction('Import mail', self) # 建立二级菜单里面的动作 Import mail
        impMenu.addAction(impAct) #把动作添加到二级菜单里面

        newAct = QAction('New', self) # 一级菜单动作NEW

        fileMenu.addAction(newAct) # 添加一级菜单里面的动作1
        fileMenu.addMenu(impMenu) # 添加一级菜单里面的新菜单
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())