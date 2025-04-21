import tkinter as tk
from img import load_image

# 표시할 이미지 이름 리스트
FILE_NAMES = ["비행기", "트럭", "버스"]
# 홈 화면에 표시할 이미지 이름 (확장자 .jpg는 생략)
HOME_IMAGE = "home"

# 초기 라벨 텍스트
HOME_TEXT = "홈 화면 이미지"

# GUI 생성
root = tk.Tk()
root.title("이미지 표시 앱")

# 버튼 프레임
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# 홈 이미지 로드
home_img = load_image(HOME_IMAGE)

# 이미지 표시용 레이블 (초기에는 홈 이미지로 표시)
image_label = tk.Label(
    root,
    image=home_img,
    text=HOME_TEXT,
    compound="top",  # 이미지 위 텍스트
    fg="#333333",
    anchor="center"
)
image_label.image = home_img
image_label.pack(padx=10, pady=10)

# 홈으로 돌아가기 함수
def go_home():
    image_label.config(image=home_img, text=HOME_TEXT)
    image_label.image = home_img

# 버튼 클릭 시 이미지 로드 및 표시 함수
def on_click(name):
    tk_img = load_image(name)
    image_label.config(image=tk_img, text="")
    image_label.image = tk_img  # 참조 유지

# 홈 버튼 생성
home_btn = tk.Button(
    btn_frame,
    text="홈",
    width=8,
    command=go_home
)
home_btn.pack(side="left", padx=5)

# 이미지 버튼 생성
for name in FILE_NAMES:
    btn = tk.Button(
        btn_frame,
        text=name,
        width=8,
        command=lambda n=name: on_click(n)
    )
    btn.pack(side="left", padx=5)

# 메인 루프
root.mainloop()