from tkinter import *
from tkinter.filedialog import *

# filedialog 함수
'''
# 파일 경로 반환
askopenfilename() : 파일 하나 선택 -> 파일 경로 반환
askopenfilenames() : 여러 파일 선택 -> 파일 경로 리스트 반환

# 파일 객체 반환
askopenfile() : 파일 하나 선택 -> 파일 객체 반환
askopenfiles() : 여러 파일 선택 -> 파일 객체 리스트 반환

# 파일 저장
asksaveasfilename() : 저장할 파일 경로 선택 -> 경로 반환
asksaveasfile() : 저장할 파일 선택 -> 파일 객체 반환

# 디렉토리 경로 반환
askdirectory() : 디렉토리 선택 -> 경로 반환
'''



def selectFile():
	file_name = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"),
													   ("모든 파일", "*.*")))
	lbl1.config(text=f"선택된 파일 : {file_name}")

def saveFile():
	# asksaveasfile의 반환값 : 저장한 file을 열어서 객체로 반환
	file = asksaveasfile(parent=window, mode='w', defaultextension=".txt",
						   filetypes=(("Text 파일", "*.txt"),("모든 파일", "*.*")))
	file.write("test test test")
	file.close()	# file을 열었으니 닫아줘야 함	

	lbl2.config(text=f"저장된 파일 : {file}")

window = Tk()
window.title("File")
window.geometry("600x200")



# 파일 선택
btn1 = Button(window, text="파일 선택", command=selectFile)
btn1.pack()

lbl1 = Label(window, text="선택된 파일 : ")
lbl1.pack()



# 파일 저장
btn2 = Button(window, text="파일 저장", command=saveFile)
btn2.pack()

lbl2 = Label(window, text="저장된 파일 : ")
lbl2.pack()



window.mainloop()