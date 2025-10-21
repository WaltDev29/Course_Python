from tkinter import *

window = Tk()
window.title("place()")
window.geometry("1024x1024")
window.resizable(width=FALSE, height=FALSE)



# 변수 준비
btnList = []
fileList = ["imgs/img0"+str(i)+".png" for i in range(1,5)]
photoList = []


# 버튼 생성
for i in range(4):
	photoList.append(PhotoImage(file=fileList[i]))
	btnList.append(Button(window, image=photoList[i]))



# 버튼 배치
index = 0
xPos = 0
yPos = 0
for i in range(2):
	for j in range(2):
		# place() : 좌표값으로 위젯 배치
		btnList[index].place(x=xPos, y=yPos)
		index += 1
		xPos += 526
	xPos = 0
	yPos += 526



window.mainloop()