# 来源http://www.51testing.com/html/04/n-4480904.html

import os
import sys
import time

from PyQt5 import QtCore, QtWidgets, QtGui


class ShowDown(object):

    def pageShow(self, page):
        """设置窗口位置和大小,标题，图标字体等"""
        page.setGeometry(400, 400, 400, 200)
        page.setWindowTitle('Windows自动关机小工具')
        # page.setWindowIcon(QtGui.QIcon('#ddffgg'))
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        page.setToolTip('这是windows关机工具')
        # 创建文本标签
        self.label = QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(60, 20, 120, 45))
        self.label.setFont(QtGui.QFont("Roman times", 10, QtGui.QFont.Bold))
        # 设置文本标签和时间栏框
        self.label2 = QtWidgets.QLabel(page)
        self.label2.setGeometry(QtCore.QRect(100, 55, 40, 51))
        self.label2.setFont(QtGui.QFont("Roman times", 10, QtGui.QFont.Bold))
        self.time = QtWidgets.QDateTimeEdit(page)
        self.time.setGeometry(QtCore.QRect(140, 70, 180, 25))
        self.time.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        # 设置日期可使用日历插件
        self.time.setCalendarPopup(True)
        # 根据PyQt方法获取系统当前时间
        now = QtCore.QDateTime.currentDateTime()
        now_time = now.toString(QtCore.Qt.ISODate)
        # 将当前系统时间复制给时间框中
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.time.setDateTime(QtCore.QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))
        # 一个按钮并设置添加单击事件
        self.btn = QtWidgets.QPushButton(page, clicked=self.shut)
        # self.btn.clicked.connect(self.shut(page))
        self.btn.setToolTip("提交按钮")
        self.btn.move(110, 110)

        self.btn1 = QtWidgets.QPushButton(page, clicked=self.cleart)
        self.btn1.setToolTip('这是清除任务按钮')
        self.btn1.move(210, 110)
        self.text = QtWidgets.QLabel(page)
        self.text.setGeometry(QtCore.QRect(25, 150, 350, 25))
        self.text.setFont(QtGui.QFont("Roman times", 14, QtGui.QFont.Bold))

        self.setUi(page)
        page.show()

    def setUi(self, page):
        """设置UI界面信息"""
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(_translate("page", "请输入关机时间"))
        self.label2.setText(_translate("page", "日期： "))
        self.btn.setText(_translate("page", "提交"))
        self.btn1.setText(_translate("page", "清除"))
        self.text.setText(_translate("page", "请设置关机时间！ "))

    def shut(self, page):
        """设置关机"""
        datetime = self.time.text()
        t1 = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
        t = int(time.mktime(t1))
        nq = int(time.time())
        d = t - nq
        if d > 0:
            try:
                os.system('shutdown -s -t %d' % d)
                self.text.setText("电脑将在%s关机！" % datetime)
            except:
                self.text.setText("设置失败！")
            else:
                self.text.setText("日期设置错误！")

    def cleart(self, page):
        """清除关机任务"""
        try:
            os.system('shoutdown -a')
            self.text.setText("已经清除关机任务！")
        except:
            self.text.setText("清除任务失败！")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    page = QtWidgets.QWidget()
    ui = ShowDown()
    ui.pageShow(page)
    sys.exit(app.exec())
