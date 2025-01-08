import mss
from PIL import Image
import io

def Screenshot():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])

    img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    binary_data = buffer.getvalue()
    buffer.close()

    return binary_data



if __name__ == "__main__":
    i = 1
    while True:
        Screenshot()
        print(i)
        i+=1
