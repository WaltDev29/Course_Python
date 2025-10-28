from tkinter import *
from tkinter import messagebox

window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("400x400")
window.title("Mouse Event")

def click(e):
	print(f"이벤트 타입 :", e.type)
	print(f"이벤트 :", e.num)
	print(f"위젯 :", e.widget)
	print(f"위젯 내 좌표", e.x, e.y)
	print(f"화면(디스플레이) 좌표 :", e.x_root, e.y_root)
	print(f"시간 :", e.time)
	print(f"시리얼 :", e.serial)		
	print("\n")

window.bind("<Button>", click)
window.mainloop()