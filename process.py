import cv2

def process_image(path):
    img = cv2.imread(path)

    if img is None:
        return "Khong doc duoc anh!"

    h, w, _ = img.shape
    return f"Anh hop le! kich thuoc: {w}x{h}"
