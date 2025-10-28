from tkinter import *
from tkinter.filedialog import *

def showImg():
	file_name = askopenfilename(parent=window, filetypes=(("PNG 파일", "*.png"),("모든 파일", "*.*")))
	img = PhotoImage(file=file_name)
	lbl.config(image=img)
	lbl.image = img

window = Tk()
window.title("LAB")
window.geometry("500x500")
window.resizable(width=FALSE, height=FALSE)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=fileMenu, label="파일")

fileMenu.add_command(label="파일 열기", command=showImg)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=quit)

img = PhotoImage()
lbl = Label(window, image=img)
lbl.pack(expand=1, anchor=CENTER)

window.mainloop()