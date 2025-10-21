from tkinter import *
from time import *
import sys


window = Tk()
window.title("사진 앨범")
window.resizable(width=FALSE, height=FALSE)
window.geometry("700x500")


# 변수 선언
fileList = ["imgs/img0"+str(i)+".png" for i in range(1,5)]
photoList = [PhotoImage(file=fileList[i]) for i in range(4)]
index = 0



# 함수 정의
def clickNext():
	global index
	index += 1
	if index > 3: index = 0

	pLabel.config(image=photoList[index])
	nLabel.config(text=fileList[index].replace("imgs/",''))
	print(sys.getrefcount(photo))	
	# 해당 객체를 가리키는 참조 수를 반환
	# (함수 호출 시 임시 참조가 추가되어 실제 참조 수보다 1 많음)

def clickPrev():
	global index
	index -= 1
	if index < 0: index = 3

	nLabel.config(text=fileList[index].replace("imgs/",''))
	# pLabel.config(image=photoList[index])
	pLabel["image"] = photoList[index] # 이것도 가능
	# tkinter 위젯은 내부적으로 속성을 key-value 형태로 관리함



# main
btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)
nLabel = Label(window, text=fileList[0].replace("imgs/",''))

photo = PhotoImage(file=fileList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
nLabel.place(x=500, y=10)
pLabel.place(x=15, y=50)



window.mainloop()