import os
import time
import pyautogui
from pynput.mouse import Listener

# Path to save the screenshots
save_path = r'D:\Github\Activity.tracking_model\images'

# Function to capture screenshot and save it
def capture_and_save():
    timestamp = time.strftime('%Y%m%d%H%M%S')
    file_name = os.path.join(save_path, f'{timestamp}_img.png')
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)
    print(f'Screenshot saved as {file_name}')

# Function to monitor mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        capture_and_save()

# Start mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()
