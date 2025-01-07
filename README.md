# Python Screenshot Server-Client

A simple project using Python with the following libraries:
- `socket`: To create a connection between the server and the client.
- `pyautogui`: To capture a screenshot from the server.
- `pygame`: To display the image on the client interface.

## Project Idea
The project consists of a server that captures a screenshot using `pyautogui` and sends it over the network using `socket`. The client receives the image and displays it in a window using `pygame`.

---

## Requirements
To run the project, make sure you have the following:

- Python 3.7 or higher
- socket (built-in library in Python)
- pyautogui
- pygame

Install the required libraries using pip:
```bash
pip install pyautogui pygame
