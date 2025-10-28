from tkinter import *
from tkinter import messagebox

def funcOpen():
	messagebox.showinfo("알림", "열기 메뉴 선택됨")

def funcExit():
	window.quit()
	window.destroy()

window = Tk()
window.title("Menu")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)

# 메인 메뉴 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

# 하위 메뉴 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)

# 세부 메뉴 생성
fileMenu.add_command(label="열기", command=funcOpen)
fileMenu.add_separator()
fileMenu.add_command(label="닫기", command=funcExit)

window.mainloop()