import sys 
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon 


class Example(QWidget):
	
	def __init__(self):
		super().__init__()  #返回父级对象

		self.initUI()  #使用initUI（）方法创建一个GUI


	def initUI(self):

		self.setGeometry(300, 300, 300, 220)  #设置X、Y坐标和窗口大小
		self.setWindowTitle('Icon')           #创建窗口标题
		self.setWindowIcon(QIcon('web1.PNG')) # 添加图标，先创建QIcon对象，然后接受路径作为显示图标

		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
