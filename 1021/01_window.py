from tkinter import *

window = Tk()	# 윈도우 객체를 생성
window.title("Window")	# 타이틀 지정
# window.geometry("400x400")	# 윈도우 창 크기 설정 
# (지정하지 않으면 요소에 맞게 자동으로 지정됨)
window.resizable(width= FALSE, height = FALSE)	# 창 크기 조절 FALSE



# Label
	# fg : 글자색
	# bg : 배경색
	# anchor : 위젯 배치 위치
		# SE : South East
lbl1 = Label(window, text = "Python")
lbl2 = Label(window, text="tkinter", font=("궁서체", 30), fg="blue")
lbl3 = Label(window, text="공부중입니다.", bg="magenta", width=20, height=5, anchor=SE)

# 라벨 attach (pack한 순서대로 배치됨)
lbl1.pack()
lbl2.pack()
lbl3.pack()



# PhotoImage
photo = PhotoImage(file="imgs/walking_duck.gif")
lbl4 = Label(window, image=photo)
lbl4.pack()

# 이 코드는 image가 변수에 할당되지 않아 
# 가비지 컬렉션 때문에 image가 메모리에서 지워지는듯
# lbl5 = Label(window, image=PhotoImage(file="walking_duck.gif"))



# 윈도우 창이 계속 표시되도록 루프를 돌림
window.mainloop()