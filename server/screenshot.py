import pyautogui
import io
import random

def Screenshot():
    screenshot = pyautogui.screenshot()

    buffer = io.BytesIO()
    screenshot.save(buffer, format="JPEG")
    binary_data = buffer.getvalue()
    buffer.close()

    return binary_data


if __name__ == "__main__":
    i = 1
    while True:
        Screenshot()
        print(i)
        i+=1
