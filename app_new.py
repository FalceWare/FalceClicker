from PyQt5 import QtCore, QtGui, QtWidgets
import files_rc
import time
import pyautogui as auto
import keyboard as key
from PyQt5.QtCore import QThread, pyqtSignal


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(1100, 675)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/ico/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1100, 675))
		self.stackedWidget.setObjectName("stackedWidget")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")
		self.frame = QtWidgets.QFrame(self.page)
		self.frame.setGeometry(QtCore.QRect(0, 0, 1100, 675))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(20, -10, 311, 111))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(36)
		font.setBold(False)
		font.setWeight(50)
		self.label.setFont(font)
		self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.482587 rgba(49, 36, 225, 255), stop:1 rgba(29, 21, 132, 255));\n"
"background: none;")
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(340, 140, 491, 111))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		font.setBold(False)
		font.setWeight(50)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("color: #E2E1F0;\n"
"background: none;")
		self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_2.setObjectName("label_2")
		self.lineEdit = QtWidgets.QLineEdit(self.frame)
		self.lineEdit.setGeometry(QtCore.QRect(370, 240, 401, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.lineEdit.setFont(font)
		self.lineEdit.setStyleSheet("background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.lineEdit.setMaxLength(10)
		self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
		self.lineEdit_2.setGeometry(QtCore.QRect(370, 330, 401, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setStyleSheet("background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.lineEdit_2.setMaxLength(10)
		self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(370, 420, 401, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton.setFont(font)
		self.pushButton.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.482587 rgba(49, 36, 225, 255), stop:1 rgba(29, 21, 132, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: rgb(34, 25, 158);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgb(21, 33, 99);\n"
"border-radius: 15px;\n"
"}\n"
"")
		self.pushButton.setObjectName("pushButton")
		self.label_4 = QtWidgets.QLabel(self.frame)
		self.label_4.setGeometry(QtCore.QRect(20, 45, 341, 111))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		font.setBold(False)
		font.setWeight(50)
		self.label_4.setFont(font)
		self.label_4.setStyleSheet("color: #E2E1F0;\n"
"background: none;")
		self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_4.setObjectName("label_4")
		self.stackedWidget.addWidget(self.page)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.frame_2 = QtWidgets.QFrame(self.page_2)
		self.frame_2.setGeometry(QtCore.QRect(0, 0, 1100, 675))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.label_9 = QtWidgets.QLabel(self.frame_2)
		self.label_9.setGeometry(QtCore.QRect(20, -10, 311, 111))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(36)
		font.setBold(False)
		font.setWeight(50)
		self.label_9.setFont(font)
		self.label_9.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.482587 rgba(49, 36, 225, 255), stop:1 rgba(29, 21, 132, 255));\n"
"background: none;")
		self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_9.setObjectName("label_9")
		self.label_12 = QtWidgets.QLabel(self.frame_2)
		self.label_12.setGeometry(QtCore.QRect(340, 140, 491, 111))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		font.setBold(False)
		font.setWeight(50)
		self.label_12.setFont(font)
		self.label_12.setStyleSheet("color: #E2E1F0;\n"
"background: none;")
		self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_12.setObjectName("label_12")
		self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
		self.horizontalSlider.setGeometry(QtCore.QRect(370, 350, 291, 21))
		self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"background-color: transparent;\n"
"height: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.482587 rgba(49, 36, 225, 255), stop:1 rgba(29, 21, 132, 255));\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"background-color: #191919;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background-color: #E2E1F0;\n"
"border-radius: 10px;\n"
"width: 22px;\n"
"margin-top: -8px;\n"
"margin-bottom: -8px;\n"
"}")
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setObjectName("horizontalSlider")
		self.label_13 = QtWidgets.QLabel(self.frame_2)
		self.label_13.setGeometry(QtCore.QRect(490, 315, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		font.setBold(False)
		font.setWeight(50)
		self.label_13.setFont(font)
		self.label_13.setStyleSheet("background: none;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_13.setObjectName("label_13")
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
		self.doubleSpinBox.setGeometry(QtCore.QRect(670, 310, 100, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.doubleSpinBox.setFont(font)
		self.doubleSpinBox.setStyleSheet("background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
		self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_2.setGeometry(QtCore.QRect(370, 410, 401, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.482587 rgba(49, 36, 225, 255), stop:1 rgba(29, 21, 132, 255));\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: rgb(34, 25, 158);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgb(21, 33, 99);\n"
"border-radius: 15px;\n"
"}\n"
"")
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_3.setGeometry(QtCore.QRect(290, 240, 361, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton_3.setFont(font)
		self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(20, 20, 20);\n"
"color: gray;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(16, 16, 16);\n"
"color: gray;\n"
"border-radius: 15px;\n"
"}")
		self.pushButton_3.setObjectName("pushButton_3")
		self.label_14 = QtWidgets.QLabel(self.frame_2)
		self.label_14.setGeometry(QtCore.QRect(660, 240, 171, 61))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		font.setBold(False)
		font.setWeight(50)
		self.label_14.setFont(font)
		self.label_14.setStyleSheet("background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.label_14.setText("")
		self.label_14.setAlignment(QtCore.Qt.AlignCenter)
		self.label_14.setObjectName("label_14")
		self.label_5 = QtWidgets.QLabel(self.frame_2)
		self.label_5.setGeometry(QtCore.QRect(20, 45, 341, 111))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		font.setBold(False)
		font.setWeight(50)
		self.label_5.setFont(font)
		self.label_5.setStyleSheet("color: #E2E1F0;\n"
"background: none;")
		self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_5.setObjectName("label_5")
		self.stackedWidget.addWidget(self.page_2)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "FalceWare"))
		self.label.setText(_translate("MainWindow", "FalceWare"))
		self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Авторизируйтесь через <span style=\" color:#1d1584;\">FalceID</span></p></body></html>"))
		self.lineEdit.setPlaceholderText(_translate("MainWindow", "Логин:"))
		self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Пароль:"))
		self.pushButton.setText(_translate("MainWindow", "Войти"))
		self.pushButton.setShortcut(_translate("MainWindow", "Return"))
		self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Лучший <span style=\" color:#1d1584;\">универсальный</span> клиент</p></body></html>"))
		self.label_9.setText(_translate("MainWindow", "FalceWare"))
		self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Выполните <span style=\" color:#1d1584;\">быструю настройку</span></p></body></html>"))
		self.label_13.setText(_translate("MainWindow", "0 cps"))
		self.pushButton_2.setText(_translate("MainWindow", "Сохранить"))
		self.pushButton_2.setShortcut(_translate("MainWindow", "Return"))
		self.pushButton_3.setText(_translate("MainWindow", "Выберите кнопку включения:"))
		self.pushButton_3.setShortcut(_translate("MainWindow", "Return"))
		self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Лучший <span style=\" color:#1d1584;\">универсальный</span> клиент</p></body></html>"))

class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.auth)
		self.pushButton_3.clicked.connect(self.start_thread_button)
		self.pushButton_2.clicked.connect(self.clicker_thread_button)
		self.connect_slider_spinbox()
	def auth(self):
		self.login = self.lineEdit.text()
		self.password = self.lineEdit_2.text()
		if self.login == 'admin' and self.password == 'winter2024':
			self.stackedWidget.setCurrentIndex(1)
		else:
			self.lineEdit.clear()
			self.lineEdit_2.clear()
			self.lineEdit.setPlaceholderText('Неверные данные')
			self.lineEdit_2.setPlaceholderText('Неверные данные')
	def start_thread_button(self):
		self.label_14.setStyleSheet("background-color: #161616;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.label_14.clear()
		self.thread = ThreadingClass(parent=None)
		self.thread.start()
		self.thread.any_signal.connect(self.method)
	def method(self, counter):
		cnt = counter
		self.label_14.setStyleSheet("background-color: #191919;\n"
"color: gray;\n"
"border-radius: 15px;")
		self.label_14.setText(cnt)
	def value(self):
		self.valuecheck = self.doubleSpinBox.value()
		self.label_13.setText(str(self.valuecheck) + ' cps')
	def connect_slider_spinbox(self):
		self.horizontalSlider.valueChanged.connect(self.doubleSpinBox.setValue)
		self.horizontalSlider.valueChanged.connect(self.value)
		self.doubleSpinBox.valueChanged.connect(self.horizontalSlider.setValue)
		self.doubleSpinBox.valueChanged.connect(self.value)
	def clicker_thread_button(self):
		self.thread = ThreadingClick(mainwindow=self)
		self.thread.start()
class ThreadingClick(QThread):
	def __init__(self, mainwindow):
		super(ThreadingClick, self).__init__()
		self.mainwindow = mainwindow
	def run(self):
		self.hk = str(self.mainwindow.label_14.text())
		self.cd = float(self.mainwindow.doubleSpinBox.value())
		try:
			while True:
				if key.is_pressed(str(self.hk)):
					for i in range(10):
						auto.tripleClick()
						time.sleep(float(self.cd))
					while i == True:
						i
				else:
					while True:
						if key.is_pressed(str(self.hk)):
							for i in range(10):
								auto.tripleClick()
							while i == True:
								i
		except:
			pass

class ThreadingClass(QThread):
	any_signal = pyqtSignal(str)
	def __init__(self, parent=None):
		super(ThreadingClass, self).__init__(parent)
	def run(self):
		cnt = key.read_key()
		self.any_signal.emit(cnt)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = MainClass()
	MainWindow.show()
	sys.exit(app.exec_())