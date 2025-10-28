from tkinter import *
from tkinter import messagebox

def showMessages():
	# 알림
	messagebox.showinfo("알림", "알림창입니다.")
	messagebox.showwarning("경고", "경고창입니다.")
	messagebox.showerror("에러", "에러창입니다.")

	# 확인
	messagebox.askyesno("Y/N", "askyesno")
	messagebox.askokcancel("Ok/Cancel", "askokcancel")
	messagebox.askyesnocancel("Y/N/Cancel", "askyesnocancel")
	messagebox.askquestion("Question", "askquestion")
	messagebox.askretrycancel("Retry/Cancel", "askretrycancel")

window = Tk()
window.title("Message Box")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)

btn1 = Button(window, text="메시지창 출력", command=showMessages)
btn1.pack()

window.mainloop()