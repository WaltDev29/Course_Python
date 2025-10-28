from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def showMessages():
	value1 = simpledialog.askinteger("Ask Integer", "정수를 입력하세요", minvalue=1, maxvalue=6)
	value2 = simpledialog.askfloat("Ask Float", "실수를 입력하세요")
	value3 = simpledialog.askstring("Ask String", "문자열을 입력하세요")
	lbl.config(text = f"입력한 정수 : {value1}\n입력한 실수 : {value2}\n입력한 문자열 : {value3}")

window = Tk()
window.title("Simple Dialog")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)

btn1 = Button(window, text="입력", command=showMessages)
btn1.pack()

lbl = Label(window, text="버튼을 눌러주세요")
lbl.pack()

window.mainloop()