from tkinter import *

window = Tk()
window.title("주스 키오스크, 2501110203, 김호석")
window.resizable(width=FALSE, height=FALSE)
window.config(padx=20, pady=20)
window.config(bg="#f8f8fa")



# ============ 가격 계산 함수 ============
# 변수 준비
fruit_list = ["사과", "딸기", "바나나", "망고", "키위"]
size_list = ["Small", "Medium", "Large"]

size_costs = [1.0, 1.2, 1.3]
fruit_costs = [4500, 5500, 4000, 5500, 5000]

fruit = 0
size = 0

# 계산 함수
def calc_price(fruit, size):
	price = int(fruit_costs[fruit] * size_costs[size])
	lbl_price.config(text=f"가격 : {price:,}원")

	name = f"{fruit_list[fruit]}주스 {size_list[size]}사이즈"
	lbl_result.config(text=f"선택한 음료 : {name}")


# 과일 선택 함수
def choice_fruit(idx):
	global fruit
	fruit = idx

	calc_price(fruit, size)

# 컵 사이즈 선택 함수
def choice_size(idx):
	global size
	size = idx

	calc_price(fruit, size)



# ============ 이미지 List 준비 ============
img_path = "./imgs"

fruit_img_list = [f"{img_path}/fruit0{num}.png" for num in range(1,6)]
cup_img_list = [f"{img_path}/cup0{num}.png" for num in range(1,4)]
photoimgs = []



# ============ 요소 생성 ============
# 라벨 생성
lbl_fruit = Label(window, text="과일 선택", font=("",20, "bold"), bg="#ff7b8a")
lbl_cup = Label(window, text="컵 사이즈 선택", font=("",20, "bold"), bg="#ff7b8a")
lbl_result = Label(window, text="선택한 음료 : ", font=("",15, "bold"), bg="#f8f8fa", width=35, anchor=W)
lbl_price = Label(window, text="가격 : ", font=("",15, "bold"), bg="#f8f8fa", width=35, anchor=W)

# 프레임 생성
frame_fruit = Frame(window, bg="#f8f8fa")
frame_cup = Frame(window, bg="#f8f8fa")

# 이미지 라벨 생성
def set_imgs(frame, item_list, img_list, callback):
	for idx, img in enumerate(img_list):
		photo = PhotoImage(file=img)
		photoimgs.append(photo)
		lbl = Button(frame, image=photo, text=item_list[idx], compound=TOP, bg="pink", font=("",12, "bold"), width=150, height=170, command=lambda x=idx: callback(x))

		lbl.pack(side=LEFT, padx=10)

set_imgs(frame_fruit, fruit_list, fruit_img_list, choice_fruit)
set_imgs(frame_cup, size_list, cup_img_list, choice_size)



# ============ 요소 배치 ============
lbl_fruit.pack(pady=10)
frame_fruit.pack(pady=(0,20))
lbl_cup.pack(pady=10)
frame_cup.pack(pady=(0,20))
lbl_result.pack()
lbl_price.pack()



window.mainloop()