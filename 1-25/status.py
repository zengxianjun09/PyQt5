import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
QVBoxLayout, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):   

        okButton = QPushButton("OK") #建立ok 和 cancel 按钮
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() #建立水平布局
        hbox.addStretch(1)  #在按钮之间增加弹性空间
        hbox.addWidget(okButton) #把元素放在应用的右下角
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox) #把水平布局放置到垂直布局盒里面

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()
    
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())