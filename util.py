# -*- coding: utf-8 -*-

import redis
import msgpack
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
import sip
import run

def addTab(player_data, mainWindow):
    height = mainWindow.height()
    width = mainWindow.width()
    tabWidget = mainWindow.tabWidget
    tab = QtWidgets.QWidget()
    tab.setObjectName(player_data[1])
    tabWidget.addTab(tab, player_data[1])
    index = tabWidget.indexOf(tab)
    mainWindow.uuid_map[index] = [player_data[0], player_data[2]]  # 用字典存储 tabWidget的索引和uuid的对应关系

    # # 显示聊天信息widget
    listWidget = QtWidgets.QListWidget(tab)
    listWidget.setObjectName("listWidget")
    listWidget.setGeometry(0, 0 , width, height - 100)
    # # 发送消息widget
    sendWidget = QtWidgets.QWidget(tab)
    sendWidget.setGeometry(0, listWidget.height(), width, 50)

    # 添加输入框
    lineEdit = QtWidgets.QLineEdit(sendWidget)
    lineEdit.setObjectName("lineEdit")
    sendButton = QtWidgets.QPushButton("发送", sendWidget)
    lineEdit.setGeometry(0, 0 , width - 300, 50)
    sendButton.setGeometry(width - 300, 0 , 300, 50)

    # 按钮绑定点击事件
    sendButton.clicked.connect(mainWindow.send)



def initTabWidght(mainWindow):
    '初始化玩家列表'
    #    r = redis.Redis(host="localhost", port=6379, db=5)
    db_gm_chat_list = run.r_gm.hgetall("gm_chat_list")
    for player_uuid in db_gm_chat_list:
        db_gm_chat = db_gm_chat_list[player_uuid]
        gm_chat = msgpack.unpackb(db_gm_chat, use_list=False)
        player_name = gm_chat[b'name']
        new_chat_num = gm_chat[b'num']
        player_name = player_name.decode("utf-8")

        addTab((player_uuid, player_name, new_chat_num), mainWindow)

def addItem(tab, chat_data):
    'chat_data  === >   (chat_content, date, player_data)    '
    listWidget = tab.findChild(QtWidgets.QWidget, "listWidget")

    item = QtWidgets.QListWidgetItem(chat_data[0])
    item.setSizeHint(QtCore.QSize(0,30));
    listWidget.addItem(item)

def initChatFrame(uuid, chat_list_widget):
    '初始化聊天窗口 和一个玩家的聊天框'
    #    r = redis.Redis(host="localhost", port=6379, db=5)
    db_chat_gm = run.r_gm.hget("chat_gm", uuid)
    chat_gm = msgpack.unpackb(db_chat_gm, use_list=False)
    chat_base = chat_gm[b'base_']
    chat_list = chat_base[b'list_']
    listWidget = chat_list_widget.findChild(QtWidgets.QWidget, "listWidget")
    listWidget.clear()
    for index in chat_list:
        chat = chat_list[index]
        one_chat_base = chat[b'base_']
        content = one_chat_base[b'content_']
        date = one_chat_base[b'date_']
        player_data = one_chat_base[b'player_data_']

        addItem(chat_list_widget, (content.decode("utf-8"), date, player_data))


def dealNewChatList(mainWindow):
    '添加一个新的和玩家的聊天列表'
    tabWidget = mainWindow.tabWidget
    uuid_map = mainWindow.uuid_map
    db_gm_chat_list = run.r_gm.hgetall("gm_chat_list")
    for player_uuid in db_gm_chat_list:
        db_gm_chat = db_gm_chat_list[player_uuid]
        gm_chat = msgpack.unpackb(db_gm_chat, use_list=False)
        player_name = gm_chat[b'name']
        new_chat_num = gm_chat[b'num']
        player_name = player_name.decode("utf-8")

        # 一、此玩家在列表中
        if isInMap(player_uuid, uuid_map):
            index = tabWidget.currentIndex()
            tab = tabWidget.currentWidget()
            # 1、当前显示界面为此玩家列表
            if tab and uuid_map[index][0] == player_uuid:
                # 有新消息 刷新界面
                # 获取聊天数据
                db_chat_gm = run.r_gm.hget("chat_gm", uuid_map[index][0])
                chat_gm = msgpack.unpackb(db_chat_gm, use_list=False)
                chat_base = chat_gm[b'base_']
                chat_list = chat_base[b'list_']

                chat_list_len = len(chat_list)
                d_num = new_chat_num - uuid_map[index][1]
                begin = chat_list_len - d_num
                for i in range(d_num):
                    chat = chat_list[begin + i + 1]
                    one_chat_base = chat[b'base_']
                    content = one_chat_base[b'content_']
                    date = one_chat_base[b'date_']
                    player_data = one_chat_base[b'player_data_']

                    addItem(tab, (content.decode("utf-8"), date, player_data))

                    uuid_map[index][1] = new_chat_num
            # 2、当前显示界面不是此玩家列表
            # else:
            #     addTab((player_uuid, player_name, new_chat_num), mainWindow)

        # 二、此玩家不在列表中
        else:
            addTab((player_uuid, player_name, new_chat_num), mainWindow)
            index = tabWidget.currentIndex()
            tab = tabWidget.currentWidget()
            if uuid_map[index][0] == player_uuid:
                initChatFrame(player_uuid, tab)

def isInMap(player_uuid, uuid_map):
    for key in uuid_map:
        data = uuid_map[key]
        if data[0] == player_uuid:
            return True
    return False

def updateUUID(mainWindow, del_index):
    tabWidget = mainWindow.tabWidget
    uuid_map = mainWindow.uuid_map
    back_num = tabWidget.count() - del_index
    map_len = len(uuid_map)
    for i in range(back_num):
        index = del_index + i
        uuid_map[index] = uuid_map[index + 1]
    if map_len > 0:
        uuid_map.pop(map_len)