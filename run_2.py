# # coding: utf-8
#
# from Tkinter import *
# from units import *
# import sys
# from PyQt4.QtGui import *
#
#
#
# def main():
#
#     a = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(320, 240)
#     w.setWindowTitle("Hello, World!")
#     w.show()
#
#     b = QPushButton("click")
#     b.setParent(w)
#     b.show()
#
#
#     # l = QLable()
#     # l.setText("hello world")
#
#
#     sys.exit(a.exec_())
#
#     # zr = ZxRedis()
#     # print dir(zr)
#     #
#     # root = Tk()
#     # root.title("GM聊天工具")
#     # root.geometry("600x600+500+100")
#     # root.resizable(width=True, height=False)
#
#     # lb = Listbox(root)
#     # sl = Scrollbar(root, orient = HORIZONTAL)
#     # sl.pack(side = RIGHT, fill = Y)
#     # lb['yscrollcommand'] = sl.set
#     # for i in range(100):
#     #     lb.insert(END, str(i))
#     # lb.pack(side = LEFT)
#     # sl['command'] = lb.yview
#
#     # Spinbox(root).pack()
#
#     #可以的
#     # lb = Listbox(root)
#     # bt1 = Button(root, text='leftmost button')
#     # for item in ['python', 'widget', 'thinter']:
#     #     lb.insert(END, item)
#     # lb.pack()
#     # Message(root, text = "hello ").pack()
#
#     # t = Text(root)
#     #
#     # t.pack()
#
#     # print root.size()
#     # Frame(height = 20, width = 400, bg = 'blue').place(x = 0, y = 0)
#
#     # def hello(event):
#     #     print 'hello menu'
#     #     root2 = Tk()
#     #     root2.title("neirong")
#     #     print event.widget["text"]
#     # for i in range(100):
#     #     bt1 = Button(root, text='leftmost button')
#     #     bt1.bind('<Button-1>', hello)
#     #     bt1.pack()
#     # menubar = Menu(root)
#     # # 创建主菜单，每个菜单对应的回调函数都是hello
#     # for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
#     #     menubar.add_command(label=item, command=hello)
#     # # 将root的menu属性设置为menubar
#     # root['menu'] = menubar
#
#     # cv = Canvas(root, bg='white')
#     # # 创建三个rectangle
#     # rt1 = cv.create_rectangle(
#     #     10, 10, 110, 110,
#     #     tags=('r1', 'r2', 'r3'))
#     # rt2 = cv.create_rectangle(
#     #     20, 20, 80, 80,
#     #     tags=('s1', 's2', 's3'))
#     # rt3 = cv.create_rectangle(
#     #     30, 30, 70, 70,
#     #     tags=('y1', 'y2', 'y3'))
#     # # 向rt2的上一个item添加r4
#     # cv.addtag_above('r4', rt2)
#     # # 向rt2的下一个item添加r5
#     # cv.addtag_below('r5', rt2)
#     #
#     # for item in [rt1, rt2, rt3]:
#     #     print cv.gettags(item)
#     #
#     # cv.pack()
#
#     # cv = Canvas(root, bg='white')
#     # # 使用tags指定一个tag('r1')
#     # rt = cv.create_rectangle(10, 10, 110, 110,
#     #                          tags='r1'
#     #                          )
#     # cv.pack()
#     # print cv.gettags(rt)
#     # # 使用tags属性指定多个tags,即重新设置tags的属性
#     # cv.itemconfig(rt, tags=('r2', 'r3', 'r4'))
#     # print cv.gettags(rt)
#
#     # cv = Canvas(root, bg='white')
#     # cv.create_rectangle(10, 10, 110, 110,
#     #                     outline='red',
#     #                     dash=10,
#     #                     fill='green')
#     # cv.pack()
#
#     # cv = Canvas(root, bg='white')
#     # # 创建一个矩形，坐标为(10,10,110,110)
#     # cv.create_rectangle(10, 10, 110, 110)
#     # cv.pack()
#
#     # cv = Canvas(root, bg='white')
#     # cv.pack()
#
#
#
#     # Label(root, text="frame", bg="red", font=("Arial", 15), command=click()).pack()
#     # frm = Frame(root)
#     # # left
#     # frm_L = Frame(frm)
#     # Label(frm_L, text="左上", bg="pink", font=("Arial", 12)).pack(side=TOP)
#     # Label(frm_L, text="左下", bg="green", font=("Arial", 12)).pack(side=TOP)
#     # frm_L.pack(side=LEFT)
#     # # right
#     # frm_R = Frame(frm)
#     # Label(frm_R, text="右上", bg="yellow", font=("Arial", 12)).pack(side=TOP)
#     # Label(frm_R, text="右下", bg="purple", font=("Arial", 12)).pack(side=TOP)
#     # frm_R.pack(side=RIGHT)
#     # frm.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
#
#     # mainloop()
#
#
#
# if __name__ == "__main__":
#     main()