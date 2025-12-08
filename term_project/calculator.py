from tkinter import *

window = Tk()
window.title("KOPO 계산기, 2501110203, 김호석")

window.resizable(width=FALSE, height=FALSE)



# ============ 프레임 설정 ============
frame_top = Frame(window, bd=1, relief="solid")
frame_bottom = Frame(window, padx=10, pady=10)

frame_top.pack(side=TOP, fill=BOTH, padx=10, pady=(10,0))
frame_bottom.pack(side=BOTTOM, fill=BOTH)



# ============ 계산 함수 ============
# 변수 준비
txt_result, txt_progress = "", ""
num = ""
symbol = ""
result = ""

# 함수
def put_txt(lbl):
	global txt_result, txt_progress, num, symbol

	if txt_result == "" and lbl == '.': return

	# 숫자 입력 시 txt 업데이트
	if lbl in map(str, range(0,10)) or lbl == '.':
		txt_result = txt_result + lbl
		lbl_result.config(text=txt_result)

	# 연산자 입력 시 계산
	else:
		# 연산자만 입력 시 연산자 변경
		if txt_result == "":			
			if txt_progress != "":
				txt_progress = txt_progress[:-2] + lbl + " "
				lbl_progress.config(text=txt_progress)
				symbol = lbl
			else: return

		# num 비어있으면 num에 대입
		elif num == "":
			# num에 숫자 대입
			if '.' in txt_result: num = float(txt_result)
			else: num = int(txt_result)

			# symbol에 연산자 대입
			symbol = lbl

			# 디스플레이 초기화
			txt_progress = txt_result + f" {lbl} "
			lbl_progress.config(text=txt_progress)

			txt_result = ""
			lbl_result.config(text="")
		
		# num에 값이 있으면 계산
		else:
			# num2에 숫자 대입
			if '.' in txt_result: num2 = float(txt_result)
			else: num2 = int(txt_result)

			# 계산
			if symbol == '＋': num = num + num2
			elif symbol == '－': num = num - num2
			elif symbol == '×': num = num * num2
			elif symbol == '÷': num = num / num2

			# symbol 대입
			symbol = lbl

			# 디스플레이 초기화
			txt_progress = str(round(num,3)) + f" {lbl} "
			lbl_progress.config(text=txt_progress)

			txt_result = ""
			lbl_result.config(text="")



# ============ 지우기 함수 ============
def erase():
	global txt_result
	if txt_result == "": return
	else:
		txt_result = txt_result[:-1]
		lbl_result.config(text=txt_result)
		


# ============ 결과 출력 함수 ============
def calc_result():
	global txt_result, txt_progress, num, symbol

	# 계산할 두 번째 숫자를 입력하지 않은 경우
	if txt_result == "":
		txt_result = str(num)
		lbl_result.config(text=num)
		lbl_progress.config(text="")

		# 변수 초기화
		symbol = ""
		txt_result = ""
		txt_progress = ""

	else:
		# num2에 숫자 대입
		if '.' in txt_result: num2 = float(txt_result)
		else: num2 = int(txt_result)

		txt_progress = f"{str(num)} {symbol} {str(num2)} = "

		# 계산
		if symbol == '＋': num = num + num2
		elif symbol == '－': num = num - num2
		elif symbol == '×': num = num * num2
		elif symbol == '÷': num = num / num2

		txt_result = str(round(num,3))

		lbl_progress.config(text=txt_progress)
		lbl_result.config(text=txt_result)

		# 변수 초기화
		symbol = ""
		txt_result = ""
		txt_progress = ""
		# num = ""



# ============ 디스플레이 설정 ============

lbl_progress = Label(frame_top, text="", anchor=E)
lbl_result = Label(frame_top, text="", anchor=E, font=(20))

lbl_progress.pack(fill=BOTH)
lbl_result.pack(fill=BOTH)



# ============ 버튼 배치 ============
# 버튼 배열 설정
btn_lbls = [
	['7','8','9','÷'],
	['4','5','6','×'],
	['1','2','3','－']
	]

# 배열 순회하여 버튼 생성 및 배치
for row, lbls in enumerate(btn_lbls):
	for col, lbl in enumerate(lbls):
		btn = Button(frame_bottom, text=lbl, width=5, height=2, command=lambda x=lbl: put_txt(x))
		btn.grid(row=row, column=col, padx=2, pady=2)


# 0, '.', '+' 버튼 생성
btn_0 = Button(frame_bottom, text='0', width=5, height=2, command=lambda: put_txt('0'))
btn_dot = Button(frame_bottom, text='.', width=5, height=2, command=lambda: put_txt('.'))
btn_plus = Button(frame_bottom, text="＋", width=5, height=2, command=lambda: put_txt("＋"))

# 0, '.', '+' 버튼 배치
btn_0.grid(row=3, column=0, columnspan=2, sticky=EW, padx=2, pady=2)
btn_dot.grid(row=3, column=2, padx=2, pady=2)
btn_plus.grid(row=3, column=3, padx=2, pady=2)

# '<-', '=' 버튼 생성
btn_erase = Button(frame_bottom, text="<-", width=5, height=2, command=erase)
btn_equal = Button(frame_bottom, text="＝", width=5, height=2, command=calc_result)

# '<-', '=' 버튼 배치
btn_equal.grid(row=4, column=0, columnspan=2, sticky=EW, padx=2, pady=2)
btn_erase.grid(row=4, column=2, columnspan=2, sticky=EW, padx=2, pady=2)
	


window.mainloop()