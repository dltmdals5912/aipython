import tkinter as tk
from PIL import Image, ImageTk

# 표시할 이미지 이름 리스트
FILE_NAMES = ["비행기", "트럭", "버스"]
# 홈 화면에 표시할 이미지 이름 (확장자 생략)
HOME_IMAGE = "home"
# 홈 화면 텍스트
HOME_TEXT = "홈 화면 이미지"

# 이미지 로드 함수
def load_image(name, size=(400, 300)):
    """
    주어진 이름(name).jpg 파일을 열어 지정된 크기로 리사이즈한 뒤,
    Tkinter에서 사용할 수 있는 PhotoImage 객체로 반환합니다.
    """
    path = f"{name}.jpg"
    pil_img = Image.open(path)
    pil_img = pil_img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(pil_img)

# GUI 생성
root = tk.Tk()
root.title("이미지 표시 앱")

# 버튼 프레임
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# 홈 이미지 로드
home_img = load_image(HOME_IMAGE)

# 이미지 레이블 생성 (초기: 홈 이미지 + 텍스트)
image_label = tk.Label(
    root,
    image=home_img,
    text=HOME_TEXT,
    compound="top",
    fg="#333333",
    anchor="center"
)
image_label.image = home_img
image_label.pack(padx=10, pady=10)

# 홈 화면으로 리셋
def go_home():
    image_label.config(image=home_img, text=HOME_TEXT)
    image_label.image = home_img

# 버튼 클릭 시 해당 이미지 표시
def on_click(name):
    tk_img = load_image(name)
    image_label.config(image=tk_img, text="")
    image_label.image = tk_img

# 홈 버튼
home_btn = tk.Button(
    btn_frame,
    text="홈",
    width=8,
    command=go_home
)
home_btn.pack(side="left", padx=5)

# 이미지 버튼들
for name in FILE_NAMES:
    btn = tk.Button(
        btn_frame,
        text=name,
        width=8,
        command=lambda n=name: on_click(n)
    )
    btn.pack(side="left", padx=5)

# 메인 루프 실행
root.mainloop()