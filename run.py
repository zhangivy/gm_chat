# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PyQT\ChatGMUI\ChatGMUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import util
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import redis
import msgpack
import struct

import threading
from time import ctime, sleep

r_server = redis.Redis(host="localhost", port=6379, db=4)
r_gm = redis.Redis(host="localhost", port=6379, db=5)


class Ui_MainWindow(QtWidgets.QMainWindow):
    newChatSignal = pyqtSignal()

    def setupUi(self):
        self.uuid_map = {}  # index = [uuid, new_chat_num]
        self.setObjectName("MainWindow")
        self.resize(1366, 768)
        self.setFixedSize(self.size())
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")

        self.newChatSignal.connect(self.newChat)

        # 初始化玩家名字列表
        util.initTabWidght(self)

        # 点击 监听
        self.tabWidget.tabBarClicked.connect(self.click)
        # 关闭 监听
        self.tabWidget.tabCloseRequested.connect(self.close)

        if self.tabWidget.widget(0):
            util.initChatFrame(self.uuid_map[0][0], self.tabWidget.widget(0))



        # 创建一个线程，处理新的消息
        t = threading.Thread(target=self.loop, args=(self,))
        t.setDaemon(True)
        t.start()

        self.tabWidget.setTabsClosable(True)
        self.horizontalLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralWidget)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def click(self, index):
        '点击tab的事件'
        util.initChatFrame(self.uuid_map[index][0], self.tabWidget.widget(index))

    def close(self, index):
        '关闭tab的事件'
        self.tabWidget.removeTab(index)
        self.uuid_map.pop(index)
        util.updateUUID(self, index)
        #更新uuid_map
        index = self.tabWidget.currentIndex()
        if index != -1:
            util.initChatFrame(self.uuid_map[index][0], self.tabWidget.widget(index))

    def send(self):
        '发送按钮事件'
        tab = self.tabWidget.currentWidget()
        lineEdit = tab.findChild(QtWidgets.QLineEdit, "lineEdit")

        if len(lineEdit.text()) == 0:
            return

        util.addItem(tab, (lineEdit.text(), 00000))

        index = self.tabWidget.currentIndex()
        uuid_str = str(struct.unpack('Q', bytes(self.uuid_map[index][0]))[0])

        sendData = [uuid_str, [lineEdit.text()]]
        sendDataBytes = msgpack.packb(sendData)
        #        r = redis.Redis(host="localhost", port=6379, db=4)
        r_server.lpush("gm_chat", sendDataBytes)

        lineEdit.setText("")

    def newChat(self):
        util.dealNewChatList(self)
    def loop(self, args):
        while True:
            self.newChatSignal.emit()
            sleep(1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()
    ui.setupUi()

    ui.show()
    sys.exit(app.exec_())
