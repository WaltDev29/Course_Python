from tkinter import *

window = Tk()
window.title("pack()")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)



# pack() 속성들
btn1 = Button(window, text="버튼1")
btn2 = Button(window, text="버튼2")
btn3 = Button(window, text="버튼3")


# pack()의 속성들
	# side : 위젯의 배치위치 지정 (TOP, BOTTOM, LEFT, RIGHT)
	# expand : 부모 위젯의 남은 공간을 차지할지 TRUE/FALSE(기본값)
	# fill : 남은 공간을 어떻게 채울지 지정
		# NONE : 채우지 않음 (기본값)
		# X : 가로 방향으로 채움
		# Y : 세로 방향으로 채움
		# BOH : 가로,세로 모두 채움
	# ipadx, ipady : x,y 내부 패딩 
	# padx, pady : x,y 외부 패딩 (margin)
btn1.pack(side=LEFT, fill=Y, ipadx=30, ipady=30)
btn2.pack(side=LEFT,padx=20, pady=20)
btn3.pack(side=BOTTOM, fill=X, ipadx=10, ipady=10 ,padx=10, pady=10)

window.mainloop()