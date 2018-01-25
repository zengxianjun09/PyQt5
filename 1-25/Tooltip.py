import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
	QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
	
	def __init__(self):
		super().__init__()  #返回父级对象

		self.initUI1()#使用initUI（）方法创建一个GUI
		#self.initUI()


	def initUI1(self):

		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(80,80)

		self.setGeometry(300, 300, 300, 220)  #设置X、Y坐标和窗口大小
		self.setWindowTitle('Tooltips')    #创建窗口标题
		self.setWindowIcon(QIcon('web1.PNG')) # 添加图标，先创建QIcon对象，然后接受路径作为显示图标

		self.show()

	def initUI(self):

		QToolTip.setFont(QFont('SansSerif', 10)) #提示框字体和大小

		self.setToolTip('This is a <b>QWidget</b> widget') #文本提示符

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget') #文本提示符
		btn.resize(btn.sizeHint())
		btn.move(50, 50) #按钮坐标

		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(80,80)

		self.setGeometry(300, 300, 300, 220)  #设置X、Y坐标和窗口大小
		self.setWindowTitle('Tooltips')    #创建窗口标题
		self.setWindowIcon(QIcon('web1.PNG')) # 添加图标，先创建QIcon对象，然后接受路径作为显示图标

		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
