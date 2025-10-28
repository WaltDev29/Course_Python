from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Menu")
window.geometry("400x400")
window.resizable(width=FALSE, height=FALSE)


mainMenu = Menu(window)	# 메인 메뉴 생성
window.config(menu=mainMenu)	# window의 menu에 설정

fileMenu = Menu(mainMenu, tearoff=0)	# 하위 메뉴 생성 (tearoff : 메뉴 분리)
mainMenu.add_cascade(label="파일", menu=fileMenu)	# 상위/하위 메뉴 연결
fileMenu.add_command(label="열기")	# 세부 메뉴 추가
fileMenu.add_separator()	# 구분선 추가
fileMenu.add_command(label="종료")	# 세부 메뉴 추가


# 메뉴 메서드
'''
add_cascade(매개변수) : 상위메뉴와 하위 메뉴 연결
add_command(매개변수) : 기본 메뉴 항목 생성
add_radiobutton(매개변수) : 라디오버튼 메뉴 항목 생성
add_checkbutton(매개변수) : 체크버튼 메뉴 항목 생성
add_separator() : 구분선 생성

add(유형, 매개변수) : 특정 유형의 메뉴 항목 생성
delete(start_index, end_index) : start~end의 항목 삭제
entryconfig(index, 매개변수) : index 위치의 메뉴 항목 수정
index(item) : item 메뉴 항목의 index 반환
insert_separator(index) : index 위치에 구분선 생성
invoke(index) : index 위치의 항목 실행
tpye(속성) : 선택 유형 반환 (command, radiobutton, cascade ...)
'''

window.mainloop()