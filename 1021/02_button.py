from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Buttons")
window.geometry("400x400")
window.resizable(width= FALSE, height = FALSE)



# Button
	# command : 버튼 클릭시 실행할 함수를 지정하는 옵션
		# quit : tkinter 내장함수 (mainloop()를 종료)
	# Label처럼 image 속성 사용 가능
btn1 = Button(window, text="창 닫기", fg="red", command=quit)
btn1.pack()



# messagebox
	# showinfo() : 알림 표시
	# showerror() : 에러 표시
	# showwarning() : 경고창 표시
		# 첫번째 인자 : title
		# 두 번째 인자 : message
def showImage():	
	messagebox.showinfo("알림", "알림입니다.")
	messagebox.showerror("에러","에러 발생.")
	messagebox.showwarning("경고","경고합니다.")

# command에 커스텀 함수 지정
btn2 = Button(window, text="알림 표시", command=showImage)
btn2.pack()



# Button 클릭 시 Label 추가
def addLabel():
	lbl = Label(window, text="라벨")
	lbl.pack()
btn3 = Button(window, text="라벨 추가", command=addLabel)
btn3.pack()



# Checkbutton
def check():
	if chk.get() == 0:	# get, set method 사용 가능
		messagebox.showinfo("체크", "체크버튼이 꺼졌습니다.")
	else: 
		messagebox.showinfo("체크", "체크박스가 켜졌습니다.")

# tkinter 전용 클래스 (위젯들과 연동할 수 있는 변수를 만들어줌)
	# 그냥 일반 변수를 넣으면 안됨!
chk = IntVar()	

# variable속성 : 체크상태를 저장할 변수 지정 (Checkbox객체에 상태를 저장하지 않음)
	# 0 : False
	# 1 : True
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=check)
cb1.pack()



# Radiobutton
# Lambda 연습을 위해 lbl 파라미터 지정
def configLabel(lbl):
	if rbChk.get() == 1:
		lbl.config(text= "선택한 버튼 : Python")
	elif rbChk.get() == 2:
		lbl.config(text="선택한 버튼 : C")
	elif rbChk.get() == 3:
		lbl.configure(text="선택한 버튼 : Java")


rbChk = IntVar()
rb1 = Radiobutton(window, text="Python", variable=rbChk, value=1, command=lambda:configLabel(lbl5))
rb2 = Radiobutton(window, text="C", variable=rbChk, value=2, command=lambda: configLabel(lbl5))
rb3 = Radiobutton(window, text="Java", variable=rbChk, value=3, command=lambda: configLabel(lbl5))
lbl5 = Label(window, text="선택한 버튼 : ")

rb1.pack()
rb2.pack()
rb3.pack()
lbl5.pack()

window.mainloop()