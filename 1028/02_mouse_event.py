from tkinter import *
from tkinter import messagebox

def clickMouse(e):
	txt1 = ""
	if e.num == 1:
		txt1 += "마우스 왼쪽 버튼이 "
	elif e.num == 2:
		txt1 += "마우스 가운데 버튼이 "
	elif e.num == 3:
		txt1 += "마우스 오른쪽 버튼이 "

	txt1 += f"({e.x},{e.y})에서 클릭됨"
	txt2 = f"절대 좌표 : ({e.x_root}, {e.y_root})"
	lbl1.config(text=txt1)
	lbl2.config(text=txt2)


window = Tk()
window.title("Mouse Event")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)

lbl1 = Label(window, text="이곳이 바뀜")
lbl1.pack(expand=1, anchor=CENTER)

lbl2 = Label(window, text="이곳이 바뀜")
lbl2.pack(expand=1, anchor=CENTER)

window.bind("<Button>", clickMouse)

# 마우스 이벤트
'''
마우스 클릭 시 :
모든 버튼 공통 : <Button>
왼쪽 버튼 : <Button-1>
가운데 버튼 : <Button-2>
오른쪽 버튼 : <Button-3>

마우스 클릭 떼었을 때 :
모든 버튼 공통 : <ButtonRelease>
왼쪽 버튼 : <ButtonRelease-1>
가운데 버튼 : <ButtonRelease-2>
오른쪽 버튼 : <ButtonRelease-3>

마우스 더블 클릭 시 :
모든 버튼 공통 : <Double-Button>
왼쪽 버튼 : <Double-Button-1>
가운데 버튼 : <Double-Button-2>
오른쪽 버튼 : <Double-Button-3>

마우스 드래그 시 :
왼쪽 버튼 : <B1-Motion>
가운데 버튼 : <B2-Motion>
오른쪽 버튼 : <B3-Motion>

마우스 커서 올렸을 시 : <Enter>
마우스 커서 내릴 시 : <Leave>
'''

window.mainloop()