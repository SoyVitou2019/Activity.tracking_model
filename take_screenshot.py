import mss
import mss.tools
from pynput import mouse
from datetime import datetime

def get_screen(x, y):
    # You can customize this function to determine which screen the coordinates (x, y) belong to.
    # This example assumes a horizontal setup with equal-sized screens.
    screen_width = 1920  # Width of each screen
    if x < screen_width:
        return 1  # First screen
    else:
        return 2  # Second screen

def on_click(x, y, button, pressed):
    if pressed:
        monitor_number = get_screen(x, y)
        print(f"Clicked at ({x}, {y}) on screen {monitor_number}")

        with mss.mss() as sct:
            # Get information of the clicked monitor
            mon = sct.monitors[monitor_number]

            # The screen part to capture
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }
            # Generate image name based on current time
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output = f"./images/sct-mon{monitor_number}_{current_time}.png"

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            print(f"Screenshot saved as {output}")

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
