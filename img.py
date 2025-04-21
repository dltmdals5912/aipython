from PIL import Image, ImageTk

def load_image(name, size=(400, 300)):
    """
    주어진 이름(name).jpg 파일을 열어 지정된 크기로 리사이즈한 뒤,
    Tkinter에서 사용할 수 있는 PhotoImage 객체로 반환합니다.
    """
    path = f"{name}.jpg"
    pil_img = Image.open(path)
    pil_img = pil_img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(pil_img)