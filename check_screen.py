import pyautogui
from pynput.mouse import Listener
import screeninfo

# Get information about screens
screens = screeninfo.get_monitors()

def get_screen_sizes():
    screen_sizes = []
    for i, monitor in enumerate(screens, start=1):
        width = monitor.width
        height = monitor.height
        screen_sizes.append((f"Screen {i}", width, height))
    return screen_sizes

def on_click(x, y, button, pressed):
    if pressed:
        for i, monitor in enumerate(screens, start=1):
            print(screens)
            if monitor.x <= x <= monitor.x + monitor.width and monitor.y <= y <= monitor.y + monitor.height:
                print(f"Screen {i} has been clicked!")
                break

if len(screens) == 2:
    screen_sizes = get_screen_sizes()
    screen1_region = (screens[0].x, screens[0].y, screens[0].width, screens[0].height)
    screen2_region = (screens[1].x, screens[1].y, screens[1].width, screens[1].height)
    with Listener(on_click=on_click) as listener:
        listener.join()
else:
    print("This script requires exactly 2 screens.")
