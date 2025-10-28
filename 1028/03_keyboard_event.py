from tkinter import *
from tkinter import messagebox

def keyEvent(e):
	messagebox.showinfo("알림", f"키 : {e.char}\n키코드 : {e.keycode}")

window = Tk()
window.title("Keyboard Event")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)

window.bind("<Key>", keyEvent)

# 키보드 이벤트
'''
모든 키 : <KEY>
특수 키 : <Return>, <BackSpace>, <Tab>, <Shift_L>, <Alt_L> ...
일반 키 : a~z, A~Z, 0~9, <space>, <less> (<)
화살표 키 조합 : <Shift-Up>, <Shift-Down>, <Shift-Left>, <Shift-Right>
'''

window.mainloop()